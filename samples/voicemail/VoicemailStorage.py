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
Simple voicemail storage. Mailbox locking is not implemented
intentionally as it will complicate the example but the purpose
of this example is rather educational than practical.
"""
import os
import fcntl
from vapp.voicemail.AbstractVoicemailStorage import *
import pytz
import datetime

basePath = "/var/spool/vapp-voicemail"

def msg_cmp(m1, m2):
    if (m1.name() == m2.name()):
        return 0
    elif (m1.name() < m2.name()):
        return -1
    else:
        return 1

class Message:
    def __init__(self, name, ext):
        self.__name = name
        self.__ext = ext
        self.__heard = False
        self.__deleted = False

    def name(self):
        return self.__name

    def ext(self):
        return self.__ext

    def heard(self):
        return self.__heard

    def deleted(self):
        return self.__deleted

    def setHeard(self, heard):
        self.__heard = heard

    def setDeleted(self, deleted):
        self.__deleted = deleted

class Folder:
    def __init__(self, folder_path):
        self.__home = folder_path
        self.__current_msg = -1
        self.__messages = []
        try:
            for name in os.listdir(folder_path):
                try:
                    (name, ext) = name.split('.', 1)
                    fid = int(name)
                    self.__messages.append(Message(fid, ext))
                except ValueError:
                    pass
        except OSError:
            pass
        self.__messages.sort(msg_cmp)
        if (len(self.__messages) != 0):
            self.__current_msg = 0

    def home(self):
        return self.__home

    def numOfMessages(self):
        return len(self.__messages)

    def currentMessage(self):
        return self.__current_msg

    def currentMessageFile(self):
        msg = self.__messages[self.__current_msg]
        return "%s/%d" % (self.__home, msg.name())

    def currentMessageDatetime(self, tz):
        msg = self.__messages[self.__current_msg]
        fname = "%s/%d.%s" % (self.__home, msg.name(), msg.ext())
        return datetime.datetime.fromtimestamp(os.stat(fname).st_birthtime, pytz.timezone(tz))

    def setCurrentMessageHeard(self, heard):
        self.__messages[self.__current_msg].setHeard(heard)

    def setCurrentMessage(self, mid):
        self.__current_msg = mid

    def finalize(self, owner):
        old_messages_path = "%s/%d" % (owner.home(), FOLDER_OLD)
        inbox_path = "%s/%d" % (owner.home(), FOLDER_INBOX)
        for msg in self.__messages:
            if (msg.deleted()):
                try:
                    os.unlink("%s/%d.%s" % (self.__home, msg.name(), msg.ext()))
                except:
                    pass
            elif (msg.heard()):
                from_path = "%s/%d.%s" % (inbox_path, msg.name(), msg.ext())
                to_path = "%s/%d.%s" % (old_messages_path, msg.name(), msg.ext())
                try:
                    os.renames(from_path, to_path)
                except:
                    pass

    def setCurrentMessageDeleted(self, deleted):
        self.__messages[self.__current_msg].setDeleted(deleted)

    def isCurrentMessageDeleted(self):
        return self.__messages[self.__current_msg].deleted()

    def takeCurrent(self):
        ret = self.__messages.pop(self.__current_msg)
        if (len(self.__messages) >= self.__current_msg):
            self.__current_msg = len(self.__messages) - 1
        return ret

    def putMessage(self, msg, from_path):
        self.__messages.append(msg)
        self.__messages.sort(msg_cmp)
        msg.setHeard(False)
        to_path = "%s/%d.%s" % (self.__home, msg.name(), msg.ext())
        os.renames(from_path, to_path)


class VoicemailStorage(AbstractVoicemailStorage):
    def __init__(self, user):
        self.__home = "%s/%s" % (basePath, user.username())
        try:
            os.stat(self.__home)
        except OSError:
            raise Exception("No mailbox found")
        self.__current_folder = None
        self.__folders = {}
        self.setCurrentFolder(FOLDER_INBOX)

    def home(self):
        return self.__home

    def setCurrentFolder(self, fid):
        self.__current_folder = fid
        self.__loadFolder(fid)

    def __loadFolder(self, fid):
        if fid not in self.__folders:
            folder_path = "%s/%d" % (self.__home, fid)
            self.__folders[fid] = Folder(folder_path)
        return self.__folders[fid]

    def currentFolderId(self):
        return self.__current_folder

    def numOfMessages(self):
        return self.__folders[self.__current_folder].numOfMessages()

    def setCurrentMessage(self, mid):
        self.__folders[self.__current_folder].setCurrentMessage(mid)

    def setCurrentMessageDeleted(self, deleted):
        self.__folders[self.__current_folder].setCurrentMessageDeleted(deleted)

    def currentMessage(self):
        return self.__folders[self.__current_folder].currentMessage()

    def currentMessageFile(self):
        return self.__folders[self.__current_folder].currentMessageFile()

    def currentMessageDatetime(self, tz):
        return self.__folders[self.__current_folder].currentMessageDatetime(tz)

    def isCurrentMessageDeleted(self):
        return self.__folders[self.__current_folder].isCurrentMessageDeleted()

    def saveCurrentMessageToFolder(self, target_folder):
        target = self.__loadFolder(target_folder)
        src = self.__folders[self.__current_folder]
        msg = src.takeCurrent()
        from_path = "%s/%d.%s" % (src.home(), msg.name(), msg.ext())
        target.putMessage(msg, from_path)

    def saveMessage(self, fd, format, cli, logger):
        folder_path = "%s/%d" % (self.__home, FOLDER_INBOX)
        last_id_filename = "%s/last_id.txt" % self.__home
        try:
            os.stat(folder_path)
        except OSError:
            os.makedirs(folder_path)
        try:
            last_id = int(file(last_id_filename).readline()) + 1
        except IOError:
            last_id = 0
        tmp = file(last_id_filename, "w")
        tmp.write("%d" % last_id)
        tmp.close()
        outfile = "%s/%d.%s" % (folder_path, last_id, format)
        out = file(outfile, "w")
	while True:
	    buf = os.read(fd, 8192)
	    if (buf == None or buf == ""):
		break
	    out.write(buf)

    def setCurrentMessageHeard(self, heard):
        if (self.__current_folder != FOLDER_INBOX):
            return
        return self.__folders[self.__current_folder].setCurrentMessageHeard(heard)

    def finalize(self):
        for fld in self.__folders.itervalues():
            fld.finalize(self)
