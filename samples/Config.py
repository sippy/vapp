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


default_locale = "en"

class Config:
    def defaultSystemLocale(self):
        return default_locale

    def maxPasswordLen(self):
        return 5

    def defaultPromptTimeoutMsec(self):
        return 10000

    def tmpDir(self):
        return "/var/tmp"

    def maxMessageTimeMsec(self):
        return 200000

    def maxSilenceTimeSec(self):
        return 3

    def skipAfterCmd(self):
        return False

    def maxGreetingTimeMsec(self):
        return 60000

    def callbackApp(self):
        return "vm"

    def callbackRingTime(self):
        return 3

    def callbackGuardInterval(self):
        return 5

    def callbackTimeoutSec(self):
        return 10

    def callbackProxy(self):
        return "192.168.0.101"

    def callbackCli(self):
        return "vm"

    def managerUser(self):
        return 'ivrd'

    def managerPassword(self):
        return 'secret'
