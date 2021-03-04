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
AGI handler able to manage IVR plugins.
"""
from threading import Thread
import sys
import traceback
import pkgutil
import vapp
from BaseIvrHandler import *
from TextSynth import *
import SpeechSynth.Chunked
from SpeechSynth.PromptException import PromptException

_plugins = dict()
_daemons = dict()

def loadPlugins(plugin_packages, exclude_modules = []):
    """
    This procedure must be called before using the PluginHandler class.
    It searches and loads all available IVR plugins from packages specified
    in the plugin_packages parameter (array of strings). The exclude_modules
    parameter can contain a list of module names that must not be loaded.

    Note that the vapp.logger must be set before calling this function.
    """
    _logger = vapp.logger
    if (_logger == None):
	raise Exception("Cannot run without logger instance. Please place a logger instance to vapp.logger before running this function.")
    for pkg_name in plugin_packages:
        plugins_found = 0
        try:
            pkg = __import__(pkg_name, fromlist = [''])
            for importer, modname, ispkg in pkgutil.iter_modules(pkg.__path__):
                if ispkg:
                    continue
                full_name = "%s.%s" % (pkg_name, modname)
                if ((full_name in exclude_modules) or (modname in exclude_modules)):
                    _logger.debug("The %s module is disabled by administrator" % full_name)
                    continue
                try:
                    mod = __import__(full_name, fromlist = [''])
                except:
                    for msg in traceback.format_exception(*sys.exc_info()):
                        _logger.error(msg)
                    sys.exit(1)

                try:
                    #
                    # import IVR plugins
                    #
                    mod.Plugin
                    _plugins[full_name] = mod
                    _logger.debug("Plugin %s imported successfully." % modname)
                except AttributeError:
                    pass
                try:
                    #
                    # import Daemon plugins
                    #
                    daemon = mod.Daemon()
                    _daemons[full_name] = daemon
                    _logger.debug("Daemon %s imported successfully." % modname)
                    if (isinstance(daemon, Thread)):
                        daemon.setDaemon(True)
                        daemon.start()
                except AttributeError:
                    pass
                plugins_found += 1
        except ImportError:
            pass
        if (plugins_found == 0):
            _logger.debug("No plugins found in %s package" % pkg_name)

def pluginInstance(mod_name):
    """
    Look for non-IVR plugin running as a standalone thread.

    For example suppose that there is a plugin misc/CallbackMonitor.py and
    it inherits the threading.Thread. In this case the call:

	PluginHandler.pluginInstance('CallbackMonitor')

    will return the reference to this plugin instance.
    """
    for name in _daemons.keys():
        if (name.endswith(mod_name)):
            return _daemons[name]
    return None

class PluginHandler(BaseIvrHandler):
    """
    Class that manages a set of IVR plugins (see BasePlugin).
    """
    # static members
    __textSynthCache = dict()
    __speechSynthCache = dict()
    __localeCache = dict()

    # normal members
    __session_handler = None
    __session_handler_name = None
    __locale = None

    def parseNetworkScript(self):
	"""
	The purpose of this method is to determine which plugin wishes
	to handle the call. This method iterates all loaded IVR plugins
	and runs the parseNetworkScript() method of each plugin.
	First plugin that returned True value becomes the session
	controller. Called by BaseIvrHandler.
	"""
        self.setLocale(self.options().defaultSystemLocale())
	if (len(_plugins.keys()) == 0):
	    self.error("No plugins found! Make sure you've called PluginHandler.loadPlugins() before using the PluginHandler class.")
	for pname in _plugins.keys():
	    self.debug("Trying the %s plugin." % pname)
	    plugin = _plugins[pname].Plugin(self)
	    if (plugin.parseNetworkScript()):
		self.debug("The %s plugin is responsible for the call." % pname)
		self.__session_handler = plugin
		self.__session_handler_name = pname
		break

    def plugin(self):
	""" Returns the current session controller. """
	return self.__session_handler

    def answerSession(self):
	"""
	Wrapper method. It calls the answerSession() method of
	the session controller plugin. Called by BaseIvrHandler.
	"""
	if (self.__session_handler != None):
	    self.__session_handler.answerSession()

    def handleCall(self):
	"""
	Wrapper method. It calls the run() method of the session
	controller plugin. Called by BaseIvrHandler.
	"""
	if (self.__session_handler == None):
	    self.debug("None of the plugins accepted the call. Aborting the call...")
	    return
	try:
	    self.__session_handler.run()
	except vapp.AgiError:
	    self.debug("User hung up")
	    self.hangup()
        except PromptException as e:
            e.dump()
            self.error("BAD PROMPT. Trace dumped into %s" % e.dumpFileName())
	except:
	    for msg in traceback.format_exception(*sys.exc_info()):
		self.error(msg)

    def cleanup(self):
	"""
	Called by BaseIvrHandler.
	"""
	self.__session_handler = None

    def logger(self):
	"""
	Returns a logger instance. It is the vapp.logger by default but
	this method can be overriden to make more advanced per session
	logging such as to prepend the SIP Call-ID to each log message
	or something similar.
	"""
	return vapp.logger

    def debug(self, msg):
	""" Shortcut for self.logger().debug(msg) """
	self.logger().debug(msg)

    def info(self, msg):
	""" Shortcut for self.logger().info(msg) """
	self.logger().info(msg)

    def error(self, msg):
	""" Shortcut for self.logger().error(msg) """
	self.logger().error(msg)

    def warn(self, msg):
	""" Shortcut for self.logger().warn(msg) """
	self.logger().warn(msg)

    #
    # TTS
    #
    def speechSynth(self):
	locale_name = self.locale().name()
	if locale_name not in self.__speechSynthCache:
            self.__speechSynthCache.setdefault(locale_name, self.createSpeechSynth(locale_name))
	return self.__speechSynthCache[locale_name]

    def createSpeechSynth(self, locale_name):
        return SpeechSynth.Chunked.Chunked(locale_name)

    def textSynth(self):
	locale_name = self.locale().name()
	if locale_name not in self.__textSynthCache:
	    self.__textSynthCache.setdefault(locale_name, self.createTextSynth(self.locale()))
	return self.__textSynthCache[locale_name]

    def createTextSynth(self, locale):
        return TextSynth(locale)

    def setLocale(self, locale_name):
        if locale_name not in self.__localeCache:
            self.__localeCache.setdefault(locale_name, self.createLocale(locale_name))
	self.__locale = self.__localeCache[locale_name]

    def createLocale(self, name):
        return vapp.Locale(name)

    def locale(self):
	return self.__locale
