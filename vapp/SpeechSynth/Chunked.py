#!/usr/local/bin/python
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

import re
import os
from PromptException import PromptException
import vapp

class Chunked:
    def __init__(self, lang, basedirs = None):
        if (basedirs == None):
            basedirs = vapp.default_prompt_dirs()
	self._map = dict()
        for basedir in basedirs:
            self.init(os.path.abspath(basedir), lang, self._map)

    def init(self, basedir, lang, pmap):
	if (not basedir.endswith("/")):
	    basedir += "/"
	basedir += lang + "/"
	for map_fname in os.listdir(basedir):
	    if (map_fname.startswith("prompt_map") and map_fname.endswith(".txt")):
		vapp.logger.debug("Loading prompt map %s" % (basedir + map_fname))
		mapfile = file(basedir + map_fname, "r")
		encoding = 'ascii'
		for line in mapfile.readlines():
		    if (line.lstrip().startswith('#')):
			if (line.startswith('# encoding: ')):
			    encoding = line[12:].rstrip()
			    vapp.logger.debug("Detected encoding: %s" % encoding)
			continue
		    try:
			(prompt, phrase) = line.rstrip().split("|", 1)
			phrase = unicode(phrase, encoding)
			pmap[phrase.lower()] = (prompt, basedir)
			#
			# Hash also the phrase without puctuation at the end
			#
			res = re.findall(r"^(.*)([.?!]+$)", phrase)
			if (res):
			    s = res[0][0].rstrip().lower()
			    pmap[res[0][0].rstrip().lower()] = (prompt, basedir)
		    except:
			pass

    def promptFileSequence(self, msg, prepend_basedir = False):
	return self._promptFileSequence(msg, prepend_basedir, (self._map, ))

    def _promptFileSequence(self, msg, prepend_basedir, pmaps):
	dbg_dump = "INIT: message '%s'\n" % msg
	retval = list()
        msg = msg.strip()
	phrase = msg.lower()
	offset = 0
	while True:
	    found = False
	    #dbg_dump += "TRY: '%s'\n" % phrase
	    for pmap in pmaps:
		if phrase in pmap: # match found
		    (prompt, basedir) = pmap[phrase]
		    if (prepend_basedir and not prompt.startswith("/")):
			prompt = basedir + prompt
		    retval.append(prompt)
		    dbg_dump += "MATCH: '%s', prompt %s\n" % (phrase, prompt)
		    found = True
		    break
	    if (found):
		offset += len(phrase)
		while (offset < len(msg) and re.findall(unicode(r'^[\s　.!?]', 'utf-8'), msg[offset])):
		    offset += 1
		if (offset >= len(msg)):
		    break
		phrase = msg[offset:].lower() # skip to the next part
	    else:
		# if only punctuation left then the search has been finished
		if (re.findall(r"^[.?!]+$", phrase)):
		    break
		# try to skip punctuation at the end of the phrase
		res = re.findall(r"^(.*)([.?!]+$)", phrase)
		if (res):
		    phrase = res[0][0].rstrip()
		    continue
		# try to shorten the phrase by one word
		res = re.findall(unicode(r"^(.*)([\s　,]+.*$)", 'utf-8'), phrase)
		if (res):
		    phrase = res[0][0].rstrip()
		    continue
		raise PromptException("Cannot find any match for the phrase '%s'\nMapping traceback:\n%s" % (msg[offset:], dbg_dump))
	return retval
