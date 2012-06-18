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

"""
Base class for plugins to be managed by PluginHandler.
"""

__all__ = [ "BasePlugin" ]

class BasePlugin:
    """
    Abstract base class for IVR plugins.

    Most methods are wrappers for PluginHandler, BaseIvrHandler and 
    AgiHandler methods.

    Real plugin must be the python module with arbitrary name and
    must contain class with fixed name 'Plugin'. The Plugin class
    must inherit the BasePlugin and implement at least the 
    following methods:

	parseNetworkScript()
	run()

    The parseNetworkScript() must return boolean value. True means that
    the plugin wishes to handle current call.
    
    You can also override the answerSession() method to do nothing if 
    your application wants to use the early media mode.
    """
    def __init__(self, owner):
	""" Constructor. 'owner' is PluginHandler instance. """
	self.__owner = owner

    def owner(self):
	""" The PluginHandler instance owning this plugin instance. """
	return self.__owner

    def answerSession(self):
	self.answer()

    def _tts(self, str):
	return self.locale().gettext(str)

    def _ntts(self, text_singular, text_plural, num):
	return self.locale().ngettext(text_singular, text_plural, num)

    # logging methods
    def logger(self):
	return self.__owner.logger()

    def debug(self, msg):
	self.__owner.debug(msg)

    def info(self, msg):
	self.__owner.info(msg)

    def error(self, msg):
	self.__owner.error(msg)

    def warn(self, msg):
	self.__owner.warn(msg)

    # AgiHandler wrappers
    def network_script(self):
	return self.__owner.network_script

    def answer(self):
	return self.__owner.answer()

    def setVariable(self, var, value):
	return self.__owner.setVariable(var, value)

    def getVariable(self, var):
	return self.__owner.getVariable(var)

    def getFullVariable(self, var):
	return self.__owner.getVariable(var)

    def execApp(self, app, options = ""):
	self.__owner.execApp(app, options)

    def extension(self):
	return self.__owner.extension

    def setExtension(self, ext):
	""" Replace AgiHandler.extension with custom value """
	self.__owner.extension = ext

    def dnid(self):
	return self.__owner.dnid

    def rawCallerid(self):
	return self.__owner.raw_callerid

    def callerid(self):
	return self.__owner.callerid

    def channel(self):
	return self.__owner.channel

    def execMenu(self, menu, start = None):
	return self.__owner.execMenu(menu, start)

    def waitForDigitEx(self, timeout_msec):
	self.__owner.waitForDigitEx(timeout_msec)

    def hangup(self):
	return self.__owner.hangup()

    def streamFileEx(self, filename, escape = "*#0123456789", sample_offset = ""):
	self.__owner.streamFileEx(filename, escape, sample_offset)

    def streamFile(self, filename, escape = "", sample_offset = ""):
	return self.__owner.streamFileEx(filename, escape, sample_offset)

    def getData(self, file, timeout_msec = "", max_digits = ""):
	return self.__owner.getData(file, timeout_msec, max_digits)

    def recordFileEx(self, filename, format, escape, timeout_msec, offset = None, beep = False, silence_sec = None):
	if (beep):
	    self.streamFileEx(self.locale().beepFile(), escape)
	self.__owner.recordFileEx(filename, format, escape, timeout_msec, offset, False, silence_sec)

    def sayTimeEx(self, time):
	self.__owner.sayTimeEx(time)

    def wait(self, timeout):
	self.__owner.wait(timeout)

    def options(self):
        return self.__owner.options()

    #
    # TTS
    #
    def readString(self, prompt, max_len, timeout_msec = None):
	if (timeout_msec == None):
	    timeout_msec = self.options().defaultPromptTimeoutMsec()
	return self.__owner.readString(prompt, max_len, timeout_msec)

    def sayEx(self, text, args = [], kw = {}, escape="0123456789*#", long_escapes=None):
	self.__owner.sayEx(text, args, kw, escape, long_escapes)

    def say(self, text, args = [], kw = {}, escape = "", long_escapes=None):
        self.__owner.sayEx(text, args, kw, escape, long_escapes)

    def textSynth(self):
	return self.__owner.textSynth()

    def speechSynth(self):
	return self.__owner.speechSynth()

    def readLine(self, prompt, max_len, timeout_msec, editing_enabled = True):
        return self.__owner.readLine(prompt, max_len, timeout_msec, editing_enabled)

    def setLocale(self, locale):
	self.__owner.setLocale(locale)

    def locale(self):
	return self.__owner.locale()

    #
    # Abstract methods
    #
    def findUser(self, user):
        raise NotImplementedError()

    def format(self):
        raise NotImplementedError()

    def createStorage(self):
        raise NotImplementedError()
