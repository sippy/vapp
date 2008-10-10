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
import vapp

class Plugin(vapp.BasePlugin):
    def parseNetworkScript(self):
	if (self.extension() == "testnum"):
	    return True
	return False

    def answerSession(self):
	pass

    def run(self):
	self.debug("TestNumbers started")
	self.answer()
	key = 1
	locales = list()
	base_dir = vapp._translation_config.get('default', 'prompt_catalog_dir')
	for l in os.listdir(base_dir):
	    if (os.access(base_dir + "/" + l + "/prompt_map.txt", os.F_OK)):
		locales.append(l)
	counter = 0
	while(True):
	    try:
		key = 1
		for l in locales:
		    self.setLocale(l)
		    self.sayEx(self._tts("For English press %n"), [ key ])
		    key += 1
		self.waitForDigitEx(self.options().defaultPromptTimeoutMsec())
		if (counter > 3):
		    return
		counter += 1
	    except vapp.AgiKeyStroke, k:
		if (k.key().isdigit()):
		    i = int(k.key()) - 1
		    if (i >= 0 and i < len(locales)):
			self.setLocale(locales[i])
			break
        self.testNumbers()
	self.debug("TestNumbers ended")

    def testNumbers(self):
	while (True):
	    num = ''
	    while (True):
		try:
		    self.waitForDigitEx(10000)
		except vapp.AgiKeyStroke, k:
		    if (k.key().isdigit()):
			num += k.key()
		    else:
			break
	    self.say("%n", [int(num)])
