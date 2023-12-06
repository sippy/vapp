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

import time
import traceback
import sys
from threading import Thread, Lock
import vapp
import Commons

callbacks_lock = Lock()
callbacks = []

class CallbackReq(object):
    def __init__(self, cld, app):
        self.__cld = cld
        self.__app = app
        self.__created = time.time()

    def __get_created(self):
        return self.__created

    created = property(__get_created)

    def call(self):
        cli = "%(cli)s<%(cli)s>" % { 'cli' : Commons.config.callbackCli() }
        Commons.manager.originate(
                self.__cld,
                Commons.config.callbackTimeoutSec() * 1000,
                Commons.config.callbackProxy(),
                cli,
                "AGI",
                "agi://127.0.0.1/callback/%s" % self.__cld)


class Daemon(Thread):
    def run(self):
        global callbacks
        vapp.logger.debug("Callback monitor started")
        while True:
            try:
                callbacks_lock.acquire()
                now = time.time()
                guard_interval = Commons.config.callbackGuardInterval()
                tmp = []
                for r in callbacks:
                    if now - r.created < guard_interval:
                        tmp.append(r)
                    else:
                        r.call()
                callbacks = tmp
                callbacks_lock.release()
            except:
                for msg in traceback.format_exception(*sys.exc_info()):
                    vapp.logger.error(msg.rstrip())
            time.sleep(5)

class Plugin(vapp.BasePlugin):
    def parseNetworkScript(self):
        if (self.extension() == 'callback'):
            return True
        return False

    def run(self):
        global callbacks
        self.debug("Callback plugin started")
        if (self.extension() == 'callback'):
            self.debug("Scheduling callback request to %s" % self.callerid())
            self.execApp("Ringing")
            self.wait(self.options().callbackRingTime())
            callbacks_lock.acquire()
            callbacks.append(CallbackReq(self.callerid(), self.options().callbackApp()))
            callbacks_lock.release()
        self.debug("Callback plugin ended")
