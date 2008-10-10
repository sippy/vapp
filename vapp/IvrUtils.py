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
Utility functions for Voicemail IVR application.
"""
import time
import random
import md5

__all__ = [ "ivrAuthenticate", "AuthenticationError", "SipDialer" ]

def generateSipCallId(host = '127.0.0.1'):
    if (':' in host):
        host, port = host.split(':')
    return md5.md5(str((random.random() * 1000000000L) + time.time())).hexdigest() + '@' + host

class AuthenticationError(Exception):
    pass

def ivrAuthenticate(agi_handler):
    """
    Interactively asks the PIN code. Raises the AuthenticationError
    if wrong PIN code entered for too many times.
    """
    valid = False
    attempts = 0

    if (agi_handler.user == None):
        raise AuthenticationError("User not found.")
    elif (not agi_handler.askPin()):
        # we have found user and have no need in checking password
        return
    prompt = agi_handler._tts("Please enter your PIN code.")
    while (not valid):
        if (agi_handler.user.hasPassword()):
            password = agi_handler.readString(prompt, agi_handler.options().maxPasswordLen())
            if (password != -1 and agi_handler.user.checkPassword(password)):
                valid = 1
            prompt = agi_handler._tts("Wrong PIN code. Please enter your PIN code.")
        else:
            valid = 1
        if (not valid):
            attempts += 1
            if (attempts >= agi_handler.options().maxLoginRetries()):
                raise AuthenticationError("Login incorrect")

class SipDialer:
    """
    Class to automate the calls using Dial() Asterisk application
    and SIP channel.
    """
    __authname = ""
    __md5secret = ""
    __call_id = None
    __idx = 10
    __max_duration = None
    __misc_vars_set = False
    __sip_proxy = None

    class _SipHeader:
	def __init__(self, hdr_name, val, idx):
	    self.__name = hdr_name
	    self.__val = val
	    self.__idx = idx
	    self.__changed = True

	def update(self, val):
	    if (self.__val == val):
		return 
	    self.__val = val
	    self.__changed = True

	def apply(self, agi_handler):
	    if (not self.__changed):
		return
	    var_name = "_SIPADDHEADER%d" % self.__idx
	    if (self.__val == None):
		agi_handler.setVariable(var_name, '')
	    else:
		agi_handler.setVariable(var_name, '%s: %s' % (self.__name, self.__val))
	    self.__changed = False

    def __init__(self):
	self.__hdr_by_name = {}

    def callId(self):
        """
        Returns the current value for Call-ID header to be used for 
        the call.
        """
	return self.__call_id

    def cli(self):
        """
        Returns the current CLI value to be used for the call.
        """
	return self.__cli

    def setAuthname(self, authname):
        """
        Allows to specify the authname to be used for the call.
        """
	self.__authname = authname

    def setCallId(self, call_id):
        """
        Allows to specify the Call-ID to be used for the call.
        """
	self.__call_id = call_id

    def setCli(self, cli):
        """
        Allows to specify the CLI to be used for the call.
        """
	self.__cli = cli

    def setMaxDuration(self, duration):
        """
        Allows to specify the maximum duration of the call in seconds.
        """
	self.__max_duration = duration

    def setSecret(self, md5secret):
        """
        Allows to specify the md5secret to be used for the call.
        """
	self.__md5secret = md5secret

    def setSipProxy(self, proxy):
        """
        Set destination SIP proxy
        """
        self.__sip_proxy = proxy

    def setHeader(self, hdr_name, value):
        """
        Allows to specify an additional SIP header for the call or
        change the value of the already added custom SIP header with
        the same name.

        If the 'value' is set to None then previously defined SIP header
        with the given name will be removed from the SIP request. 
        """
	if (self.__hdr_by_name.has_key(hdr_name)):
	    hdr = self.__hdr_by_name[hdr_name]
	    hdr.update(value)
	else:
	    hdr = self._SipHeader(hdr_name, value, self.__idx)
	    self.__hdr_by_name[hdr_name] = hdr
	    self.__idx += 1

    def dial(self, dest, agi_handler):
        """
        Place the call. Returns nothing. Use the DIALSTATUS dialplan 
        variable to find out how the call ended.
        """
        if (self.__sip_proxy == None):
            self.__sip_proxy = agi_handler.sipProxy()

	if (not self.__misc_vars_set):
	    if (self.__call_id != None):
		agi_handler.setVariable('_SIP_FORCE_CALLID', self.__call_id)
	    
	    agi_handler.setVariable('CALLERID(all)', "%s <%s>" % (self.__cli, self.__cli))
	    self.__misc_vars_set = True

        arg = "SIP/%s::%s:%s@%s||H" % (dest, self.__md5secret, self.__authname, self.__sip_proxy)

	if (self.__max_duration != None and self.__max_duration > 0):
	    arg += 'S(%d)' % self.__max_duration

	for hdr in self.__hdr_by_name.values():
	    hdr.apply(agi_handler)

	agi_handler.execApp('Dial', arg)
