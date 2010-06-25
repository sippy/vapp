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
Abstract implementation of voicemail IVR application with behavior
similar to Asterisk app_voicemail implementation.
"""
from AbstractVoicemailStorage import *
from vapp.BasePlugin import *
from vapp.Prompt import *
from vapp.Agi import *
import tempfile
import os
import re

class AbstractPlugin(BasePlugin):
    user = None
    prompt_id = None

    def parseNetworkScript(self):
        """
        Accepts the CLD that starts with 'vm' and contains the user 
        identifier. Examples of possible CLDs:

            vm-505
            vm505b
            vm-s505
            vmu505

        the b, s and u characters can be included in user identifier and
        mean 'play busy message', 'play unavailable message' and
        'do not play any prompt' before starting message recording.

        """
	arr = self.dnid().split("_")
	if (arr[0].startswith("vm") and len(arr[0]) > 2):
	    return True
	return False

    def run(self):
	self.debug("Starting message recording...")
        tmp = self.extension()
        if (tmp == None or tmp == ""):
            tmp = self.dnid()
        if (tmp == None or tmp == ""):
            # ask the target number
	    tmp = self.readString(self._tts("To leave a message please enter a mailbox number"), self.options().maxLoginLen())
        self.target = ""
        self.silent = False
        if (self.user == None and tmp != ""):
            for c in tmp[2:]:
                if (c == 's'):
                    self.silent = True
                elif (c == 'b'):
                    self.prompt_id = PROMPT_BUSY
                elif (c == 'u'):
                    self.prompt_id = PROMPT_UNV
                elif (c == '-'):
                    continue
                else:
                    self.target = self.target + c
        self.__leaveAMessage()
        self.hangup()

    def __leaveAMessage(self):
        if self.user == None:
            self.user = self.findUser(self.target)
        self.debug("Recording a voicemail message for the user %s" % self.user.username())

        if (self.user == None):
            return
        #
        # Set the own caller locale for current session if caller is our account
        #
        caller_user = self.findUser(self.callerid())
        if (caller_user != None):
            self.setLocale(caller_user.locale())
        try:
            if (self.prompt_id != None):
                promptfile = self.user.preparePrompt(self.prompt_id, self.format())
                if (promptfile == None):
                    if (self.prompt_id == PROMPT_BUSY):
                        self.sayEx(self._tts("Extension is on the phone."))
                    elif (self.prompt_id == PROMPT_UNV):
                        self.sayEx(self._tts("Extension is unavailable."))
                    self.sayEx(self._tts("Please leave your message after the tone. When done hang up or press the pound key"))
                else:
                    self.streamFileEx(promptfile)
            elif (not self.silent):
                self.sayEx(self._tts("Please leave your message after the tone. When done hang up or press the pound key"))
        except AgiKeyStroke, keystroke:
            if (keystroke.key() == '#' and self.isAutoAttendantAvailable()):
                self.autoAttendant()
            elif (keystroke.key() == '0' and self.isOperatorAvailable()):
                self.dialOperator()

        self.message_exists = False
        (self.messageFd, self.messageFilename) = tempfile.mkstemp(suffix = "." + self.format(), dir = self.options().tmpDir())
        m = re.search("(.+)\\." + self.format() + "$", self.messageFilename)
        self.messageFilenameNoExt = m.groups()[0]
	try:
	    self.execMenu({ \
		'1':self.__saveMessage, \
		'2':self.reviewMessage, \
		'3':self.recordMessage, \
		'default':self.messageDefault, \
		'quit':'t#'
	    }, '3')
	    self.say(self._tts("Good bye"))
	except AgiError:
	    pass
        os.close(self.messageFd)
        os.unlink(self.messageFilename)

    def __saveMessage(self):
        if (not self.message_exists):
            raise AgiKeyStroke('3')
        else:
            os.lseek(self.messageFd, 0, 0)
            self.user.saveMessage(self.messageFd, self.format(), self.callerid(), self.logger())
	    self.debug("New message for user %s saved successfully" % self.user.username())
            self.sayEx(self._tts("Your message has been saved."))
            raise AgiKeyStroke('t')

    def reviewMessage(self):
        self.streamFileEx(self.messageFilenameNoExt)

    def isAutoAttendantAvailable(self):
        return False

    def isOperatorAvailable(self):
        return False

    def recordMessage(self):
        self.message_exists = True
        try:
            self.recordFileEx(filename = self.messageFilenameNoExt, \
                              format = self.format(), \
                              timeout_msec = self.options().maxMessageTimeMsec(), \
                              escape = '#*', \
                              beep = True, \
                              silence_sec = self.options().maxSilenceTimeSec())
        except AgiKeyStroke, keystroke:
            if (keystroke.key() == '*' or keystroke.keyCode() == -1):
                raise
	# handle hangup
	except AgiError:
	    pass
        self.__saveMessage()

    def messageDefault(self):
        if (self.message_exists):
            self.sayEx(self._tts("Press one to accept this recording. Press two to listen to it. Press three to rerecord your message."))
        else:
            self.sayEx(self._tts("Press three to rerecord your message."))
            self.waitForDigitEx(600)
        self.sayEx(self._tts("or pound to cancel"))
        self.waitForDigitEx(6000)
