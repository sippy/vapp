#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
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

import datetime

__all__ = [ "VI" ]

def _phrase_noop(str):
    return unicode(str, 'utf-8')

ONES = [
	_phrase_noop("không"),	# 0
	_phrase_noop("một"),  	# 1
	_phrase_noop("hai"),	# 2
	_phrase_noop("ba"),	# 3
	_phrase_noop("bốn"),	# 4
	_phrase_noop("năm"),	# 5
	_phrase_noop("sáu"),	# 6
	_phrase_noop("bảy"),	# 7
	_phrase_noop("tám"),	# 8
	_phrase_noop("chín")	# 9
	]

def sayNumber(number, ordinal, flags):
    retval = []
    number = int(number)
    if (number == 0):
        return ONES[0]

    if ordinal:
        retval.append(_phrase_noop("thứ"))
        if number == 1:
            retval.append(_phrase_noop("nhất"))
        elif number == 4:
            retval.append(_phrase_noop("tư"))
        else:
            try:
                retval.append(ONES[number])
            except:
                pass
        return " ".join(retval)

    minus = False
    build_started = False

    if (number < 0):
        number = -number
        minus = True
        retval.append(_phrase_noop("trừ đi"))

    if number >= 1000000:
        if minus:
            return _phrase_noop("Less than minus one million") 
        else:
            return _phrase_noop("More than one million")

    if number >= 1000: # and number < 10000
        retval += _say_num(number / 1000, False)
        retval.append(_phrase_noop("ngàn")) # "thousand"
        build_started = True
    number = number % 1000
    retval += _say_num(number, build_started)

    return " ".join(retval)

def _say_num(num, build_started):
    ret = []
    if num >= 100 or build_started:
        ret.append(ONES[(num % 1000) / 100])
        ret.append(_phrase_noop("trăm"))
        build_started = True
    num = num % 100
    tens = num / 10
    if num >= 20:
        ret.append(ONES[num / 10])
        ret.append(_phrase_noop("mươi"))
    elif num >= 10:
        ret.append(_phrase_noop("mười"))
    num = num % 10
    if num != 0:
        if num == 1 and build_started:
            ret.append(_phrase_noop("linh"))
            ret.append(ONES[1])
        elif tens > 0 or build_started:
            if num == 1:
                ret.append(_phrase_noop("mốt"))
            elif num == 4:
                ret.append(_phrase_noop("tư"))
            elif num == 5:
                ret.append(_phrase_noop("lăm"))
            else:
                ret.append(ONES[num])
        else:
            ret.append(ONES[num])
    return ret


def sayDigits(num, flags):
    return " ".join([ ONES[int(x)] for x in str(num) if x.isdigit() ])

def sayDuration(seconds, say_hours, say_minutes, say_seconds, flags):
    retval = []
    s = seconds
    hours = 0
    minutes = 0
    if (say_hours):
        hours = int(s / 3600)
        s -= hours * 3600
        if (say_minutes):
            minutes = int((s / 60) % 60)
            s -= minutes * 60
    else:
        minutes = int(s / 60)
    s = int(s % 60)
    if hours + minutes > 0 and not say_seconds:
        s = 0
    if (hours > 0):
        retval.append(sayNumber(hours, False, None))
        retval.append(_phrase_noop("giờ"))
    if (minutes > 0):
        retval.append(sayNumber(minutes, False, None))
        retval.append(_phrase_noop("phút"))
    if (s > 0 or seconds == 0):
        retval.append(sayNumber(s, False, None))
        retval.append(_phrase_noop("giây"))
    return " ".join(retval)


def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = []
    now = datetime.datetime.now(date_time.tzinfo)

    if say_date:
        if date_time.date() == now.date():
            retval.append(_phrase_noop("hôm nay")) # today
        elif date_time.date() == now.date() - datetime.timedelta(1):
            retval.append(_phrase_noop("hôm qua")) # yesterday
        elif date_time.date() == now.date() + datetime.timedelta(1):
            retval.append(_phrase_noop("mai")) # tomorrow
        else:
            retval.append(_phrase_noop("ngày"))
            retval.append(sayNumber(date_time.day, False, None))
            retval.append(_phrase_noop("tháng"))
            if date_time.month == 1:
                ret.append(_phrase_noop("giên"))
            elif date_time.month == 4:
                ret.append(_phrase_noop("tư"))
            elif date_time.month == 12:
                ret.append(_phrase_noop("chap"))
            retval.append(sayNumber(date_time.month, False, None))
            retval.append(_phrase_noop("năm"))
            retval.append(sayNumber(date_time.year, False, None))
        if say_time:
            retval.append(_phrase_noop("lúc"))
    if say_time:
        suffix = _phrase_noop("sáng") # AM
        hour = date_time.hour
        if (hour >= 12):
            hour -= 12
            suffix = _phrase_noop("chiều") # PM
        if (hour == 0):
            hour = 12
        retval.append(sayNumber(hour, False, None))
        retval.append(_phrase_noop("giờ"))
        minute = date_time.minute
        if (minute > 0):
            retval.append(sayNumber(minute, False, None))
            retval.append(_phrase_noop("phút"))
        if (say_seconds):
            secs = date_time.second
            retval.append(sayNumber(secs, False, None))
            retval.append(_phrase_noop("giây"))
        retval.append(suffix)
    return " ".join(retval)

if (__name__ == "__main__"):
    print "=== Vietnamese numbers ==="
    for i in range(10) + [10, 11, 14, 15, 100, 101, 102, 1004, 2045, 34567, 400001, 1000001, -1, -1000001]:
        print("  %d: %s" % (i, sayNumber(i, False, "")))
    print "=== Vietnamese ordinal numbers ==="
    for i in range(1, 10):
        sufx = "th"
        if i == 1:
            sufx = "st"
        elif i == 2:
            sufx = "nd"
        elif i == 3:
            sufx = "rd"
        print("  %d%s: %s" % (i, sufx, sayNumber(i, True, "")))
    print "=== Vietnamese durations ==="
    for i in (0, 1, 23, 466, 78910, 11, 12, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("  %02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, True, None)))
