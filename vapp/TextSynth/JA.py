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

def _phrase_noop(s):
    return s

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

HUNDREDS = [
	"",                     # placeholder
	_phrase_noop("百"),	# 100
	_phrase_noop("二百"),	# 200
	_phrase_noop("三百"),	# 300
	_phrase_noop("四百"),	# 400
	_phrase_noop("五百"),	# 500
	_phrase_noop("六百"),	# 600
	_phrase_noop("七百"),	# 700
	_phrase_noop("八百"),	# 800
	_phrase_noop("九百")	# 900
	]

THOUSANDS = [
	"",                     # placeholder
	_phrase_noop("千"),	# 1000
	_phrase_noop("二千"),	# 2000
	_phrase_noop("三千"),	# 3000
	_phrase_noop("四千"),	# 4000
	_phrase_noop("五千"),	# 5000
	_phrase_noop("六千"),	# 6000
	_phrase_noop("七千"),	# 7000
	_phrase_noop("八千"),	# 8000
	_phrase_noop("九千")	# 9000
	]

THOUSAND_HOURS = [
	"",                     # placeholder
	_phrase_noop("千時"),	# 1000
	_phrase_noop("二千時"),	# 2000
	_phrase_noop("三千時"),	# 3000
	_phrase_noop("四千時"),	# 4000
	_phrase_noop("五千時"),	# 5000
	_phrase_noop("六千時"),	# 6000
	_phrase_noop("七千時"),	# 7000
	_phrase_noop("八千時"),	# 8000
	_phrase_noop("九千時")	# 9000
	]

HUNDRED_HOURS = [
	"",                     # placeholder
	_phrase_noop("百時"),	# 100
	_phrase_noop("二百時"),	# 200
	_phrase_noop("三百時"),	# 300
	_phrase_noop("四百時"),	# 400
	_phrase_noop("五百時"),	# 500
	_phrase_noop("六百時"),	# 600
	_phrase_noop("七百時"),	# 700
	_phrase_noop("八百時"),	# 800
	_phrase_noop("九百時")	# 900
	]

TEN_HOURS = [
	"",  	                # placeholder
	_phrase_noop("十時"),	# 10
	_phrase_noop("二十時"),	# 20
	_phrase_noop("三十時"),	# 30
	_phrase_noop("四十時"),	# 40
	_phrase_noop("五十時"),	# 50
	_phrase_noop("六十時"),	# 60
	_phrase_noop("七十時"),	# 70
	_phrase_noop("八十時"),	# 80
	_phrase_noop("九十時")	# 90
	]

HOURS = [
	"",  	                # placeholder
	_phrase_noop("一時"),	# 1
	_phrase_noop("二時"),	# 2
	_phrase_noop("三時"),	# 3
	_phrase_noop("四時"),	# 4
	_phrase_noop("五時"),	# 5
	_phrase_noop("六時"),	# 6
	_phrase_noop("七時"),	# 7
	_phrase_noop("八時"),	# 8
	_phrase_noop("九時")	# 9
	]

THOUSAND_MINUTES = [
	"",                     # placeholder
	_phrase_noop("千分"),	# 1000
	_phrase_noop("二千分"),	# 2000
	_phrase_noop("三千分"),	# 3000
	_phrase_noop("四千分"),	# 4000
	_phrase_noop("五千分"),	# 5000
	_phrase_noop("六千分"),	# 6000
	_phrase_noop("七千分"),	# 7000
	_phrase_noop("八千分"),	# 8000
	_phrase_noop("九千分")	# 9000
	]

HUNDRED_MINUTES = [
	"",                     # placeholder
	_phrase_noop("百分"),	# 100
	_phrase_noop("二百分"),	# 200
	_phrase_noop("三百分"),	# 300
	_phrase_noop("四百分"),	# 400
	_phrase_noop("五百分"),	# 500
	_phrase_noop("六百分"),	# 600
	_phrase_noop("七百分"),	# 700
	_phrase_noop("八百分"),	# 800
	_phrase_noop("九百分")	# 900
	]

TEN_MINUTES = [
	"",  	                # placeholder
	_phrase_noop("十分"),	# 10
	_phrase_noop("二十分"),	# 20
	_phrase_noop("三十分"),	# 30
	_phrase_noop("四十分"),	# 40
	_phrase_noop("五十分"),	# 50
	_phrase_noop("六十分"),	# 60
	_phrase_noop("七十分"),	# 70
	_phrase_noop("八十分"),	# 80
	_phrase_noop("九十分")	# 90
	]

MINUTES = [
	"",  	                # placeholder
	_phrase_noop("一分"),	# 1
	_phrase_noop("二分"),	# 2
	_phrase_noop("三分"),	# 3
	_phrase_noop("四分"),	# 4
	_phrase_noop("五分"),	# 5
	_phrase_noop("六分"),	# 6
	_phrase_noop("七分"),	# 7
	_phrase_noop("八分"),	# 8
	_phrase_noop("九分")	# 9
	]

THOUSAND_SECONDS = [
	"",                     # placeholder
	_phrase_noop("千秒"),	# 1000
	_phrase_noop("二千秒"),	# 2000
	_phrase_noop("三千秒"),	# 3000
	_phrase_noop("四千秒"),	# 4000
	_phrase_noop("五千秒"),	# 5000
	_phrase_noop("六千秒"),	# 6000
	_phrase_noop("七千秒"),	# 7000
	_phrase_noop("八千秒"),	# 8000
	_phrase_noop("九千秒")	# 9000
	]

