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

def _phrase_noop(str):
    return unicode(str, 'utf-8')

MONTHS = [
    # Jan
    _phrase_noop("كانون ثاني"),
    # Feb
    _phrase_noop("شباط"),
    # Mar
    _phrase_noop("آذار"),
    # Apr
    _phrase_noop("نيسان"),
    # May
    _phrase_noop("أيار"),
    # Jun
    _phrase_noop("حزيران"),
    # Jul
    _phrase_noop("تموز"),
    # Aug
    _phrase_noop("آب"),
    # Sep
    _phrase_noop("أيلول"),
    # Oct
    _phrase_noop("تشرين أول"),
    # Nov
    _phrase_noop("تشرين ثاني"),
    # Dec
    _phrase_noop("كانون أول")
    ]

ONES = [
	# 0
	_phrase_noop("صفر"),
	# 1
	_phrase_noop("واحد"),
	# 2
	_phrase_noop("إثنان"),
	# 3
	_phrase_noop("ثلاثة"),
	# 4
	_phrase_noop("أربعة"),
	# 5
	_phrase_noop("خمسة"),
	# 6
	_phrase_noop("ستة"),
	# 7
	_phrase_noop("سبعة"),
	# 8
	_phrase_noop("ثمانية"),
	# 9
	_phrase_noop("تسعة"),
	# 10
	_phrase_noop("عشرة"),
	# 11
	_phrase_noop("إحدى عشر"),
	# 12
	_phrase_noop("إثنا عشر"),
	# 13
	_phrase_noop("ثلاثة عشر"),
	# 14
	_phrase_noop("أربعة عشر"),
	# 15
	_phrase_noop("خمسة عشر"),
	# 16
	_phrase_noop("ستة عشر"),
	# 17
	_phrase_noop("سبعة عشر"),
	# 18
	_phrase_noop("ثمانية عشر"),
	# 19
	_phrase_noop("تسعة عشر")
	]

ONES_ORDINAL = [
	]

TENS = [
 	# 20
	_phrase_noop("عشرون"),
 	# 30
	_phrase_noop("ثلاثون"),
 	# 40
	_phrase_noop("أربعون"),
 	# 50
	_phrase_noop("خمسون"),
 	# 60
	_phrase_noop("الستون"),
 	# 70
	_phrase_noop("سبعون"),
 	# 80
	_phrase_noop("ثمانون"),
 	# 90
	_phrase_noop("تسعون")
	]

HUNDREDS = [
    # 100
    _phrase_noop("مائة"),
    # 200
    _phrase_noop("مائتان"),
    # 300
    _phrase_noop("ثلاث مائة"),
    # 400
    _phrase_noop("أربعمائة"),
    # 500
    _phrase_noop("وخمسمائة"),
    # 600
    _phrase_noop("ستمائة"),
    # 700
    _phrase_noop("سبعمائة"),
    # 800
    _phrase_noop("ثمانمائة"),
    # 900
    _phrase_noop("تسعمائة"),
    ]

def sayNumber(number, ordinal, flags):
    retval = unicode("")
    minus = False

    if number == 0:
        return 	_phrase_noop("صفر")

    if (number < 0):
        number = -number
        minus = True

    if (number >= 1000000):
        if (minus):
            retval = _phrase_noop("أقل من ناقص واحد مليون") # less than minus one million
        else:
            retval = _phrase_noop("أكثر من مليون واحد") # more than one million
        return retval

    if (minus):
        retval = _phrase_noop("ناقص") + " "
    num = number % 100
    num_hundreds = int((number % 1000) / 100)
    num_thousands = int(number / 1000) % 100
    num_hundred_thousands = int(number / 100000) % 10
    num_started = False

    # thousands
    if (num_hundred_thousands > 0):
        retval += HUNDREDS[num_hundred_thousands] + " "
        num_started = True

    if (num_thousands > 0):
        if num_started:
            retval += _phrase_noop("و") + " "
        num_started = True
        retval += __say_number(num_thousands) + " "

    if (num_hundred_thousands + num_thousands > 0):
        retval += _phrase_noop("الف") + " " # thousand

    if (num_hundreds > 0):
        if num_started:
            retval += _phrase_noop("و") + " "
        num_started = True
        retval += HUNDREDS[num_hundred_thousands] + " "

    if (num > 0):
        if num_started:
            retval += _phrase_noop("و") + " "
        retval += __say_number(num)

    return retval.rstrip()

