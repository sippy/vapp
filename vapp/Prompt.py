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

import os
import tempfile

__all__ = [ "Prompt", "PROMPT_UNV", "PROMPT_BUSY", "PROMPT_NAME" ]

PROMPT_UNV = 0
PROMPT_BUSY = 1
PROMPT_NAME = 2

class Prompt:
    def __init__(self):
        self.__files = []
	self.__basename = tempfile.mktemp(dir = self.options().tmpDir())

    def addAudio(self, data, ext):
        fname = ("%s%s" % (self.__basename, ext))
        f = file(fname, "w")
        f.write(data)
        f.close()
        self.__files.append(fname)

    def basename(self):
        return self.__basename

    def __del__(self):
        self.clear()

    def clear(self):
        for f in self.__files:
            try:
                os.unlink(f)
            except:
                pass
        self.__files = []

    def resetBasename(self, name):
        self.clear()
        self.__basename = name

    def addFile(self, fname):
        self.__files.append(fname)
