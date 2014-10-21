#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2007-2008 Sippy Software, Inc. All rights reserved.
#
# This file is part of SIPPY VAPP, a free IVR library.
#
# SIPPY VAPP is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# For a license to use the SIPPY VAPP software under conditions
# other than those described here, or to purchase support for this
# software, please contact Sippy Software, Inc. by e-mail at the
# following addresses: sales@sippysoft.com.
#
# SIPPY VAPP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

import getopt
import sys
import codecs
import re
import os
import random
import datetime
from os.path import join, abspath
import gettext
import vapp
from vapp.SpeechSynth.PromptException import PromptException
import logging
import pkgutil
from vapp import TextSynth

TAG_RE = r'((%\([^)]*\)\[[^]]*\][nsdD]|%\([^)]*\)[nsdD]|%[nsdD]|%\[[^]]*\][nsdD]))'

logger = logging

class MyException(Exception):
    pass

def usage(e):
    print e
    print("""
usage: prompt_utils.py [OPTIONS] COMMAND
OPTIONS:
    -l, --lang=LANG	  - specify the language (default: en)
    -p, --promptpath=DIR  - specify the path to prompts
    -o, --optimize	  - optimize sentences in phrases
    --filter-untranslated - filter out untranslated phrases
    -d, --debug		  - enable debug info
    --enum=start_num	  - add numbers as the first column starting with 
			    start_num
    --enum-suffix	  - suffix to be appended to the enum values
    --extra-extensions    - check prompts with these extensions 
                            (comma or pipe separated list)

COMMANDS:
    list phrases	- list all phrases
    list mappings	- list all phrases with existing prompt (existence
			  of prompt files is not verified)
    list unmapped	- find all phrases that cannot be transformed into a
			  prompt file sequence
    list orphans	- list unused prompt files for the specified language
    verify mappings     - check existence of prompt files (no phrase check)
    make stoplist       - create stop list from unmapped phrases
    generate tests      - find all dynamic messages and generate test data
                          for them to allow to see the final phrases.
""")
    
