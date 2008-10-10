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

import codecs
from threading import Lock

log_lock = Lock()

class PromptException(Exception):
    def __init__(self, *args):
	Exception.__init__(self, *args)
	self.__msg = None
	if (len(args) > 0):
	    self.__msg = args[0]

    def dump(self):
	if (self.__msg != None):
	    log_lock.acquire()
	    try:
		out = codecs.open(self.dumpFileName(), "a", 'utf-8')
		out.write(self.__msg)
		out.write("\n")
		out.close()
	    except:
		pass
	    log_lock.release()

    def dumpFileName(self):
	return "/tmp/vapp_bad_phrases.trace"
