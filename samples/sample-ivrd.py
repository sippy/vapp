#!/usr/bin/env python
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
import signal
import sys
from SocketServer import ThreadingTCPServer
import vapp
import traceback
import logging
from SamplePluginHandler import SamplePluginHandler
import Commons

class SampleServer(ThreadingTCPServer):
    def __init__(self, handler):
        #
        # We assume the server to be listening on local socket only, as we want 
	# to have an easy and fast access to the recorded by Asterisk files,
        # easily pass own prompt files, etc
        #
        self.allow_reuse_address = True
        ThreadingTCPServer.__init__(self, ("127.0.0.1", 4573), handler)

def daemonize():
    old_sighup = signal.getsignal(signal.SIGHUP)
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    if (os.fork() != 0):
        os._exit(0)
    os.setsid()
    os.chdir("/")
    fd = os.open("/dev/null", os.O_RDWR, 0)
    os.dup2(fd, sys.__stdin__.fileno())
    os.dup2(fd, sys.__stdout__.fileno())
    os.dup2(fd, sys.__stderr__.fileno())
    os.close(fd)
    signal.signal(signal.SIGHUP, old_sighup)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging
    vapp.logger = logger
    #daemonize()
    try:
        Commons.startManager(logger)
	vapp.loadPlugins([ "ivr_plugins" ])

	server = SampleServer(SamplePluginHandler)
	server.serve_forever()
    except KeyboardInterrupt:
	pass
    except SystemExit:
	pass
    except:
	for msg in traceback.format_exception(*sys.exc_info()):
	    logger.error(msg)
	logger.error("Unrecoverable error. Exiting...")
	sys.exit(1)