class PhraseContainer(object):
    def __init__(self, lang, opts):
	self.setLang(lang)
	self.__opts = opts
        self.__raw_msgs = []
        self.__raw_msgs_plural = []
        self.orig_local_by_chunk = {}
        self.orig_eng_by_chunk = {}
        self.control_phrases = {}
        self.opt_hash = {}
        self.__stoplist = {}
        self.__tagged = []

        self.__load_stoplist()
	self.__load_phrases()

    def __load_stoplist(self):
        fname = "prompt-stoplist-" + self.__lang + ".txt"
        try:
            fd = file(fname)
            for l in fd.readlines():
                self.__stoplist[l.rstrip()] = 1
        except IOError:
            pass

    def __load_pot(self, fname):
	STATE_IDLE = 1
	STATE_MSGID = 2
	STATE_MSGIDPLURAL = 3

	state = STATE_IDLE
	pot = file(fname, "r")
	skip_next = False
	for line in pot.readlines():
	    line = line.rstrip()
	    if (state == STATE_IDLE):
		if (line.startswith('#, fuzzy')):
		    skip_next = True
		if (line.startswith('msgid "')):
		    if (skip_next):
			skip_next = False
			continue
		    msg = line[7:(len(line) - 1)]
		    msg_plural = None
		    state = STATE_MSGID
	    elif (state == STATE_MSGID):
		if (line.startswith('"')):
		    msg += line[1:(len(line) - 1)]
		elif (line.startswith('msgid_plural "')):
		    msg_plural = line[14:(len(line) - 1)]
		    state = STATE_MSGIDPLURAL
		else:
		    self.addMsg(msg)
		    state = STATE_IDLE
	    elif (state == STATE_MSGIDPLURAL):
		if (line.startswith('"')):
		    msg_plural += line[1:(len(line) - 1)]
		else:
		    self.addMsgPlural(msg, msg_plural)
		    state = STATE_IDLE
	pot.close()

    def __load_phrases(self):
        for pot in vapp.default_pot_files():
            self.__load_pot(pot)
	#
	# Translate phrases
	#
	# 1. Translate simple phrases
	#
	for raw_message in self.__raw_msgs:
	    translated_message = self._(raw_message)
            if (self.__opts.filter_untranslated and raw_message == translated_message):
                continue

	    #
	    # Check %-tag consistency
	    #
	    self.checkTags(raw_message, translated_message)

	    #
	    # Split prase into chunks
	    #
	    for chunk in re.split('\s*' + TAG_RE + '\s*', translated_message):
		if (chunk.startswith('%') or chunk == ''):
		    continue
		# only punctuation left
		if (re.findall(r"^[.?!]+$", chunk)):
		    break
		# try to skip punctuation at the beginning of the phrase
		res = re.findall(r"^([.?!\s]+)(.*)$", chunk)
		if (res):
		    chunk = res[0][1].rstrip()
		self.addPhrase(chunk, raw_message, translated_message)
	#
	# 2. Translate plural forms
	#
	for singular, plural in self.__raw_msgs_plural:
	    for i in self.__plurals:
		translated_message = self._N(singular, plural, i)
                if (self.__opts.filter_untranslated and (singular == translated_message or plural == translated_message)):
                    continue
		#
		# Check %-tag consistency
		#
		self.checkTags(singular, translated_message)

		#
		# Split phrase into chunks
		#
		for chunk in re.split('\s*' + TAG_RE + '\s*', translated_message):
		    if (chunk.startswith('%') or chunk == ''):
			continue
                    if (i == 1):
                        self.addPhrase(chunk, singular, translated_message, i)
                    else:
                        self.addPhrase(chunk, plural, translated_message, i)

	#
	# Read appropriate language module
	#
        fname = pkgutil.find_loader('vapp.TextSynth.%s' % self.__lang.upper()).get_filename()
	f = file(fname, 'r')
	encoding = None
	for line in f.readlines():
	    line = line.rstrip()
	    if (encoding == None):
		if (line.startswith('# -*- coding:')):
		    encoding = line[14:(len(line) - 4)]
		elif (line.startswith('#')):
		    continue
		else:
		    encoding = 'ISO8859-1'
	    else:
		if (line.startswith('#')):
		    continue
		l = unicode(line, encoding)
		if (l.find('_phrase_noop') >= 0):
		    for i in re.findall(r'_phrase_noop\("[^"]*"\)|_phrase_noop\(\'[^\']*\'\)', l):
			r = i[14:(len(i) - 2)]
			self.addPhrase(r, None, None)

    def _(self, text):
	return self.__gettext(text)

    def _N(self, msg, msg_plural, n):
	return self.__ngettext(msg, msg_plural, n)

    def addMsg(self, msg):
	self.__raw_msgs.append(msg)

    def addMsgPlural(self, msg, msg_plural):
	self.__raw_msgs_plural.append((msg, msg_plural))

    def checkTags(self, orig_phrase, translated_phrase):
	original_tags = re.findall(TAG_RE, orig_phrase)
	translated_tags = re.findall(TAG_RE, translated_phrase)
	if (len(original_tags) > 0):
	    orig = []
	    for tag in original_tags:
		orig.append(self.stripTagFlags(tag[0]))
	    if (len(original_tags) != len(translated_tags)):
		print "ERROR: different number of %%-tags. Original phrase: %s" % orig_phrase
		sys.exit(1)
	    for tag in translated_tags:
		t = self.stripTagFlags(tag[0])
		if (t not in orig):
		    print "ERROR: %%-tag mismatch. Original phrase: '%s'" % orig_phrase
		    sys.exit(1)
		else:
		    orig.remove(t)

    def stripTagFlags(self, tag):
	ret = ""
	suppress = False
	for c in tag:
	    if (c == '['):
		suppress = True
	    elif (c == ']'):
		suppress = False
	    elif (not suppress):
		ret += c
	return ret

    def setLang(self, lang):
	if (lang in ('en', 'es', 'hy', 'fr', 'de')):
	    self.__plurals = [ 0, 1 ]
	elif (lang == 'ru'):
	    self.__plurals = [ 1, 2, 5 ]
	elif (lang == 'ar'):
	    self.__plurals = [ 1, 2, 3 ]
        elif (lang in ('th', 'zh', 'ja', 'tr', 'vi', 'ka')):
            self.__plurals = [ 0 ]
        else:
            print("ERROR: You must define __plurals for the language %s!!!" % lang)
            print("Please change the source code of this utility accordingly.")
            print("The code to be changed is above this message.")
            sys.exit(1)
	self.__lang = lang

	if (self.__lang != 'en'):
            locale = vapp.Locale(self.__lang)
	    self.__gettext = locale.gettext
	    self.__ngettext = locale.ngettext
	else:
	    self.__gettext = gettext.gettext
	    self.__ngettext = gettext.ngettext

    def optimize(self):
	class chunk_obj:
	    def __init__(self, chunk, orig_key, orig_phrases, orig_local):
		self.__orig_phrases = []
		self.__orig_phrases += orig_phrases
		self.__orig_keys = [ orig_key ]
                self.__orig_local = []
                self.__orig_local += orig_local
		self.chunk = chunk
		self.counter = 0

	    def append(self, orig_key, orig_phrases, orig_local):
		self.__orig_phrases += orig_phrases
		self.__orig_keys.append(orig_key)
		self.__orig_local += orig_local

	    def orig_keys(self):
		return self.__orig_keys

	    def orig_phrases(self):
		return self.__orig_phrases

            def orig_local(self):
                return self.__orig_local

        rel_hash = {}
	for orig_chunk in self.orig_eng_by_chunk.keys():
	    if (re.findall(r'[.?!]', orig_chunk)):
                regexp = unicode('[.?!。]', 'utf-8')
                rel_hash[orig_chunk] = []
		for chunk in re.split(r'[.?!]', orig_chunk):
		    chunk = chunk.strip()
		    if (chunk == ''):
			continue
		    if (self.opt_hash.has_key(chunk)):
			self.opt_hash[chunk].counter += 1
			self.opt_hash[chunk].append(orig_chunk, self.orig_eng_by_chunk[orig_chunk], self.orig_local_by_chunk[orig_chunk])
		    else:
			self.opt_hash[chunk] = chunk_obj(chunk, orig_chunk, self.orig_eng_by_chunk[orig_chunk], self.orig_local_by_chunk[orig_chunk])
                    rel_hash[orig_chunk].append(self.opt_hash[chunk])
	cnt = 0
	for c in self.opt_hash.values():
	    if (c.counter == 0):
		continue
	    for k in c.orig_keys():
                # flush all related chunks
                for rel in rel_hash[k]:
                    if (not self.orig_eng_by_chunk.has_key(rel.chunk)):
                        for idx in range(0, len(rel.orig_phrases())):
                            cnt += self.addPhrase(rel.chunk, rel.orig_phrases()[idx], rel.orig_local()[idx])
		if (self.orig_eng_by_chunk.has_key(k)):
