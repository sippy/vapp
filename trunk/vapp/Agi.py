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
AGI and OGI protocol implementation.

AgiHandler is an abstract class. The user of this class must inherit 
the AgiHandler and implement the runSession() method.

Example:

    import vapp

    class MyAgiHandler(vapp.AgiHandler):
	def runSession(self):
	    do something useful

    class AgiServer(ThreadingTCPServer):
	def __init__(self, handler):
	    self.allow_reuse_address = True
	    ThreadingTCPServer.__init__(self, ("127.0.0.1", 4573), handler)

    #
    # Optional logger can be specified. This can be log4py.Logger instance 
    # or something similar.
    #
    vapp.logger = logger_instance 

    server = AgiServer(MyAgiHandler)
    server.serve_forever()

"""

import sys
import traceback
import re
from SocketServer import StreamRequestHandler
import vapp

__all__ = ["AgiKeyStroke", "AgiError", "AgiHandler", "AgiLongKeyStroke"]

long_event_interdigit_delay = 600

class AgiKeyStroke(Exception):
    """ An exception representing a single keypress event.  """
    __keycode = None
    __key = ""

    def __init__(self, keycode):
	""" Constructor. Keycode can be either int or single character. """
        if (type(keycode) == type(str())):
            self.__keycode = ord(keycode)
            self.__key = keycode
        else:
            self.__keycode = keycode
            if (keycode >= 0 and keycode < 256):
                self.__key = chr(keycode)

    def keyCode(self):
	""" ASCII representation of the keystroke. """
        return self.__keycode

    def key(self):
	""" String representation of the keystroke. """
        return self.__key

class AgiError(Exception):
    """ 
    An exception representing an error condition. It is usually raised when 
    hangup occurs but not limited to hangup event only. All methods of 
    AgiHandler class raise this exception upon error.
    """

class AgiLongKeyStroke(Exception):
    """ Class idicating that a key sequence detected.  """
    def __init__(self, seq):
	""" Constructor. The seq is the detected key sequence. """
	self.__seq = seq

    def str(self):
	""" The detected key sequence. """
	return self.__seq

class AgiHandler(StreamRequestHandler, object):
    """ The AGI session runner class.  """
    network = ""
    request = ""
    channel = ""
    language = ""
    _type = ""
    uniqueid = ""
    callerid = ""
    calleridname = ""
    callingpres = ""
    callingani2 = ""
    callington = ""
    callingtns = ""
    __dnid = ""
    rdnis = ""
    context = ""
    extension = ""
    priority = ""
    enhanced = ""
    accountcode = ""
    network_script = ""

    __lastresponse = None

    def __get_dnid(self):
        # The dnid has larger buffer than extension so one may want use
        # this field as extension. However dnid can be unset in some cases.
        # So use this hack to ensure the dnid is always defined.
        if self.__dnid == 'unknown':
            return self.extension
        return self.__dnid

    def __set_dnid(self, val):
        self.__dnid = val

    dnid = property(__get_dnid, __set_dnid)

    def handle(self):
	""" The main loop of AGI session.   """
        while True:
            line = self.rfile.readline()
            line = line.rstrip()
            if (line == ""):
                break
            try:
                if (re.search("^[ao]gi_network:", line)):
                    self.network = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_request:", line)):
                    self.request = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_channel:", line)):
                    self.channel = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_language:", line)):
                    self.language = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_type:", line)):
                    self._type = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_uniqueid:", line)):
                    self.uniqueid = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_callerid:", line)):
                    self.callerid = line.split(' ', 1)[1]
                    self.raw_callerid = self.callerid
		    m = re.search("<(.+)>", self.callerid)
		    if (m):
                        self.callerid = m.groups()[0]
                elif (re.search("^[ao]gi_calleridname:", line)):
                    self.calleridname = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_callingpres:", line)):
                    self.callingpres = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_callingani2:", line)):
                    self.callingani2 = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_callington:", line)):
                    self.callington = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_callingtns:", line)):
                    self.callingtns = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_dnid:", line)):
                    self.__dnid = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_rdnis:", line)):
                    self.rdnis = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_context:", line)):
                    self.context = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_extension:", line)):
                    self.extension = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_priority:", line)):
                    self.priority = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_enhanced:", line)):
                    self.enhanced = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_accountcode:", line)):
                    self.accountcode = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_network_script:", line)):
                    self.network_script = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_version:", line)):
                    self.agi_version = line.split(' ', 1)[1]
                elif (re.search("^[ao]gi_threadid:", line)):
                    self.agi_threadid = line.split(' ', 1)[1]
		elif (vapp.logger != None):
                    vapp.logger.warn("Unknown AGI header: '" + line + "'")
            except IndexError:
                pass
	try:
	    self.runSession()
	except AgiError:
	    pass
	except:
	    if (vapp.logger != None):
		for msg in traceback.format_exception(*sys.exc_info()):
		    vapp.logger.error(msg)

    def runSession(self):
        raise NotImplementedError()

    def dumpVars(self):
	""" 
	Returns the variables sent by asterisk during AGI session startup 
	"""
        return "network_script = " + self.network_script + "\n" + \
            "network = " + self.network + "\n" + \
            "request = " + self.request + "\n" + \
            "channel = " + self.channel + "\n" + \
            "language = " + self.language + "\n" + \
            "type = " + self._type + "\n" + \
            "uniqueid = " + self.uniqueid + "\n" + \
            "callerid = " + self.callerid + "\n" + \
            "calleridname = " + self.calleridname + "\n" + \
            "callingpres = " + self.callingpres + "\n" + \
            "callingani2 = " + self.callingani2 + "\n" + \
            "callington = " + self.callington + "\n" + \
            "callingtns = " + self.callingtns + "\n" + \
            "dnid = " + self.dnid + "\n" + \
            "rdnis = " + self.rdnis + "\n" + \
            "context = " + self.context + "\n" + \
            "extension = " + self.extension + "\n" + \
            "priority = " + self.priority + "\n" + \
            "enhanced = " + self.enhanced + "\n" + \
            "accountcode = " + self.accountcode

    def __execute(self, command, need_string = False):
	retval = -1
        try:
            self.__execcommand(command);
            res = self.__readresponse();
            retval = self.__checkresult(res, need_string);
        except:
	    pass
	if (retval == -1):
	    raise AgiError()
	return retval

    def __execcommand(self, command):
	if (command == None):
            return -1
	self.wfile.write(command + "\n")

    def __readresponse(self):
        response = self.rfile.readline()
        if (response == ""):
            return '200 result=-1 (noresponse)'
        return response.rstrip()

    def __checkresult(self, response, need_string):
	if (response == None):
            return -1
	result = -1
	self.__lastresponse = response
        if (re.search("^200", response)):
            m = re.search("result=(-?[\\d*#]+)", response)
            if (m):
                result = str(m.groups()[0])
                if (result.startswith('-') or not need_string):
                    result = int(result)
            else:
                m = re.search("result=\\s*(\\(timeout\\))?$", response)
                if (m):
                    result = ""
	return result

    def getVariable(self, variable):
	""" AGI 'GET VARIABLE' command wrapper. """
	result = None
	retval = self.__execute("GET VARIABLE " + variable)
	if (retval and self.__lastresponse != None):
		tempresult = self.__lastresponse
		m = re.search("\((.*)\)", tempresult)
                if (m):
			result = m.groups()[0]
	return result

    def getFullVariable(self, variable):
	""" AGI 'GET FULL VARIABLE' command wrapper. """
	result = None
	if (self.__execute("GET FULL VARIABLE " + variable)):
	    tempresult = self.__lastresponse
	    m = re.search("\((.*)\)", tempresult)
	    if (m):
		    result = m.groups()[0]
	return result

    def setVariable(self, variable, value):
	""" AGI 'SET VARIABLE' command wrapper. """
	return self.__execute("SET VARIABLE %s \"%s\"" % (variable, value))

    def streamFile(self, filename, escape = "*#0123456789", sample_offset = ""):
	""" AGI 'STREAM FILE' command wrapper. """
	if (escape == None or escape == ""):
	    escape = "n"
        retval = self.__execute("STREAM FILE " + filename + " " + escape + " " + sample_offset)
        return retval

    def streamFileEx(self, filename, escape = "*#0123456789", sample_offset = "", long_escapes = None):
	""" 
	Same as streamFile() but raises AgiKeyStroke instead of returning 
	key code. 
	
	This method is able to detect key sequences. The long_escapes 
	parameters should contain the list() of sequences to detect.
	"""
	if (long_escapes != None):
	    long_escape_listener = self.LongEscapeListener(long_escapes)
	    escape = long_escape_listener.prepareEscapeString(escape)

        retval = self.streamFile(filename, escape, sample_offset)
        if (retval != 0):
	    if (long_escapes == None):
		raise AgiKeyStroke(retval)
	    else:
		long_escape_listener.complete(self, AgiKeyStroke(retval))

    def getData(self, file, timeout_msec = "", max_digits = ""):
	""" AGI 'GET DATA' command wrapper. """
        return self.__execute("GET DATA " + str(file) + " " + str(timeout_msec) + " " + str(max_digits), need_string = True)

    def hangup(self, channel = ""):
	""" AGI 'HANGUP' command wrapper. """
        return self.__execute("HANGUP " + channel)

    def wait(self, seconds):
	""" AGI 'WAIT' command wrapper. """
        return self.execApp("WAIT", seconds)

    def execApp(self, app, options = ""):
	""" AGI 'EXEC' command wrapper. """
	try:
	    self.__execute("EXEC " + app + " " + str(options))
	except AgiError:
	    pass

    def sayNumber(self, number, escape = "*#0123456789"):
	""" AGI 'SAY NUMBER' command wrapper. """
        retval = self.__execute("SAY NUMBER " + str(number) + " " + escape)
        return retval

    def sayNumberEx(self, number, escape = "*#0123456789"):
	""" 
	Same as sayNumber() but raises AgiKeyStroke instead of returning 
	key code
	"""
        retval = self.sayNumber(number, escape)
        if (retval != 0):
            raise AgiKeyStroke(retval)

    def getOption(self, filename, escape = "*#0123456789", timeout_msec = ""):
	""" AGI 'GET OPTION' command wrapper. """
        retval = self.__execute("GET OPTION " + filename + " " + str(escape) + " " + str(timeout_msec))
        return retval

    def waitForDigit(self, timeout_msec):
	""" AGI 'WAIT FOR DIGIT' command wrapper. """
        retval = self.__execute("WAIT FOR DIGIT " + str(timeout_msec))
        return retval

    def waitForDigitEx(self, timeout_msec):
	""" 
	Same as waitForDigit() but raises AgiKeyStroke instead of returning 
	key code
	"""
        retval = self.waitForDigit(timeout_msec)
        if (retval != 0):
            raise AgiKeyStroke(retval)

    def sayDatetime(self, unixtime, escape = "*#0123456789", _format = "", tz = ""):
	""" AGI 'SAY DATETIME' command wrapper. """
        if (_format != ""):
            _format = '"' + _format + '"'
        retval = self.__execute("SAY DATETIME " + str(unixtime) + " " + str(escape) + " " + _format + " " + tz)
        return retval

    def sayDatetimeEx(self, unixtime, escape = "*#0123456789", _format = "", tz = ""):
	""" 
	Same as sayDatetime() but raises AgiKeyStroke instead of returning 
	key code
	"""
        retval = self.sayDatetime(unixtime, escape, _format, tz)
        if (retval != 0):
            raise AgiKeyStroke(retval)

    def sayTime(self, unixtime, escape = "*#0123456789"):
	""" AGI 'SAY TIME' command wrapper. """
        retval = self.__execute("SAY TIME " + str(unixtime) + " " + str(escape))
        return retval

    def sayTimeEx(self, unixtime, escape = "*#0123456789"):
	""" 
	Same as sayTime() but raises AgiKeyStroke instead of returning 
	key code
	"""
        retval = self.sayTime(unixtime, escape)
        if (retval != 0):
            raise AgiKeyStroke(retval)

    def recordFile(self, filename, _format, escape, timeout_msec, offset = None, beep = False, silence_sec = None):
	""" AGI 'RECORD FILE' command wrapper. """
        # strip extension from filename if it exists
        cmd = "RECORD FILE \"" + filename + "\" " + _format + " " + str(escape) + " " + str(timeout_msec)
        if (offset != None):
            cmd = cmd + " " + str(offset)
        if (beep):
            cmd = cmd + " BEEP"
        if (silence_sec != None):
            cmd = cmd + " s=" + str(silence_sec)
        retval = self.__execute(cmd)
        return retval

    def recordFileEx(self, filename, _format, escape, timeout_msec, offset = None, beep = False, silence_sec = None):
	""" 
	Same as recordFile() but raises AgiKeyStroke instead of returning 
	key code
	"""
        retval = self.recordFile(filename, _format, escape, timeout_msec, offset, beep, silence_sec)
        if (retval != 0):
            raise AgiKeyStroke(retval)

    def answer(self):
	""" AGI 'ANSWER' command wrapper. """
	return self.__execute("ANSWER")

    class LongEscapeListener:
	def __init__(self, escapes):
	    self.__escapes = []
	    self.__incomplete_escapes = []
	    for x in range(0, len(escapes)):
		unique = True
		for y in range(0, len(escapes)):
		    if x == y:
			continue
		    if (long_escapes[y].startswith(x)):
			unique = False
			break
		self.__escapes.append((escapes[x], unique))

	def prepareEscapeString(self, initial_escape_str):
	    #
	    # Append chars from long escapes to AGI escape string if necessary
	    #
	    for esc, unique in self.__escapes:
		for c in esc: 
		    if c not in initial_escape_str:
			initial_escape_str += c
	    self.__escape_str = initial_escape_str
	    return initial_escape_str

	def complete(self, agi_handler, key):
	    self.__pos = 0
	    self.__last_key = key
	    for code, unique in self.__escapes:
		if (code.startswith(key.key())):
		    self.__incomplete_escapes.append((code, unique))
	    while True:
		self.__on_hit(key)
		try:
		    agi_handler.waitForDigitEx(long_event_interdigit_delay)
		    key = None
		except AgiKeyStroke, k:
		    key = k
		    self.__last_key = key

	def __on_hit(self, key):
	    if (key == None):
		for code, unique in self.__incomplete_escapes:
		    if (len(code) == self.__pos):
			raise AgiLongKeyStroke(code)
		raise self.__last_key

	    hit = False
	    tmp_escapes = []

	    for code, unique in self.__incomplete_escapes:
		if (len(code) == self.__pos):
		    continue
		if (code[self.__pos] == key.key()):
		    if (len(code) == self.__pos + 1 and unique):
			raise AgiLongKeyStroke(code)
		    hit = True
		    tmp_escapes.append((code, unique))
	    self.__pos += 1
	    
	    if not hit:
		for code, unique in self.__incomplete_escapes:
		    if (len(code) == self.__pos and not unique):
			raise AgiLongKeyStroke(code)
		raise self.__last_key

	    if (len(tmp_escapes) == 0):
		raise self.__last_key

	    self.__incomplete_escapes = tmp_escapes
