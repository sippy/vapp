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

import EN
import re

class TextSynth:
    def __init__(self, locale):
	self.__locale = locale
        self.__tts = None
        try:
            self.__tts = __import__("TextSynth." + locale.name().upper(), fromlist = [''])
        except ImportError:
            try:
                self.__tts = __import__("vapp.TextSynth." + locale.name().upper(), fromlist = [''])
            except ImportError:
                self.__tts = EN

    def say(self, str, args = [], kw = {}):
	#
	# %(ident)[FLAGS]n - number substitution
	# Where 
	#   ident - identifier to search in function args
	#   FLAGS - set of single digit flags
	# Common flags:
	#   N - say number, not digits (default)
	#   D - say digits, not number
	#   H - use ordinal form
	# For other flags please consult the appropriate language module
	#
	#
	# %(ident)[FLAGS]s - string substitution
	# Currently no flags affect the substitution
	#
	# 
	# %(ident)[FLAGS]d - duration substitution
	# Common flags:
	#   H - don't say hours
	#   M - don't say minutes
        #   S - don't say seconds
	#
	#
	# %(ident)[FLAGS]D - datetime substitution
	# Common flags:
	#   D - don't say date
	#   T - don't say time
	#   S - don't say seconds
	# For other flags please consult the appropriate language module
	# 
	res = re.findall(r'(%\([^)]*\)\[[^]]*\][nsdD]|%\([^)]*\)[nsdD]|%[nsdD]|%\[[^]]*\][nsdD])', str)
	idx = 0
	retval = str
	for p in res:
	    ident = None
	    flags = None
	    arr = re.findall(r'\(([^)]*)\)', p)
	    if (arr):
		ident = arr[0]
	    arr = re.findall(r'\[([^]]*)\]', p)
	    if (arr):
		flags = arr[0]
	    if (ident != None):
		if (not ident in kw.keys()):
		    raise Exception("No '%s' key found in function arguments" % ident)
		val = kw[ident]
	    else:
		if (idx >= len(args)):
		    raise Exception("Too few arguments to the function")
		val = args[idx]
		idx += 1
	    if (p.endswith('n')): # number substitution
		if (flags != None and 'H' in flags):
		    ordinal = True
		else:
		    ordinal = False
		if (flags != None and 'D' in flags):
		    if ('N' in flags):
			raise Exception("Both N and D flags specified")
		    repl = self.__tts.sayDigits(val, flags)
		else:
		    repl = self.__tts.sayNumber(int(val), ordinal, flags)
	    elif (p.endswith('s')): # string substitution
		repl = val
	    elif (p.endswith('d')): # duration substitution
		say_hours = True
		say_minutes = True
                say_seconds = True
		if (flags != None):
		    if ('H' in flags):
			say_hours = False
		    if ('M' in flags):
			say_minutes = False
		    if ('S' in flags):
			say_seconds = False
		repl = self.__tts.sayDuration(val, say_hours, say_minutes, say_seconds, flags)
	    elif (p.endswith("D")):
		say_date = True
		say_time = True
		say_seconds = True
		if (flags != None):
		    if ('D' in flags):
			say_date = False
		    if ('T' in flags):
			say_time = False
		    if ('S' in flags):
			say_seconds = False
		repl = self.__tts.sayDatetime(val, say_date, say_time, say_seconds, flags)
	    retval = re.sub(re.escape(p), repl, retval, 1)
	return retval