#		    print "Removing phrase " + self.orig_eng_by_chunk[k][0]
		    self.orig_eng_by_chunk.pop(k)
		if (not self.orig_eng_by_chunk.has_key(c.chunk)):
		    for idx in range(0, len(c.orig_phrases())):
                        cnt += self.addPhrase(c.chunk, c.orig_phrases()[idx], c.orig_local()[idx])
	print("%d chunks created by the optimization process" % cnt)

    def addPhrase(self, chunk, orig_eng, orig_local, def_val = None):
        if orig_eng != None:
            res = re.findall(TAG_RE, orig_local)
            if len(res) > 0:
                tup = (orig_eng, orig_local, def_val)
                if tup not in self.__tagged:
                    self.__tagged.append(tup)
        if self.__stoplist.has_key(orig_eng):
            return
        if (not self.orig_local_by_chunk.has_key(chunk)):
            self.orig_local_by_chunk[chunk] = [ orig_local ]
        else:
            self.orig_local_by_chunk[chunk].append(orig_local)

	if (not self.orig_eng_by_chunk.has_key(chunk)):
	    self.orig_eng_by_chunk[chunk] = [ orig_eng ]
	    self.control_phrases[chunk] = {}
	    self.control_phrases[chunk][orig_eng] = 1
            return 1
	elif (not self.control_phrases[chunk].has_key(orig_eng)):
            self.orig_eng_by_chunk[chunk].append(orig_eng)
            self.control_phrases[chunk][orig_eng] = 1
            return 1
        return 0

    def chunks(self):
	return self.orig_eng_by_chunk.keys()

    def phraseByChunk(self, chunk):
	return self.orig_local_by_chunk[chunk]

    def origPhraseByChunk(self, chunk):
	return self.orig_eng_by_chunk[chunk]

    def chunkCount(self):
	return len(self.orig_eng_by_chunk.keys())

    tagged = property(lambda self : self.__tagged)

class Opts:
    filter_untranslated = False

