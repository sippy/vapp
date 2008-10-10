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
Abstract interface to voicemail storage.
"""

FOLDER_INBOX   = 0
FOLDER_OLD     = 1
FOLDER_WORK    = 2
FOLDER_FAMILY  = 3
FOLDER_FRIENDS = 4
FOLDER_CUST1   = 5
FOLDER_CUST2   = 6
FOLDER_CUST3   = 7
FOLDER_CUST4   = 8
FOLDER_CUST5   = 9

__all__ = [ \
        "AbstractVoicemailStorage", \
        "FOLDER_INBOX", \
        "FOLDER_OLD", \
        "FOLDER_WORK", \
        "FOLDER_FAMILY", \
        "FOLDER_FRIENDS", \
        "FOLDER_CUST1", \
        "FOLDER_CUST2", \
        "FOLDER_CUST3", \
        "FOLDER_CUST4", \
        "FOLDER_CUST5", \
        "folderNameById", \
        "sayFolderNameById", \
        "VM_MailboxFullError"
    ]

class VM_MailboxFullError:
    pass

def _tts_noop(arg):
    return arg

def sayFolderNameById(ID):
    if (ID == FOLDER_INBOX):
        return _tts_noop("new")
    elif (ID == FOLDER_OLD):
        return _tts_noop("old")
    elif (ID == FOLDER_WORK):
        return _tts_noop("work")
    elif (ID == FOLDER_FAMILY):
        return _tts_noop("family")
    elif (ID == FOLDER_FRIENDS):
        return _tts_noop("friends")
    elif (ID == FOLDER_CUST1):
        return _tts_noop("folder five")
    elif (ID == FOLDER_CUST2):
        return _tts_noop("folder six")
    elif (ID == FOLDER_CUST3):
        return _tts_noop("folder seven")
    elif (ID == FOLDER_CUST4):
        return _tts_noop("folder eight")
    elif (ID == FOLDER_CUST5):
        return _tts_noop("folder nine")

def folderNameById(ID):
    if (ID == FOLDER_INBOX):
        return "INBOX"
    elif (ID == FOLDER_OLD):
        return "Old"
    elif (ID == FOLDER_WORK):
        return "Work"
    elif (ID == FOLDER_FAMILY):
        return "Family"
    elif (ID == FOLDER_FRIENDS):
        return "Friends"
    elif (ID == FOLDER_CUST1):
        return "Cust1"
    elif (ID == FOLDER_CUST2):
        return "Cust2"
    elif (ID == FOLDER_CUST3):
        return "Cust3"
    elif (ID == FOLDER_CUST4):
        return "Cust4"
    elif (ID == FOLDER_CUST5):
        return "Cust5"

class AbstractVoicemailStorage:
    """
    Abstract interface to voicemail storage. Actual storage should
    inherit this class and implement the following methods:

    setCurrentFolder(folder_id) 
	where folder_id is integer in range from 0 to 9. 
	No return value required.

    currentFolderId()
	Must return current folder ID.

    numOfMessages()
	Must return number of messages in current folder.

    setCurrentMessage(idx)
	Seek to specified message in the folder. 'idx' is zero based.
	No return value required.

    currentMessage()
	Must return current message index. Value of -1 means that
	current message is not selected.

    currentMessageDatetime(tz)
	Must return current message datetime adjusted to specified
	timezone. The value should be datetime.datetime() object
	or compatible.

    currentMessageFile()
	Must return filename (without extension) containing the
	voice message.

    setCurrentMessageHeard(val)
	Set the flag 'heard' of the current message.
	No return value required.

    isCurrentMessageDeleted()
	Returns True or False

    setCurrentMessageDeleted(val)
	The 'val' is True or False.
	No return value required.

    saveCurrentMessageToFolder(folder_id)
	No return value required.

    finalize()
	Do post hangup procedures. Cleanup temporary files, 
	remove deleted messages, etc.
	No return value required.

    saveMessage(fd, format)
	Save the message from the temporary file on disk to the real
	storage.

	fd - active file() object with message data

	format - the format of the message data
	
    """
    def __init__(self):
        self.setCurrentFolder(FOLDER_INBOX)

    def newMessages(self):
        old_folder = None
        if (self.currentFolderId() != FOLDER_INBOX):
            old_folder = self.currentFolderId()
            self.setCurrentFolder(FOLDER_INBOX)
        ret = self.numOfMessages()
        if (old_folder != None):
            self.setCurrentFolder(old_folder)
        return ret

    def oldMessages(self):
        old_folder = None
        if (self.currentFolderId() != FOLDER_OLD):
            old_folder = self.currentFolderId()
            self.setCurrentFolder(FOLDER_OLD)
        ret = self.numOfMessages()
        if (old_folder != None):
            self.setCurrentFolder(old_folder)
        return ret

    def folderIsEmpty(self):
        return self.numOfMessages() == 0

    def sayFolderName(self):
        return sayFolderNameById(self.currentFolderId())

    def folderName(self):
        return folderNameById(self.currentFolderId())

    def lastMessage(self):
        return self.numOfMessages() - 1
