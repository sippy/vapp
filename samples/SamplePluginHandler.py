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

import vapp
import Commons

class SamplePluginHandler(vapp.PluginHandler):
    callerid = None

    def parseNetworkScript(self):
        args = self.network_script.split('/')
        if len(args) == 2 and args[0] == 'callback':
            self.debug("This is a callback call")
            # Swap CLI and CLD so other plugins will handle
            # callback call in the same way as direct call.
            self.extension = self.callerid
            self.dnid = self.callerid
            self.callerid = args[1]
        vapp.PluginHandler.parseNetworkScript(self)
#        if (self.plugin() != None):
#            manager.registerChannel(self.plugin())

#    def cleanup(self):
#        if (self.plugin() != None):
#            manager.unregisterChannel(self.plugin())
#        cleanup(self)

    def options(self):
        return Commons.config