def __say_number(number):
    retval = unicode("")
    if (number < 20):
        return ONES[number] + " "
    tens = int(number / 10)
    ones = number % 10
    if (ones > 0):
        retval += ONES[ones] + " "
    if tens > 0:
        if len(retval) > 0:
            retval += _phrase_noop("و") + " "
        retval = TENS[tens - 2] + " "
    return retval

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (i.isdigit()):
            retval += ONES[int(i)] + " "
    
    return retval.rstrip()

def sayDuration(seconds, say_hours, say_minutes, flags):
    retval = unicode("")
    s = seconds
    hours = 0
    minutes = 0
    if (say_hours):
        hours = int(s / 3600)
        s -= hours * 3600
    if (say_minutes):
        minutes = int((s / 60) % 60)
        s -= minutes * 60
    s = int(s % 60)
    if (hours > 0):
        if hours == 2:
            retval += _phrase_noop("ساعتين")
        else:
            retval += sayNumber(hours, False, None) + " "
            retval += _phrase_noop("ساعة") + " "
    if (minutes > 0):
        if (retval != ""):
            retval += _phrase_noop("و") + " "
        if minutes == 2:
            retval += _phrase_noop("دقيقتين") + " "
        else:
            retval += sayNumber(minutes, False, None)
            retval += " " + _phrase_noop("دقيقة")
    if (s > 0):
        if (retval != ""):
            retval += _phrase_noop("و") + " "
        if s == 2:
            retval += _phrase_noop("ثانيتين") + " "
        else:
            retval += sayNumber(s, False, None)
            retval += " " + _phrase_noop("ثوان")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    now = datetime.datetime.now(date_time.tzinfo)

    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("اليوم") + " " # today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("أمس") + " " # yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("غدا") + " " # tomorrow
        else:
            retval += MONTHS[date_time.month - 1] + " "
            retval += sayNumber(date_time.day, True, "") + " "
            yh = int(date_time.year / 100)
            yl = date_time.year % 100
            retval += sayNumber(date_time.year, False, "") + " "

    if (say_time):
        suffix = _phrase_noop("صباحاً") # AM
        hour = date_time.hour
        if (hour >= 12):
            hour -= 12
            suffix = _phrase_noop("مساءً") # PM
        if (hour == 0):
            hour = 12
        retval += sayNumber(hour, False, "") + " "
        minute = date_time.minute
        if (minute > 0):
            retval += sayNumber(minute, False, "") + " "
        retval += suffix
    return retval.rstrip()

if (__name__ == "__main__"):
    print "########## Arabic numbers ###########"
    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 45, 78, 98, 123, 234, 345, 678, 876, 
             1234, 2345, 12345, 456789, 1234567, 12345678, -1000000123
             -1, -12):
        print("%d:\n %s" % (i, sayNumber(i, False, "")))
    print "########## Arabic durations ###########"
    for i in (1, 23, 466, 78912, 11, 14, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d:\n %s" % (h, m, s, sayDuration(i, True, True, None)))
    print "########## Arabic date and time ###########"
    tmp = datetime.datetime.now()
    now = datetime.datetime(tmp.year, tmp.month, tmp.day, tmp.hour, tmp.minute, tmp.second)
    for i in ((now, '(today)'), 
              (now - datetime.timedelta(1), '(yesterday)'),
              (now + datetime.timedelta(1), '(tomorrow)'),
              (datetime.datetime(1970, 1, 20, 12, 0), ''),
              (datetime.datetime(1996, 2, 11, 0, 0), ''),
              (datetime.datetime(2006, 3, 11, 9, 45), ''),
              (datetime.datetime(1996, 4, 11, 18, 22), ''),
              (datetime.datetime(1996, 5, 11, 9, 0), ''),
              (datetime.datetime(1996, 6, 11, 9, 9), ''),
              (datetime.datetime(1996, 7, 11, 9, 19), ''),
              (datetime.datetime(1996, 8, 11, 9, 12), ''),
              (datetime.datetime(1996, 9, 11, 9, 23), ''),
              (datetime.datetime(1996, 10, 11, 9, 2), ''),
              (datetime.datetime(1996, 11, 11, 14, 0), ''),
              (datetime.datetime(1996, 12, 11, 2, 46), ''),
        ):
        print("%s - %s %s" % (str(i[0]), sayDatetime(i[0], True, True, True, None), i[1]))