HUNDRED_SECONDS = [
	"",                     # placeholder
	_phrase_noop("百秒"),	# 100
	_phrase_noop("二百秒"),	# 200
	_phrase_noop("三百秒"),	# 300
	_phrase_noop("四百秒"),	# 400
	_phrase_noop("五百秒"),	# 500
	_phrase_noop("六百秒"),	# 600
	_phrase_noop("七百秒"),	# 700
	_phrase_noop("八百秒"),	# 800
	_phrase_noop("九百秒")	# 900
	]

TEN_SECONDS = [
	"",  	                # placeholder
	_phrase_noop("十秒"),	# 10
	_phrase_noop("二十秒"),	# 20
	_phrase_noop("三十秒"),	# 30
	_phrase_noop("四十秒"),	# 40
	_phrase_noop("五十秒"),	# 50
	_phrase_noop("六十秒"),	# 60
	_phrase_noop("七十秒"),	# 70
	_phrase_noop("八十秒"),	# 80
	_phrase_noop("九十秒")	# 90
	]

SECONDS = [
	_phrase_noop("零秒"),  	# 0
	_phrase_noop("一秒"),	# 1
	_phrase_noop("二秒"),	# 2
	_phrase_noop("三秒"),	# 3
	_phrase_noop("四秒"),	# 4
	_phrase_noop("五秒"),	# 5
	_phrase_noop("六秒"),	# 6
	_phrase_noop("七秒"),	# 7
	_phrase_noop("八秒"),	# 8
	_phrase_noop("九秒")	# 9
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

#        num = int(number / 100000000)
#        if (num == 4):
#            retval += _phrase_noop("四億") # 400000000
#        elif (num == 7):
#            retval += _phrase_noop("七億") # 700000000
#        elif (num > 0):
#            retval += _say10000(num) + " " + _phrase_noop("億") + " "

    num = int(number / 10000) % 10000
    if (num == 4):
        retval += _phrase_noop("四万") # 40000
    if (num == 7):
        retval += _phrase_noop("七万") # 70000
    elif (num > 0):
        retval += _say10000(num) + " " + _phrase_noop("万") + " "

    retval += _say10000(number % 10000)

#        if (minus):
#            retval = _phrase_noop("マイナス") + " " + retval

    return retval.strip()

def _say10000(number):
    retval = ""

    num = number % 10
    num_tens = int(number / 10) % 10
    num_hundreds = int(number / 100) % 10
    num_thousands = int(number / 1000) % 10

    if (num_thousands > 0):
        retval += THOUSANDS[num_thousands] + " "

    if (num_hundreds > 0):
        retval += HUNDREDS[num_hundreds] + " "

    if (num_tens > 0):
        if (num_tens == 1):
            retval += _phrase_noop("十") + " "
        elif (num_tens == 4):
            retval +=  _phrase_noop("四十") + " " # 40
        elif (num_tens == 7):
            retval +=  _phrase_noop("七十") + " " # 70
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
        num = hours % 10
        tens = int(hours / 10) % 10
        hundreds = int(hours / 100) % 10
        thousands = int(hours / 1000) % 10

        if (thousands > 0):
            if ((num + tens + hundreds) == 0):
                retval += THOUSAND_HOURS[thousands] + " "
            else:
                retval += _say10000(thousands * 1000) + " "
        if (hundreds > 0):
            if ((num + tens) == 0):
                retval += HUNDRED_HOURS[hundreds] + " "
            else:
                retval += _say10000(hundreds * 100) + " "
        if (tens > 0):
            if (num == 0):
                retval += TEN_HOURS[tens] + " "
            else:
                retval += _say10000(tens * 10) + " "
        if (num > 0):
            retval += HOURS[num] + " "

    if (minutes > 0):
        num = minutes % 10
        tens = int(minutes / 10) % 10
        hundreds = int(minutes / 100) % 10
        thousands = int(minutes / 100) % 10

        if (thousands > 0):
            if ((num + tens + hundreds) == 0):
                retval += THOUSAND_MINUTES[thousands] + " "
            else:
                retval += _say10000(thousands * 1000) + " "
        if (hundreds > 0):
            if ((num + tens) == 0):
                retval += HUNDRED_MINUTES[hundreds] + " "
            else:
                retval += _say10000(hundreds * 100) + " "
        if (tens > 0):
            if (num == 0):
                retval += TEN_MINUTES[tens] + " "
            else:
                retval += _say10000(tens * 10) + " "
        if (num > 0):
            retval += MINUTES[num] + " "

    if (s > 0 or seconds == 0):
        num = s % 10
        tens = int(s / 10) % 10
        hundreds = int(s / 100) % 10
        thousands = int(s / 100) % 10

        if (thousands > 0):
            if ((num + tens + hundreds) == 0):
                retval += THOUSAND_SECONDS[thousands] + " "
            else:
                retval += _say10000(thousands * 1000) + " "
        if (hundreds > 0):
            if ((num + tens) == 0):
                retval += HUNDRED_SECONDS[hundreds] + " "
            else:
                retval += _say10000(hundreds * 100) + " "
        if (tens > 0):
            if (num == 0):
                retval += TEN_SECONDS[tens] + " "
            else:
                retval += _say10000(tens * 10) + " "
        if (num > 0 or seconds == 0):
            retval += SECONDS[num] + " "

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
             -1, 10001):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    for i in (0, 1, 23, 466, 78910, 11, 12, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, True, None)))
