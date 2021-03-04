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

from .VoicemailStorage import VoicemailStorage, basePath
from vapp.Prompt import *
import os

class User:
    vm_enabled = True

    def __init__(self, username):
        self.__username = username
        self.__vm_storage = VoicemailStorage(self)
        self.__password = ""
        passwordfile = self.__vm_storage.home() + "/password.txt"
        try:
            self.__password = open(passwordfile).readline()
        except IOError:
            pass

    def username(self):
        return self.__username

    def locale(self):
        return "en"
        #return "ru"

    def hasPassword(self):
        return self.__password != ""

    def checkPassword(self, password):
        return True

    def preparePrompt(self, prompt_id):
        if (prompt_id == PROMPT_UNV):
            pfile = 'unavailable'
        elif (prompt_id == PROMPT_BUSY):
            pfile = 'busy'
        else:
            return None
        path = "%s/%s" % (self.__vm_storage.home(), pfile)
        try:
            os.stat(path + ".sln")
        except OSError:
            return None
        return path

    def savePrompt(self, prompt_id, fd, format):
        if (prompt_id == PROMPT_UNV):
            pfile = 'unavailable'
        elif (prompt_id == PROMPT_BUSY):
            pfile = 'busy'
        else:
            return
        fname = "%s/%s.%s" % (self.__vm_storage.home(), pfile, format)
        out = open(fname, "w")
        while True:
            buf = os.read(fd, 8192)
            if (buf == None or buf == ""):
                break
            out.write(buf)
        out.close()

    def saveMessage(self, fd, format, cli, logger):
        self.__vm_storage.saveMessage(fd, format, cli, logger)

    def voicemailBoxIsFull(self):
        return False

    def tz(self):
        return 'UTC'

    def setPassword(self, passwd):
        self.__password = passwd
        passwordfile = self.__vm_storage.home() + "/password.txt"
        out = open(passwordfile, "w")
        out.write(passwd)
        out.close()
