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
Improved version of AgiHandler supporting TTS and IVR menus.
"""
from Agi import *

__all__ = ["BaseIvrHandler", "NoInputException", "ClearRequestException"]

class NoInputException(Exception):
    pass

class ClearRequestException(Exception):
    """
    The exception raised by BaseIvrHandler.readLine. Contains the input
    that has been entered before the '*' button is pressed.
    """
    def __init__(self, deleted_text):
	self.__deleted_text = deleted_text

    def deletedText(self):
	return self.__deleted_text

class BaseIvrHandler(AgiHandler):
    """
    Base IVR handler containing TTS support and IVR menu infrastructure.
    This is an abstract class.
    """

    def readLine(self, prompt, max_len, timeout_msec, editing_enabled = True):
        """
        TTS enabled method that provides a way to read a string with 
        possibility of editing. Special keys are '*' (clear input) and 
        '#' (end of input). The method raises a NoInputException when 
        entered string is empty and ClearRequestException when the '*' 
        key is pressed. 

        If editing_enabled is False the ClearRequestException is not
        generated.

        Example:

            while True:
                try:
                    number = self.readLine(_tts("Please enter a number"), 
                                10, 10000)
                    print "User entered %s" % number
                    break
                except NoInputException:
                    # user entered an empty string
                    self.say(_tts("You have not pressed any digit."))
                except ClearRequestException:
                    # user wants to reenter the number
                    pass
        """
	if (editing_enabled):
	    retval = ""
	    prompt_played = False
	    while (True):
		try:
		    if (not prompt_played):
			prompt_played = True
			self.sayEx(prompt)
		    self.waitForDigitEx(timeout_msec)
		    raise AgiKeyStroke('#')
		except AgiKeyStroke, e:
		    if (e.key() == '*'):
			raise ClearRequestException(retval)
		    elif (e.key() == '#'):
			if (retval == ""):
			    raise NoInputException()
			return retval
		    else:
			retval += e.key()
			if (len(retval) >= max_len):
			    return retval
	else:
	    retval = self.readString(prompt, max_len, timeout_msec);
	    if (retval == "" or type(retval) != type(str())):
		raise NoInputException()
	    return retval

    def readString(self, prompt_txt, max_len, timeout_msec):
        """
        TTS enabled method allowing to read input ending with pound (#).
        """
	text = self.textSynth().say(prompt_txt)
	prompts = self.speechSynth().promptFileSequence(text, True)

	retval = ""
	done = False
	while (not done):
	    timeout = True
	    try:
		if (retval == ""):
		    for prompt in prompts:
			self.streamFileEx(prompt)
		self.waitForDigitEx(timeout_msec)
	    except AgiKeyStroke, key:
		timeout = False
		if (key.key() == '#'):
		    done = True
		else:
		    retval += key.key()
		    if (len(retval) >= max_len):
			done = True
	    if (timeout):
		done = True
	return retval

    def sayEx(self, prompt_txt, args = [], kw = {}, escape = "#*1234567890", long_escapes = None):
        """
        TTS enabled method similar to AgiHandler.streamFileEx().
        """
	text = self.textSynth().say(prompt_txt, args, kw)
	prompts = self.speechSynth().promptFileSequence(text, True)
	for p in prompts:
	    self.streamFileEx(p, escape = escape, long_escapes = long_escapes)

    def say(self, text, args = [], kw = {}, escape = "", long_escapes=None):
        """
        TTS enabled method similar to AgiHandler.streamFile().
        """
        try:
            self.sayEx(text, args, kw, escape, long_escapes)
        except AgiKeyStroke:
            pass

    def runSession(self):
        """
        The method that calls these abstract methods in the following order:
            self.parseNetworkScript()
            self.answerSession()
            self.handleCall()
	    self.cleanup()
        """
        self.parseNetworkScript()
	self.answerSession()
	self.handleCall()
	self.cleanup()
	
    def execMenu(self, menu, start = None):
        """
        This method allows to create IVR menus with single keypress 
        navigation. The 'menu' argument is dictionary (see example). 
        The 'start' argument allows to go directly to the specified 
        menu item upon menu start.

        Example

            def runMenuItem(self):
                ...

            menu = { \\
                'quit'    : '*4',  # quit by pressing either '*' or '4'
                'intro'   : lambda : self.sayEx(_tts("Hello!")),
                'default' : lambda : self.sayEx(_tts("Press a key.")),
                'wrong'   : lambda : self.sayEx(_tts("Wrong key."))
                'error'   : lambda : self.sayEx(_tts("Try again later."))
                'max_attempts' : 5,
                '1'       : self.runMenuItem
            }
            self.execMenu(menu)

        The default values for the keywords:

            'quit'          - '#'
            'intro'         - None
            'default'       - lambda : self.waitForDigitEx(6000)
            'wrong'         - None
            'error'         - None
            'max_attempts'  - 3
        """
        #
        # Verify the existence of the quit handler
        #
        if (menu.has_key('quit')):
            quit_chars = menu['quit']
        else:
            quit_chars = '#'
        #
        # Check the default handler
        #
        if (menu.has_key('default')):
            default = menu['default']
        else:
            default = lambda : self.waitForDigitEx(6000)
        #
        # Respect the start keystroke
        #
        if (start != None):
            cmd = AgiKeyStroke(start)
        else:
            cmd = None
        #
        # Play intro if any
        #
        if (menu.has_key('intro')):
            try:
                menu['intro']()
            except AgiKeyStroke, keystroke:
                cmd = keystroke
	
	max_attempts = 3
	if (menu.has_key('max_attempts')):
	    max_attempts = menu['max_attempts']
	
	on_err_handler = None
	if (menu.has_key('error')):
	    on_err_handler = menu['error']
	
	on_wrong_handler = None
	if (menu.has_key('wrong')):
	    on_wrong_handler = menu['wrong']
        #
        # Main loop
        #
        repeats = 0
        while (True):
            try:
                # quit on error or on the quit command
		if (cmd != None):
		    if ((cmd.keyCode() < 0) or (cmd.key() in quit_chars)):
			break
		    if (menu.has_key(cmd.key())):
			repeats = 0
			menu[cmd.key()]()
			cmd = None
			continue
		    else:
			repeats += 1
			if (repeats >= max_attempts):
			    if (on_err_handler != None):
				on_err_handler()
			    break
			# Key has no handler assosiated - use the default
			if (on_wrong_handler != None):
			    on_wrong_handler()
			default()
			self.waitForDigitEx(self.options().defaultPromptTimeoutMsec())
		else:
		    default()
		    self.waitForDigitEx(self.options().defaultPromptTimeoutMsec())
                cmd = AgiKeyStroke(0)
            except AgiKeyStroke, keystroke:
                cmd = keystroke
