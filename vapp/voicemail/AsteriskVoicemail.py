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

from AbstractVoicemailStorage import *
from vapp.BasePlugin import *
from vapp.IvrUtils import *
from vapp.Agi import *
from vapp.Prompt import *
import vapp
import tempfile
import os
import re

class AbstractPlugin(BasePlugin):

    user = None
    prefix = ""
    vm_storage = None
    logged_in = False

    def parseNetworkScript(self):
	arr = self.dnid().split("_")
	if (arr[0] == "vm"):
	    return True
	return False

    def run(self):
        #
        # Parse options if any
        #
        username = ""
        try:
            (username, opts) = self.callerid().split("|", 1)
            for opt in (opts):
                if (opt == 's'):
                    self.logged_in = True
                elif (opt == 'p' and username != ""):
                    self.prefix = username
                    username = ""
        except ValueError:
            username = self.callerid()
        if self.user == None:
            self.debug("Verifying if the callerid '%s' is our account" % username)
            self.user = self.findUser(self.prefix + username)
        else:
            self.debug("The user is '%s'" % self.user.username())

        if self.user != None:
            self.setLocale(self.user.locale())
        else:
            self.setLocale(self.options().defaultSystemLocale())
        try:
	    if not self.logged_in:
		ivrAuthenticate(self)
        except AuthenticationError, e:
            self.info("Auth error: " + str(e))
            self.say(self._tts("Good bye"))
            self.hangup()
            return
        if not self.user.vm_enabled:
            self.debug("The user %s is not VM enabled" % self.user.username())
            return
        self.vm_storage = self.createStorage()
	try:
	    #
	    # Main menu
	    #
	    self.starting = True
	    self.execMenu({ \
		    '1':self.firstMessage, \
		    '2':self.changeFolder, \
		    '4':self.prevMessage, \
		    '5':self.replayMessage, \
		    '6':self.nextMessage, \
		    '7':self.toggleDeleteMessage, \
		    '9':self.saveToFolder, \
		    '0':self.changeOptions, \
		    'quit':'#t', \
                    'default':self.instructions, \
                    'intro':self.mainIntro \
	    })
	    self.say(self._tts("Good bye"))
            self.hangup()
	except AgiError:
	    pass
        self.vm_storage.finalize()

    def firstMessage(self):
        self.setCurMsg(0)
        self.browseMessages()

    def changeFolder(self):
        try:
            self.getFolder2(self._tts("Change to which folder?"), 0)
        except AgiKeyStroke, keystroke:
            if ((keystroke.keyCode() > 0) and keystroke.key().isdigit()):
                self.setFolder(int(keystroke.key()))
            self.starting = True
            self.playFolderName()

    def prevMessage(self):
        if (self.curMsg() > 0):
            self.setCurMsg(self.curMsg() - 1)
            self.playMessage()
        else:
            self.sayEx(self._tts("no more messages"))


    def replayMessage(self):
        self.browseMessages()

    def nextMessage(self):
        if (self.curMsg() < self.lastMsg()):
            self.setCurMsg(self.curMsg() + 1)
            self.playMessage()
        else:
            self.sayEx(self._tts("no more messages"))

    def toggleDeleteMessage(self):
        self.toggleDelete()
	if (self.isMsgDeleted()):
	    self.sayEx(self._tts("Message deleted."))
	else:
	    self.sayEx(self._tts("Message undeleted."))
	if (self.options().skipAfterCmd()):
	    if (self.curMsg() < self.lastMsg()):
		self.setCurMsg(self.curMsg() + 1)
	    else:
		self.sayEx(self._tts("no more messages"))

    def saveToFolder(self):
	if (self.curMsg() < 0):
	    return
        try:
            self.getFolder2(self._tts("which folder should I save the message to?"), 1)
        except AgiKeyStroke, keystroke:
            tmp_key = None
            if (keystroke.keyCode() > 0 and keystroke.key().isdigit()):
                target_folder = int(keystroke.key())
                try:
                    self.vm_storage.saveCurrentMessageToFolder(target_folder)
		    self.sayEx(self._tts("message %(num)n saved to %(folder)s"), kw = { 'num':self.curMsg() + 1, 'folder':self._tts(sayFolderNameById(target_folder)) })
                except VM_MailboxFullError:
                    self.sayEx(self._tts("Sorry but the user's mailbox can't accept more messages."))
                except AgiKeyStroke, keystroke:
                    tmp_key = keystroke
		except AgiError:
		    return
                if (self.options().skipAfterCmd()):
                    if (self.curMsg() < self.lastMsg()):
                        self.setCurMsg(self.curMsg() + 1)
                    else:
                        self.sayEx(self._tts("no more messages"))
                if (tmp_key != None):
                    raise AgiKeyStroke(tmp_key.keyCode())

    #
    # Options menu
    #
    def changeOptions(self):
        self.execMenu({ \
            '1':lambda : self.playRecordReview(PROMPT_UNV), \
            '2':lambda : self.playRecordReview(PROMPT_BUSY), \
            '3':lambda : self.playRecordReview(PROMPT_NAME), \
            '4':self.changePassword, \
            'quit':'*', \
            'default':self.optionsDefault \
        })

    def instructions(self):
        repeats = 0
        while (True):
            if (self.starting):
                if (not self.vm_storage.folderIsEmpty()):
                    self.sayEx(self._tts("Press one for %s messages"), [self._tts(self.vm_storage.sayFolderName())])
                self.sayEx(self._tts("Press two to change folders. Press zero for mailbox options."))
            else:
                if (self.curMsg() > 0):
                    self.sayEx(self._tts("Press four for the previous message."))
                self.sayEx(self._tts("Press five to repeat the current message."))
                if (self.curMsg() < self.lastMsg()):
                    self.sayEx(self._tts("Press six to play the next message."))
                if (self.isMsgDeleted()):
                    self.sayEx(self._tts("Press seven to undelete this message."))
                else:
                    self.sayEx(self._tts("Press seven to delete this message."))
                self.sayEx(self._tts("Or nine to save this message."))
            self.sayEx(self._tts("Press star for help or a pound to exit."))
            self.waitForDigitEx(6000)
            repeats += 1
            if (repeats > 2):
                raise AgiKeyStroke('t')

    def mainIntro(self):
	new = self.vm_storage.newMessages()
	old = self.vm_storage.oldMessages()

	txt = self._ntts("You have %(num)n new", "You have %(num)n new", new)
	self.sayEx(txt, kw = {'num':new})
        if (old > 0):
            self.sayEx(self._ntts("and %n old", "and %n old", old), [ old ])
	self.sayEx(self._ntts("message", "messages", old + new))

    def browseMessages(self):
        if (self.vm_storage.folderIsEmpty()):
            self.sayEx(self._tts("You have no %s messages"), args = [ self._tts(self.vm_storage.sayFolderName()) ])
        else:
            self.playMessage()

    def getFolder2(self, msg, start):
        self.sayEx(msg)
        self.getFolder(start)

    def getFolder(self, start):
        self.sayEx(self._tts("press"))
        for x in range(start, 5):
            self.sayEx("%n", [x])
            self.sayEx(self._tts("for %s"), [self._tts(sayFolderNameById(x))])
            self.waitForDigitEx(500)
        self.sayEx(self._tts("or pound to cancel"))
        self.waitForDigitEx(4000)

    def playFolderName(self):
        self.sayEx(self._tts(self.vm_storage.sayFolderName()))

    def changePassword(self):
        password1 = self.readString(self._tts("Please enter your new PIN code followed by the pound key."), self.options().maxPasswordLen())
        password2 = self.readString(self._tts("Please reenter your PIN code followed by the pound key."), self.options().maxPasswordLen())
        if (type(password1) != type(password2) or type(password1) != type(str())):
            self.debug("Error occured while reading password")
            return
        if (password1 != password2):
            self.sayEx(self._tts("The PIN codes you've entered and reentered did not match. Please try again."))
        else:
            self.user.setPassword(password1)
            self.sayEx(self._tts("Your PIN code has been changed."))

    def optionsDefault(self):
        self.sayEx(self._tts("Press 1 to record your unavailable message. Press 2 to record your busy message. Press 3 to record your name. Press 4 to change your PIN code. Press star to return to the main menu."))
        self.waitForDigitEx(6000)

    def playRecordReview(self, prompt_id):
        if (prompt_id == PROMPT_UNV):
            self.rec_prompt = self._tts("After the tone say your unavailable message and then press the pound key.")
        elif (prompt_id == PROMPT_BUSY):
            self.rec_prompt = self._tts("After the tone say your busy message and then press the pound key.")
        elif (prompt_id == PROMPT_NAME):
            self.rec_prompt = self._tts("After the tone say your name and then press the pound key.")
        self.promptId = prompt_id
        #
        # retrieve prompt from prompt vm_storage
        #
        self.prompt_exists = False
        (self.promptFd, self.promptFilename) = tempfile.mkstemp(suffix = "." + self.format(), dir = self.options().tmpDir())
        m = re.search("(.+)\\." + self.format() + "$", self.promptFilename)
        self.promptFilenameNoExt = m.groups()[0]

        try:
            self.execMenu({ \
                '1':self.__savePrompt, \
                '2':self.reviewPrompt, \
                '3':self.recordPrompt, \
                'default':self.promptDefault, \
                'quit':'t#'
            }, '3')
        except AgiError:
            os.close(self.promptFd)
            os.unlink(self.promptFilename)
            raise
        os.close(self.promptFd)
        os.unlink(self.promptFilename)

    def __savePrompt(self):
        if (not self.prompt_exists):
            raise AgiKeyStroke('3')
        else:
            os.lseek(self.promptFd, 0, 0)
            self.user.savePrompt(self.promptId, self.promptFd, self.format())
            self.sayEx(self._tts("Your message has been saved."))
            raise AgiKeyStroke('t')

    def reviewPrompt(self):
        self.streamFileEx(self.promptFilenameNoExt)

    def recordPrompt(self):
        self.say(self.rec_prompt)
        try:
            #
            # If comercial codec is not installed then the silence detection
            # is unavailable and causes the RECORD FILE to fail. So just
            # turn the silence detection off.
            #
            # However if you've purchased the commercial codec, then you can disable
            # this behaviour by setting:
            #
            # vapp.commercial_codecs_installed = True
            #
            silence_sec = None
            if self.format() == 'sln' or vapp.commercial_codecs_installed:
                silence_sec = self.options().maxSilenceTimeSec()
            self.recordFileEx(filename = self.promptFilenameNoExt, \
                              format = self.format(), \
                              timeout_msec = self.options().maxGreetingTimeMsec(), \
                              escape = '#', \
                              beep = True, \
                              silence_sec = silence_sec)
        except AgiKeyStroke, keystroke:
            if (keystroke.keyCode() != -1):
                self.prompt_exists = True
            else:
                raise

    def promptDefault(self):
        if (self.prompt_exists):
            self.sayEx(self._tts("Press one to accept this recording. Press two to listen to it. Press three to rerecord your message."))
        else:
            self.sayEx(self._tts("Press three to rerecord your message."))
            self.waitForDigitEx(600)
        self.sayEx(self._tts("or pound to cancel"))
        self.waitForDigitEx(6000)

    def playMessage(self):
        try:
            self.starting = False
            if (self.curMsg() == 0):
                self.sayEx(self._tts("first message received %[S]D"), [self.curMsgDatetime()])
            elif (self.curMsg() == self.lastMsg()):
                self.sayEx(self._tts("last message received %[S]D"), [self.curMsgDatetime()])
            if (self.curMsg() != 0 and self.curMsg() < self.lastMsg()):
		self.sayEx(self._tts("message %(num)n received %(date)[S]D"), kw = { 'num':(self.curMsg() + 1), 'date':self.curMsgDatetime() })
        except AgiKeyStroke, keystroke:
            # Allow pressing '1' to skip intro
            if (keystroke.keyCode() != ord('1')):
                raise
        self.setHeard(True)
	msg = self.curMsgFile()
        self.streamFileEx(msg)

    #
    # Miscellaneous helper functions
    #
    def setCurMsg(self, num):
        self.vm_storage.setCurrentMessage(num)

    def curMsg(self):
        return self.vm_storage.currentMessage()

    def lastMsg(self):
        return self.vm_storage.lastMessage()

    def toggleDelete(self):
	self.vm_storage.setCurrentMessageDeleted(not self.vm_storage.isCurrentMessageDeleted())

    def setFolder(self, folder_id):
        self.vm_storage.setCurrentFolder(folder_id)

    def curMsgDatetime(self):
        return self.vm_storage.currentMessageDatetime(self.user.tz())

    def setHeard(self, val):
        self.vm_storage.setCurrentMessageHeard(val)

    def curMsgFile(self):
        return self.vm_storage.currentMessageFile()

    def isMsgDeleted(self):
        return self.vm_storage.isCurrentMessageDeleted()

    def delMsg(self):
        self.vm_storage.setCurrentMessageDeleted(True)

