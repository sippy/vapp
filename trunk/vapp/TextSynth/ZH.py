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

__all__ = [ "ZH" ]

def _phrase_noop(str):
    return unicode(str, 'utf-8')

ONES = [
	_phrase_noop("零"),  	# 0
	_phrase_noop("一"),	# 1
	_phrase_noop("二"),	# 2
	_phrase_noop("三"),	# 3
	_phrase_noop("四"),	# 4
	_phrase_noop("五"),	# 5
	_phrase_noop("六"),	# 6
	_phrase_noop("七"),	# 7
	_phrase_noop("八"),	# 8
	_phrase_noop("九")	# 9
	]

#MONTHS = [ 
#	_phrase_noop("一月"), 		# January
#	_phrase_noop("二月"),		# February
#	_phrase_noop("三月"),		# March
#	_phrase_noop("四月"),		# April
#	_phrase_noop("五月"),		# May
#	_phrase_noop("六月"),	        # June
#	_phrase_noop("七月"),		# July
#	_phrase_noop("八月"),	        # August
#	_phrase_noop("九月"),		# September
#	_phrase_noop("十月"),		# October
#	_phrase_noop("十一月"),		# November
#	_phrase_noop("十二月")		# December
#	]

def sayNumber(number, ordinal, flags):
    if (number == 0):
        return _phrase_noop("零")

    retval = ""
    minus = False

    if (number < 0):
        number = -number
        minus = True

    num = int(number / 100000000)
    if (num > 0):
        retval += _say10000(num) + " " + _phrase_noop("亿") + " "

    num = (number / 10000) % 10000
    if (num > 0):
        retval += _say10000(num) + " " + _phrase_noop("万") + " "

    retval += _say10000(number % 10000)

    if (minus):
        retval = _phrase_noop("負") + " " + retval

    return retval.strip()

def _say10000(number):
    retval = ""

    num = number % 10
    num_tens = int(number / 10) % 10
    num_hundreds = int(number / 100) % 10
    num_thousands = int(number / 1000) % 10

    if (num_thousands > 0):
        retval += ONES[num_thousands] + " " + _phrase_noop("千") + " "

    if (num_hundreds > 0):
        retval += ONES[num_hundreds] + " " + _phrase_noop("百") + " "

    if (num_tens > 0):
        if (num_tens == 1):
            retval += _phrase_noop("十") + " "
        else:
            retval += ONES[num_tens] + " " + _phrase_noop("十") + " "

    if (num > 0):
        retval += ONES[num]

    return retval.rstrip()

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (not i.isdigit()):
            pass
        retval += ONES[int(i)] + " "
    
    return retval.rstrip()

def sayDuration(seconds, say_hours, say_minutes, say_seconds, flags):
    retval = ""
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
        retval += _say10000(hours) + " " + _phrase_noop("个小时") + " "

    if (minutes > 0):
        retval += _say10000(minutes) + " " + _phrase_noop("分钟") + " "

    if (s > 0 or seconds == 0):
        retval += _say10000(s) + " " + _phrase_noop("秒") + " "

    return retval.strip()

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    # TODO
    return retval.rstrip()

if (__name__ == "__main__"):
    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100, 1000, 10000, 100000, 1000000,
             10000000, 100000000, 1000000000,
             12, 20, 23, 45, 78, 98, 123, 234, 345, 678, 876, 1234, 2345, 12345, 12345678, 123456789,
             600, 800, 8000,
             7, 70, 700, 7000, 70000, 700000000,
             -1):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    for i in (0, 1, 23, 466, 78910, 11, 12, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, None)))
