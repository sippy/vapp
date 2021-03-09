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
Asterisk Manager Protocol implementation.
"""
import os
import sys
import traceback
import select
import socket
import threading
from . import get_arg_delimiter

__all__ = [ "AsteriskManager" ]

reconnect_seconds = 5

class Packet:
    """
    Wrapper for Asterisk events and responses. It is passed to
    event listeners as argument to processMgrPacket() method call.
    """
    def __init__(self, lines):
        self.__isResponse = False
        self.__response = None
        self.__isError = False
        self.__message = ''
        self.__state = None
        self.__channel = None
        self.__channel1 = None
        self.__source = None
        self.__uniqueid = None
        self.__uniqueid1 = None
        self.__event = None
        self.__destination = None
        self.__actionId = None
        self.__other = ""
        self.__variable = None
        self.__value = None

        for l in lines:
            if (l.find(": ") < 0):
                if l.find(":"):
                    continue
                raise Exception("Bad line received from the asterisk manager: '%s'" % l)
            field, value = l.split(": ", 1)
            if (field == 'Response'):
                self.__isResponse = True
                self.__response = value
                if (self.__response != 'Success'):
                    self.__isError = True
            elif (field == 'Message'):
                self.__message = value
            elif (field == 'State'):
                self.__state = value
            elif (field == 'Channel'):
                self.__channel = value
            elif (field == 'Channel1'):
                self.__channel1 = value
            elif (field == 'Source'):
                self.__source = value
            elif (field == 'Uniqueid'):
                self.__uniqueid = value
            elif (field == 'Uniqueid1'):
                self.__uniqueid1 = value
            elif (field == 'Event'):
                self.__event = value
            elif (field == 'Destination'):
                self.__destination = value
            elif (field == 'ActionID'):
                self.__actionId = value
            elif (field == 'Variable'):
                self.__variable = value
            elif (field == 'Value'):
                self.__value = value
            else:
                self.__other += "|%s: %s" % (field, value)

    def __str__(self):
        retval = ""
        if (self.__event != None):
            retval += "Event: "		+ self.__event + "\n"

        if (self.__response != None):
            retval += "Response: "	+ self.__response + "\n"

        if (self.__state != None):
            retval += "State: "		+ self.__state + "\n"

        if (self.__channel != None):
            retval += "Channel: "	+ self.__channel + "\n"

        if (self.__channel1 != None):
            retval += "Channel1: "	+ self.__channel1 + "\n"

        if (self.__source != None):
            retval += "Source: "	+ self.__source + "\n"

        if (self.__uniqueid != None):
            retval += "Uniqueid: "	+ self.__uniqueid + "\n"

        if (self.__uniqueid1 != None):
            retval += "Uniqueid1: "	+ self.__uniqueid1 + "\n"

        if (self.__actionId != None):
            retval += "ActionID: "	+ self.__actionId + "\n"

        if (self.__destination != None):
            retval += "Destination: "	+ self.__destination + "\n"

        if (self.__message != ''):
            retval += "Message: " + self.__message + "\n"

        if (self.__variable != None):
            retval += "Variable: " + self.__variable + "\n"

        if (self.__variable != None):
            retval += "Value: " + self.__value + "\n"

        if (self.__other != ""):
            retval += self.__other + "\n"

        return retval

    def isResponse(self):
        return self.__isResponse

    def isError(self):
        """ The packet is Response but is not Success """
        return self.__isError

    def message(self):
        return self.__message

    def state(self):
        return self.__state

    def channel(self):
        return self.__channel

    def channel1(self):
        return self.__channel1

    def source(self):
        return self.__source

    def uniqueId(self):
        return self.__uniqueid

    def uniqueId1(self):
        return self.__uniqueid1

    def event(self):
        return self.__event

    def destination(self):
        return self.__destination

    def actionId(self):
        return self.__actionId

    def variable(self):
        return self.__variable

    def value(self):
        return self.__value


class AsteriskManager(threading.Thread):
    """
    The class running an Asterisk Manager protocol implementation.
    """

    __authenticated = False
    __auth_sent = False
    __sock = None

    def __init__(self, host = "127.0.0.1", port = 5038, username = None,
            password = None, logger = None):
        """
        Constructor.

        host, port, username and password are used to connect to
            Asterisk manager

        logger - a logger instance (log4py compatible)
        """
        self.__read_cmd, self.__write_cmd = os.pipe()
        self.__cmd_queue = []
        self.__cmd_lock = threading.Lock()
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.__channels = {}
        self.__auth_cond = threading.Condition()
        self.__chan_lock = threading.Lock()
        self.__parent_by_child = {}
        self.__child_by_parent = {}
        self.__parse_buf = ""
        self.__action_listeners = {}
        self.__action_lock = threading.Lock()

        self.__host = host
        self.__port = port
        self.__username = self.__ensure_bytes(username)
        self.__password = self.__ensure_bytes(password)
        self.__logger = logger

    def __ensure_bytes(self, s):
        if s == None or isinstance(s, bytes):
            return s
        return s.encode('utf-8')

    def __del__(self):
        try:
            os.close(self.__read_cmd)
        except:
            pass
        try:
            os.close(self.__write_cmd)
        except:
            pass

    def __parse(self, buf):
        if (buf.startswith(b'Asterisk Call Manager')):
            return [ Packet([]) ]
        self.__parse_buf += buf.decode('utf-8', 'ignore')
        ret = []
        tmp = []
        lines = self.__parse_buf.split('\r\n')
        while (len(lines) > 0):
            l = lines.pop(0)
            if (l != ''):
                if (len(lines) == 0):
                    # unfinished part of the line.
                    # wait till next input
                    lines.insert(0, l)
                    break
                tmp.append(l)
            else:
                if (len(lines) == 0):
                    # Not an empty line, just EOL of last line
                    # Keep the rest of the buf and return
                    tmp.append(l)
                    break
                pkt = Packet(tmp)
                ret.append(pkt)
                tmp = []
        self.__parse_buf = '\r\n'.join(tmp)
        return ret

    def run(self):
        """ Protocol thread runner. """
        while (True):
            try:
                self.__run()
            except:
                tmp = self.__sock
                self.__sock = None # force reconnect
                if (self.__logger):
                    for msg in traceback.format_exception(*sys.exc_info()):
                        self.__logger.error(msg)

                try:
                    tmp.close()
                except:
                    pass
                tmp = None

    def __run(self):
        pkt = None
        while (True):
            timeout = None
            if (self.__sock == None):
                self.__authenticated = False
                self.__auth_sent = False
                self.__parse_buf = ""

            if (not self.__authenticated):
                timeout = reconnect_seconds

            if (self.__sock == None):
                listen_fds = [self.__read_cmd]
            else:
                listen_fds = [self.__sock, self.__read_cmd]

            try:
                rlist, wlist, xlist = select.select(listen_fds, [], [], timeout)
            except select.error:
                continue # Ignore 'Interrupted system call' and friends

            if (self.__read_cmd in rlist):
                os.read(self.__read_cmd, 10)

            if (self.__sock == None):
                try:
                    self.__reconnect()
                except socket.error as e:
                    if (self.__logger):
                        self.__logger.info("AsteriskMgr: Connection to Asterisk Manager failed: %s." % (e))
                    continue

            if (self.__authenticated):
                self.__processCmdQueue()

            if (not (self.__sock in rlist)):
                continue

            res = self.__sock.recv(16384)
            if (res == ""):
                if (self.__logger):
                    self.__logger.info("AsteriskMgr: Connection to Asterisk Manager broke. Reconnecting...")
                self.__auth_cond.acquire()

                self.__authenticated = False
                self.__auth_sent = False
                try:
                    self.__sock.close()
                except:
                    pass
                self.__sock = None

                self.__auth_cond.notifyAll()
                self.__auth_cond.release()
                continue

            for pkt in self.__parse(res):
                if (not self.__authenticated):
                    if (not self.__auth_sent):
                        self.__sock.send((
                            b"Action: login\r\n"
                            b"Username: %s\r\n"
                            b"Secret: %s\r\n"
                            b"\r\n") %
                            (self.__username,
                             self.__password))
                        self.__auth_sent = True
                    else:
                        if (pkt.isResponse()):
                            if (pkt.isError()):
                                if (self.__logger):
                                    self.__logger.error("AsteriskMgr: Authentication failed. Please check configuration of Asterisk...")
                                try:
                                    self.__sock.close()
                                except:
                                    pass
                                self.__sock = None
                            else:
                                if (self.__logger):
                                    self.__logger.debug("AsteriskMgr: Authentication successfull")
                                self.__auth_cond.acquire()
                                self.__authenticated = True
                                self.__auth_cond.notifyAll()
                                self.__auth_cond.release()
                else:
                    self.__processPacket(pkt)
                pkt = None


    def __reconnect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__host, self.__port))
        self.__sock = s

    def __processCmdQueue(self):
        self.__cmd_lock.acquire()
        while (len(self.__cmd_queue) > 0):
            cmd = self.__cmd_queue.pop()
            try:
                self.__sock.send(cmd.encode('utf-8'))
            except:
                self.__sock = None
                break
        self.__cmd_lock.release()

    def originate(self, cld, timeout, sip_proxy, cli, app, app_data, md5secret = None, authname = None, action_id = None, action_listener = None, password = None, call_id = None, codecs = "g729,ulaw,alaw", vars = []):
        """
        This method allows to originate a call in syncronous mode using
        SIP channel. The call is backed by application 'app' running with
        arguments 'app_data'. Optional 'action_id' and 'action_listener'
        arguments allow to control the status of the call.

        The 'action_listener' must be a class with a processMgrPacket()
        method defined. Call state change will be reported to this
        class via call to this method. (see also registerChannel())
        """
        variables = list(vars)
        self.__checkConnection()
        qry = ("Action: Originate\r\n"
               "Async: yes\r\n")
        if (md5secret != None or password != None):
            if (md5secret == None):
                md5secret = ""
            if (password == None):
                password = ""
            qry += ("Channel: SIP/%(CLD)s:%(password)s:%(md5secret)s:%(authname)s@%(SIP_PROXY)s\r\n"
                % { 'CLD' : cld,
                    'md5secret' : md5secret,
                    'password' : password,
                    'authname' : authname,
                    'SIP_PROXY' : sip_proxy } )
        else:
            qry += "Channel: SIP/%s@%s\r\n" % (cld, sip_proxy)

        qry += "Timeout: %d\r\n" % timeout
        qry += "CallerID: %s\r\n" % cli
        qry += "Application: %s\r\n" % app
        qry += "Data: %s\r\n" % app_data
        qry += "Codecs: %s\r\n" % codecs

        if (call_id != None):
            variables.append("_SIP_FORCE_CALLID=%s" % call_id)

        if (action_id != None and action_listener != None):
            self.__action_listeners[action_id] = action_listener
            qry += "ActionID: %s\r\n" % action_id
            variables.append("_VAPP_ACTION_ID=%s" % action_id)

        if (len(variables) > 0):
            qry += "Variable: %s\r\n" % get_arg_delimiter().join(variables)

        qry += "\r\n"
        self.__send_cmd(qry)

    def absoluteTimeout(self, chan, timeout):
        qry = ("Action: AbsoluteTimeout\r\n"
               "Channel: %s\r\n"
               "Timeout: %s\r\n"
               "\r\n" % (chan, str(timeout)))
        self.__send_cmd(qry)

    def hangup(self, chan_name):
        qry = ("Action: Hangup\r\n"
               "Channel: %s\r\n"
               "\r\n" % chan_name)
        self.__send_cmd(qry)

    def __send_cmd(self, qry):
        self.__cmd_lock.acquire()
        self.__cmd_queue.append(qry)
        self.__cmd_lock.release()
        os.write(self.__write_cmd, b"1") # notify worker thread

    def __checkConnection(self):
        self.__auth_cond.acquire()
        while (not self.__authenticated):
            os.write(self.__write_cmd, b"1") # request reconnect
            self.__auth_cond.wait()
        self.__auth_cond.release()


    def registerChannel(self, listener):
        """
        Register event listener for the channel. The 'listener'
        must have a method channel() returning Asterisk channel name.

        All events relevant to the specified channel will be reported
        via the listener.processMgrPacket(pkt) call.
        """
        self.__checkConnection()
        self.__chan_lock.acquire()
        try:
            self.__channels[listener.channel()] = listener
        except:
            if (self.__logger):
                for msg in traceback.format_exception(*sys.exc_info()):
                    self.__logger.error(msg)
        self.__chan_lock.release()

    def unregisterChannel(self, listener):
        """
        Unregister listener that was registered via registerChannel().
        """
        self.__chan_lock.acquire()
        try:
            self.__channels.pop(listener.channel())
            child = listener.childChannel()
            parent = self.__parent_by_child[child]
            self.__parent_by_child.pop(child)
            self.__child_by_parent.pop(parent)
        except:
            pass
        self.__chan_lock.release()

    def unregisterChildChannel(self, child):
        """
        Unregister child channel that was registered via
        registerChildChannel() call.
        """
#	self.__chan_lock.acquire()
        try:
            parent = self.__parent_by_child[child]
            self.__parent_by_child.pop(child)
            self.__child_by_parent.pop(parent)
        except:
            pass
#	self.__chan_lock.release()

    def registerChildChannel(self, parent, child):
        """
        Route events for the child Asterisk channel to parent channel
        listener. Both 'parent' and 'child' are simple strings containing
        Asterisk channel names.
        """
#	self.__chan_lock.acquire()
        self.__parent_by_child[child] = parent
        self.__child_by_parent[parent] = child
#	self.__chan_lock.release()

    def unlistenActionId(self, action_id):
        """
        Unregister event listener registered via originate() call.
        """
        self.__action_lock.acquire()
        try:
            self.__action_listeners.pop(action_id)
        except:
            pass
        self.__action_lock.release()

    def __processPacket(self, pkt):
        #print("### %s" % str(pkt))

        if pkt.event() == 'Newchannel':
            self.__send_cmd("Action: GetVar\r\n"
                    "Channel: " + pkt.channel() + "\r\n"
                    "Variable: VAPP_ACTION_ID\r\n"
                    "ActionId: " + pkt.channel() + "\r\n"
                    "\r\n" )

        if pkt.isResponse() and pkt.variable() == 'VAPP_ACTION_ID' and pkt.value() != '':
            action_id = pkt.value()
            channel = pkt.actionId()
            listener = self.__action_listeners.get(action_id, None)
            if listener != None:
                p = Packet([ "Event: Newchannel",
                             "Channel: " + channel,
                             "ActionID: " + action_id ])
                listener.processMgrPacket(p)
            return

        action_id = pkt.actionId()
        listener = None
        if action_id != None and (action_id in self.__action_listeners):
            self.__action_lock.acquire()
            try:
                listener = self.__action_listeners[action_id]
            except:
                pass
            self.__action_lock.release()
            if (listener != None):
                listener.processMgrPacket(pkt)

        chan = pkt.channel()
        if (chan == None):
            chan = pkt.channel1()
        if (chan == None):
            chan = pkt.source()

        unique_id = pkt.uniqueId()
        if (unique_id == None):
            unique_id = pkt.uniqueId1()

        self.__chan_lock.acquire()
        try:
            if chan != None and (chan in self.__channels):
                self.__channels[chan].processMgrPacket(pkt)
            elif (chan in self.__parent_by_child) and (self.__parent_by_child[chan] in self.__channels):
                self.__channels[self.__parent_by_child[chan]].processMgrPacket(pkt)
        except:
            pass
        self.__chan_lock.release()