class Checker:
    prompt_path = None
    optimize = False
    debug = False
    __enum_suffix = ""

    def __init__(self, argv):
	self.__opts = Opts()
	self.enum_start = None
        self.g711_nonconverable_exts = [ ]

	self.__lang = 'en'
	try:
	    opts, args = getopt.getopt(argv[1:], 'dol:f:p:', 
		    [ 'debug', 'optimize', 'lang=', 'promptpath',
		      'filter-untranslated', 'enum=', 'enum-suffix=',
                      'extra-extensions='])
	    for o, a in opts:
		if (o == '-l' or o == '--lang'):
		    self.__lang = a
		elif (o == '-p' or o == "--promptpath"):
		    if (not a.endswith('/')):
			a += '/'
		    self.prompt_path = [ a ]
		elif (o == "-o" or o == "--optimize"):
		    self.optimize = True
		elif (o == "-d" or o == "--debug"):
		    self.debug = True
                elif (o == "--filter-untranslated"):
                    self.__opts.filter_untranslated = True
		elif (o == '--enum'):
		    try:
			self.enum_start = int(a)
		    except ValueError:
			raise MyException("Bad argument for --enum: '%s'" % a)
		elif (o == '--enum-suffix'):
		    self.__enum_suffix = a
		elif (o == '--extra-extensions'):
		    self.g711_nonconverable_exts = re.split(',|', a)
		else:
		    sys.__stderr__.write("Unhandled option: '%s' = '%s'\n" % (o, a))
	    self.__phrases = PhraseContainer(self.__lang, self.__opts)
	    if (len(argv) < 3):
		raise MyException("error: No command given")
            handler = None
	    if (argv[len(argv) - 2] == 'list'):
		if (argv[len(argv) - 1] == 'phrases'):
		    handler = self.doListPhrases
		elif (argv[len(argv) - 1] == 'mappings'):
		    handler = self.doListMappings
		elif (argv[len(argv) - 1] == 'unmapped'):
		    handler = self.doListUnmapped
		elif (argv[len(argv) - 1] == 'orphans'):
		    handler = self.doListOrphans
	    elif (argv[len(argv) - 2] == 'verify'):
		if (argv[len(argv) - 1] == 'mappings'):
		    handler = self.doVerifyMappings
	    elif (argv[len(argv) - 2] == 'make'):
		if (argv[len(argv) - 1] == 'stoplist'):
                    handler = self.makeStopList
            elif (argv[-2] == 'generate'):
                if (argv[-1] == 'tests'):
                    handler = self.generateTests
            if (handler == None):
		raise MyException("error: No command found")

            if self.prompt_path == None:
                self.prompt_path = vapp.default_prompt_dirs()

            self.__speech_synth = vapp.SpeechSynth.Chunked.Chunked(self.__lang, self.prompt_path)
            handler()

	except MyException, e:
            usage(e)
        except getopt.GetoptError, e:
            usage(e)

    def _generateTest(self, tag, def_val, tag_name, hints):
        mode = tag[-1]
        flags = re.findall('\[(.+)\]', tag)
        if len(flags) > 0:
            flags = flags[0]
        else:
            flags = ""
        if mode == 's':
            return ""
        if mode == 'n':
            if 'D' in flags: # string of digits
                retval = ""
                for i in range(10):
                    x = int(random.random() * 10)
                    retval += str(x)
                return retval
            else: # number
                if False and def_val != None:
                    return def_val
                else:
                    start = 0
                    stop = 10000
                    if hints != None:
                        if hints.startswith("range"):
                            keyword, _start, _stop = hints.split()
                            _tag_name = None
                            if '(' in keyword:
                                _tag_name = re.findall(r'\((.+)\)', keyword)[0]
                            if _tag_name == None or tag_name == _tag_name:
                                start = int(_start)
                                stop = int(_stop)
                    return random.randint(start, stop)
        elif mode == 'd': # duration
            return int(random.random() * 10000)
        elif mode == 'D': # date
            return datetime.datetime.fromtimestamp(random.random() * 2000000000)

    def generateTests(self):
        test_hints = {}
        try:
            fd = file("vapp_test_hints.txt", "r")
            for l in fd.xreadlines():
                l = l.rstrip()
                phrase, hints = l.split("|", 1)
                test_hints[phrase] = hints
        except IOError:
            pass

	out_fname = "test-" + self.__lang
        out_fname += ".html"
	out = codecs.open(out_fname, "w", 'utf-8')
	self.writeHeader(out)
        out.write("""
<H2>Tests for the language %s</H2>
<table border="1">
<tr bgcolor="#E0E0E0">
    <th>Localized message</th>
    <th>Localized template</th>
    <th>Original message</th>
    <th>Original template</th>
</tr>
""" % self.__lang)
        synth = TextSynth.TextSynth(vapp.Locale(self.__lang))
        en_synth = TextSynth.TextSynth(vapp.Locale('en'))
        for (phrase_en, phrase_local, def_val) in self.__phrases.tagged:
            res = re.findall(TAG_RE, phrase_local)
            named_params = {}
            unnamed_params = []
            skip = None
            for tag in res:
                tag = tag[0]
                res2 = re.findall(r'\((.+)\)', tag)
                tag_type = tag[-1]
                if tag_type == "s" and skip == None:
                    skip = True
                else:
                    skip = False
                hints = test_hints.get(phrase_en, None)
                if len(res2) > 0:
                    name = res2[0]
                    named_params[name] = self._generateTest(tag, def_val, name, hints)
                else:
                    unnamed_params.append(self._generateTest(tag, def_val, None, hints))
            if skip:
                continue
            p_l = synth.say(phrase_local, args = unnamed_params, kw = named_params)
            p_en = en_synth.say(phrase_en, args = unnamed_params, kw = named_params)
            out.write("""
<tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
</tr>
""" % (p_l, phrase_local, p_en, phrase_en))
        out.write("""
</table>
</body></html>
""")
        print "%s created" % out_fname

    def doListPhrases(self):
        if (self.optimize):
            self.__phrases.optimize()
	out_fname = "phrases-%s.html" % self.__lang
	out = codecs.open(out_fname, "w", 'utf-8')
	self.writeHeader(out)
        out.write("""
<H2>All the phrase chunks for the language %s</H2>
<TABLE BORDER="1">
<TR BGCOLOR="#E0E0E0">
""" % self.__lang)
	if (self.enum_start != None):
	    out.write("<TH>#</TH>\n")
	out.write("""
    <TH>Phrase chunk</TH>
    <TH>Original localized phrase</TH>
    <TH>Original English phrase</TH>
</TR>
""")
        num = self.enum_start

	chunks = self.__phrases.chunks()
	chunks.sort()
	for chunk in chunks:
	    out.write("<TR><TD>")
	    if (self.enum_start != None):
		out.write("%d%s</TD><TD>" % (num, self.__enum_suffix))
                num += 1
	    out.write(chunk)
            out.write("</TD><TD>")
	    orig = self.__phrases.phraseByChunk(chunk)
            if (orig != None):
                sep = ""
		for o in orig:
		    if (o != None):
                        out.write(sep)
                        idx = o.find(chunk)
                        out.write(o[:idx])
                        out.write("<B>")
                        out.write(o[idx:idx + len(chunk)])
                        out.write("</B>")
                        out.write(o[idx + len(chunk):])
                    else:
                        out.write("&nbsp;")
                    sep = "<BR>"

            out.write("</TD><TD>")
	    orig = self.__phrases.origPhraseByChunk(chunk)
	    if (orig != None):
		sep = ""
		for o in orig:
		    out.write(sep)
		    if (o != None):
			out.write(o)
		    else:
			out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
		    sep = "<BR>"
	    else:
                out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
            out.write("</TD></TR>")
	    out.write('\n')
        out.write("""
</TABLE>
<B>%d phrases total</B>
""" % self.__phrases.chunkCount())
        #
        # dump optimization tree
        #
        if (self.optimize and self.debug):
            out.write("""
<HR>
<H5>Optimization statistics</H5>
<TABLE BORDER=1>
<TR>
<TH>Final phrase</TH>
<TH>Derived from</TH>
<TH>Original English</TH>
</TR>
""")
            for c in self.__phrases.opt_hash.values():
                if (c.counter == 0):
                    continue
                out.write("""
<TR>
<TD>%s</TD>
<TD>%s</TD>
<TD>%s</TD>
</TR>
""" % (c.chunk, "<BR>".join(c.orig_keys()), "<BR>".join(c.orig_phrases())))
            out.write("""
</TABLE>
""")

        out.write("""
</BODY></HTML>
""")
	
	print("%d phrase chunks have been written into the %s file." % (self.__phrases.chunkCount(), out_fname))

    def doListMappings(self):
	out_fname = "mappings-%s.html" % self.__lang
	out = codecs.open(out_fname, "w", 'utf-8')
	self.writeHeader(out)
        out.write("""
<H2>All existing phrase chunk mappings for the language %s</H2>
<TABLE BORDER="1">
<TR BGCOLOR="#E0E0E0">
    <TH>Phrase chunk</TH>
    <TH>Original phrase</TH>
    <TH>Prompt file sequence</TH>
</TR>
""" % self.__lang)


	p = self.__phrases.chunks()
	p.sort()
	for i in p:
	    try:
		seq = self.__speech_synth.promptFileSequence(i, True)
                out.write("<TR><TD>")
		out.write(i)
                out.write("</TD><TD>")
		orig = self.__phrases.origPhraseByChunk(i)
		if (orig != None):
		    sep = ""
		    for o in orig:
			out.write(sep)
			if (o != None):
			    out.write(o)
			else:
			    out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
			sep = "<BR>"
		else:
                    out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
                out.write("</TD><TD>")
		is_first = True
		for p in seq:
		    if (is_first):
			is_first = False
		    else:
                        out.write("<BR>")
		    if (p.startswith('/')):
			s = p
		    else:
			s = p[len(self.prompt_path):] # strip off the path
		    out.write(s)
                out.write("</TD><TR>\n")
	    except PromptException:
		pass
        out.write("</TABLE></BODY></HTML>")
	print("%s created" % out_fname)

    def makeStopList(self):
        out_fname = "prompt-stoplist-" + self.__lang + ".tmp"
        out = codecs.open(out_fname, "w", 'utf-8')

        p = self.__phrases.chunks()
        stoplist = {}
        for chunk in p:
            try:
                seq = self.__speech_synth.promptFileSequence(chunk, False)
            except PromptException:
                orig = self.__phrases.origPhraseByChunk(chunk)
                if (orig != None):
                    for o in orig:
                        if (o != None):
                            stoplist[o] = 1
        stoplist = stoplist.keys()
        stoplist.sort()
        for o in stoplist:
            out.write(o + "\n")
        print("%s created" % out_fname)


    def doListUnmapped(self):
	out_fname = "unmapped-%s.html" % self.__lang
	out = codecs.open(out_fname, "w", 'utf-8')
	self.writeHeader(out)
        out.write("""
<H2>All phrase chunks that don't have mappings in the language %s</H2>
<TABLE BORDER="1">
<TR BGCOLOR="#E0E0E0">
""" % self.__lang)
        if (self.enum_start != None):
            out.write("<TH>#</TH>")
        out.write("""
    <TH>Phrase chunk</TH>
    <TH>Original phrase</TH>
    <TH>Original English phrase</TH>
</TR>
""")

	p = self.__phrases.chunks()
	p.sort()
	for chunk in p:
	    try:
		seq = self.__speech_synth.promptFileSequence(chunk, False)
	    except PromptException:
                out.write("<TR><TD>")
		if (self.enum_start != None):
		    out.write("%s%s</TD><TD>" % (self.enum_start, self.__enum_suffix))
		    self.enum_start += 1
		out.write(chunk)

                out.write("</TD><TD>")
                orig = self.__phrases.phraseByChunk(chunk)
                if (orig != None):
                    sep = ""
                    for o in orig:
                        if (o != None):
                            out.write(sep)
                            idx = o.find(chunk)
                            out.write(o[:idx])
                            out.write("<B>")
                            out.write(o[idx:idx + len(chunk)])
                            out.write("</B>")
                            out.write(o[idx + len(chunk):])
                        else:
                            out.write("&nbsp;")
                        sep = "<BR>"

                out.write("</TD><TD>")
		orig = self.__phrases.origPhraseByChunk(chunk)
		if (orig != None):
		    sep = ""
		    for o in orig:
			out.write(sep)
			if (o != None):
			    out.write(o)
			else:
			    out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
			sep = "<BR>"
		else:
                    out.write('<B>Comes from TextSynt/%s.py</B>' % self.__lang.upper())
                out.write("</TD></TR>\n")
        out.write("</TABLE></BODY></HTML>")
	print("%s created" % out_fname)

    def doListOrphans(self):
        for p in self.prompt_path:
            self._doListOrphans(p)

    def _doListOrphans(self, prompt_path):
	basedir = prompt_path + "/" + self.__lang
	#
	# Check existing prompt files if they are used in the applications
	#
	file_by_name = {}
	for root, dirs, files in os.walk(basedir):
	    for f in files:
		if (not f.startswith("prompt_map") and not f.endswith(".txt")):
		    v = abspath(join(root, f))
		    key = re.sub(r'\..*$', '', v)
		    if (file_by_name.has_key(key)):
			file_by_name[key].append(v)
		    else:
			file_by_name[key] = [ v ]
	    if ('CVS' in dirs):
		dirs.remove('CVS')

	p = self.__phrases.chunks()
	p.sort()
	required_files = {}
	for i in p:
	    try:
		seq = self.__speech_synth.promptFileSequence(i, True)
		for f in seq:
		    k = abspath(f)
		    if (file_by_name.has_key(k)):
			file_by_name.pop(k)
		    required_files[k] = 1
	    except PromptException:
		pass
	p = file_by_name.keys()
	p.sort()
	print("\nUnused prompt files:\n")
	for k in p:
	    for f in file_by_name[k]:
		print f
	#
	# Find unused prompt mappings
	#
	print "\nUnused prompt mappings:\n"
        for map_fname in os.listdir(basedir):
            if (map_fname.startswith("prompt_map") and map_fname.endswith(".txt")):
                mapfile = file(join(basedir, map_fname), "r")
                encoding = 'ascii'
                for line in mapfile.readlines():
                    if (line.lstrip().startswith('#')):
                        if (line.startswith('# encoding: ')):
                            encoding = line[12:].rstrip()
                            logger.debug("Detected encoding: %s" % encoding)
                        continue
                    try:
                        (prompt, phrase) = line.rstrip().split("|", 1)
			k = abspath(join(basedir, prompt))
			if (not required_files.has_key(k)):
			    print("%s : %s" % (k, map_fname))
		    except:
			pass

    def doVerifyMappings(self):
        for dir in self.prompt_path:
            self._doVerifyMappings(os.path.join(dir, self.__lang))

    def _doVerifyMappings(self, basedir):
	g711_convertable_exts = [ 'wav', 'sln', 'gsm', 'au' ]
        for map_fname in os.listdir(basedir):
            if (map_fname.startswith("prompt_map") and map_fname.endswith(".txt")):
		missing_g711 = {}
		missing_other = {}
                print("Processing prompt map %s" % abspath(join(basedir, map_fname)))
                mapfile = file(join(basedir, map_fname), "r")
                encoding = 'ascii'
                for line in mapfile.readlines():
                    if (line.lstrip().startswith('#')):
                        if (line.startswith('# encoding: ')):
                            encoding = line[12:].rstrip()
                            logger.debug("Detected encoding: %s" % encoding)
                        continue
                    try:
                        (prompt, phrase) = line.rstrip().split("|", 1)
			#
			# Find G711 compatible file format
			#
			count = 0
			for ext in g711_convertable_exts:
			    f = join(basedir, prompt) + "." + ext
			    count += os.access(f, os.F_OK)
			if (count == 0):
			    missing_g711[prompt] = 1

			#
			# Find nonconvertable to G711 file formats
			#
                        for ext in self.g711_nonconverable_exts:
                            if (not missing_other.has_key(ext)):
                                missing_other[ext] = {}
                            f = join(basedir, prompt) + "." + ext
                            if (os.access(f, os.F_OK) == 0):
                                missing_other[ext][prompt] = 1
                    except:
                        pass
		no_problem = True
		p_g711 = missing_g711.keys()
		p_g711.sort()
		if (len(p_g711) > 0):
		    no_problem = False
		    print """
Missing G711 compatible prompts:
"""
		    for f in p_g711:
			print " " + abspath(join(basedir, f))
                other_names = {}
                found_names = 0
                for ext in missing_other.keys():
                    p = missing_other[ext].keys()
                    p.sort()
                    other_names[ext] = p
                    found_names += len(p)
		if (found_names > 0):
		    no_problem = False
                    for ext in self.g711_nonconverable_exts:
                        print """
Missing %s prompts:
""" % ext.upper()
                        for f in other_names[ext]:
                            print " " + abspath(join(basedir, f + "." + ext))
		if (no_problem):
		    print ""
		    print "No problems found"
		print "-" * 70


    def writeHeader(self, out):
        out.write("""<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
</HEAD>
<BODY>
""")

if (__name__ == '__main__'):
#    logging.basicConfig(level=logging.DEBUG)
    vapp.logger = logger
    c = Checker(sys.argv)
