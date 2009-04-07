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

ONES = [
	_phrase_noop("զրո"),  		# 0
	_phrase_noop("մեկ"),		# 1
	_phrase_noop("երկու"),		# 2
	_phrase_noop("երեք"),		# 3
	_phrase_noop("չորս"),		# 4
	_phrase_noop("հինգ"),		# 5
	_phrase_noop("վեց"),		# 6
	_phrase_noop("յոթ"),		# 7
	_phrase_noop("ութ"),		# 8
	_phrase_noop("ինը"),		# 9
	_phrase_noop("տաս"),		# 10
	_phrase_noop("տասնմեկ"),		# 11
	_phrase_noop("տասներկու"),	# 12
	_phrase_noop("տասներեք"),	# 13
	_phrase_noop("տասնըչորս"),	# 14
	_phrase_noop("տասնըհինգ"),	# 15
	_phrase_noop("տասնըվեց"),	# 16
	_phrase_noop("տասնըյոթ"),	# 17
	_phrase_noop("տասնութ"),		# 18
	_phrase_noop("տասնինը"),		# 19
	]


TENS = [
	_phrase_noop("քսան"),		# 20
	_phrase_noop("երեսուն"),		# 30
	_phrase_noop("քառասուն"),	# 40
	_phrase_noop("հիսուն"),		# 50
	_phrase_noop("վաթսուն"),		# 60
	_phrase_noop("յոթանասուն"),	# 70
	_phrase_noop("ութսուն"),		# 80
	_phrase_noop("իննսուն")		# 90
	]	

MONTHS = [ 
	_phrase_noop("հունվարի"), 	# January's
	_phrase_noop("փետրվարի"),	# February's
	_phrase_noop("մարտի"),		# March
	_phrase_noop("ապրիլի"),		# April
	_phrase_noop("մայիսի"),		# May's
	_phrase_noop("հունիսի"),		# June
	_phrase_noop("հուլիսի"),		# July's
	_phrase_noop("оգոստոսի"),	# August
	_phrase_noop("սեպտեմբերի"),	# September
	_phrase_noop("հոկտեմբերի"),	# October
	_phrase_noop("նոյեմբերի"),	# November
	_phrase_noop("դեկտեմբերի")	# December
	]
#
# Full hours and minutes in phrases like "at <time>"
#
ONES_AT = [
	_phrase_noop("զրոին"),  		# 0
	_phrase_noop("մեկին"),		# 1
	_phrase_noop("երկուսին"),		# 2
	_phrase_noop("երեքին"),		# 3
	_phrase_noop("չորսին"),		# 4
	_phrase_noop("հինգին"),		# 5
	_phrase_noop("վեցին"),		# 6
	_phrase_noop("յոթին"),		# 7
	_phrase_noop("ութին"),		# 8
	_phrase_noop("իննին"),		# 9
	_phrase_noop("տասին"),		# 10
	_phrase_noop("տասնմեկին"),	# 11
	_phrase_noop("տասներկուսին"),	# 12
	_phrase_noop("տասներեքին"),	# 13
	_phrase_noop("տասնըչորսին"),	# 14
	_phrase_noop("տասնըհինգին"),	# 15
	_phrase_noop("տասնըվեցին"),	# 16
	_phrase_noop("տասնըյոթին"),	# 17
	_phrase_noop("տասնութին"),	# 18
	_phrase_noop("տասնիննին")	# 19
	]

#
# Hours when there minutes in the pronounced time
#
ONES_AT2 = [
	_phrase_noop("զրո"),  		# 0
	_phrase_noop("մեկ"),		# 1
	_phrase_noop("երկուս"),		# 2
	_phrase_noop("երեք"),		# 3
	_phrase_noop("չորս"),		# 4
	_phrase_noop("հինգ"),		# 5
	_phrase_noop("վեց"),		# 6
	_phrase_noop("յոթ"),		# 7
	_phrase_noop("ութ"),		# 8
	_phrase_noop("ինն"),		# 9
	_phrase_noop("տաս"),		# 10
	_phrase_noop("տասնմեկ"),		# 11
	_phrase_noop("տասներկուս"),	# 12
	_phrase_noop("տասներեք"),	# 13
	_phrase_noop("տասնըչորս"),	# 14
	_phrase_noop("տասնըհինգ"),	# 15
	_phrase_noop("տասնըվեց"),	# 16
	_phrase_noop("տասնըյոթ"),	# 17
	_phrase_noop("տասնութ"),		# 18
	_phrase_noop("տասնինն"),		# 19
	]

TENS_AT = [
	_phrase_noop("քսանին"),		# 20
	_phrase_noop("երեսունին"),	# 30
	_phrase_noop("քառասունին"),	# 40
	_phrase_noop("հիսունին"),		# 50
	_phrase_noop("վաթսունին"),	# 60
	_phrase_noop("յոթանասունին"),	# 70
	_phrase_noop("ութսունին"),	# 80
	_phrase_noop("իննսունին")		# 90
	]

def sayNumber(number, ordinal, flags):
    retval = ""
    minus = False
#	at_flag = False

#	if ('A' in flags):
#	    at_flag = True

    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("մինուս մեկ միլիարդից պակաս") # less than minus one billion
        else:
            retval = _phrase_noop("մեկ միլիարդից ավելի") # more than one billion
    else:
        if (minus):
            retval = _phrase_noop("մինուս") + " "

        num = number % 100
        num_hundreds = int((number % 1000) / 100)
        num_thousands = int(number / 1000) % 100
        num_hundred_thousands = int(number / 100000) % 10
        num_millions = int(number / 1000000) % 100
        num_hundred_millions = int(number / 100000000) % 10

        # millions
        if (num_hundred_millions > 0):
            if (num_hundred_millions > 1):
                    retval += __say_number(num_hundred_millions, False)
            retval += _phrase_noop("հարյուր") + " "
        if (num_millions > 1):
            retval += __say_number(num_millions, False)
        if ((num_hundred_millions + num_millions) > 0):
            retval += _phrase_noop("միլիոն") + " "

        # thousands
        if (num_hundred_thousands > 0):
            if (num_hundred_thousands > 1):
                    retval += __say_number(num_hundred_thousands, False)
            retval += _phrase_noop("հարյուր") + " "
        if (num_thousands > 1):
            retval += __say_number(num_thousands, False)
        if ((num_hundred_thousands + num_thousands) > 0):
            retval += _phrase_noop("հազար") + " "

        # the rest
        if (num_hundreds > 0):
            if (num_hundreds > 1):
                retval += __say_number(num_hundreds, False)
            retval += _phrase_noop("հարյուր") + " "
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal)

    return retval.rstrip()

def __say_number(number, ordinal, at_flag = 0):
    retval = ""
    if (number < 20):
        if (at_flag == 1):
            retval = ONES_AT[number] + " "
        elif (at_flag == 2):
            retval = ONES_AT2[number] + " "
        else:
            retval = ONES[number] + " "
        return retval
    tens = int(number / 10)
    ones = number % 10
    if (tens > 0):
        if (ones == 0 and at_flag != 0):
            retval = TENS_AT[tens - 2] + " "
        else:
            retval = TENS[tens - 2] + " "
    if (ones > 0):
        if (at_flag == 1):
            retval += ONES_AT[ones] + " "
        elif (at_flag == 2):
            retval += ONES_AT[ones] + " "
        else:
            retval += ONES[ones] + " "
    return retval

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (not i.isdigit()):
            pass
        retval += ONES[int(i)] + " "
    
    return retval.rstrip()

def sayDuration(seconds, say_hours, say_minutes, flags):
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
    if (hours > 0):
        retval += sayNumber(hours, False, None)
        retval += " " + _phrase_noop("ժամ")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(minutes, False, None)
        retval += " " + _phrase_noop("րոպե")
    if (s > 0 or seconds == 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(s, False, None)
        retval += " " + _phrase_noop("վայրկյան")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    now = datetime.datetime.now(date_time.tzinfo)
    #
    # Date
    #
    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("այսօր") + " "	# today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("երեկ") + " "	# yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("վաղը") + " " 	# tomorrow
        else:
            if (now.year != date_time.year):
                retval += sayNumber(date_time.year, False, "") + " "
                retval += _phrase_noop("թվականի") + " " # "year"
            retval += MONTHS[date_time.month - 1] + " "
            retval += __say_number(date_time.day, False, True)
    #
    # Time
    #
    if (say_time):
        hour = date_time.hour
        minute = date_time.minute
        retval += _phrase_noop("ժամը") + " "

        if (minute > 0):
            retval += __say_number(hour, False, 2)
            retval += _phrase_noop("անց") + " " # ~past
            retval += __say_number(minute, False, 1)
        else:
            retval += __say_number(hour, False, 1)

    return retval.rstrip()

if (__name__ == "__main__"):
    print "########## Armenian numbers ###########"
    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 45, 78, 98, 123, 234, 345, 678, 876, 
             1234, 2345, 12345, 456789, 1234567, 12345678, 234567891, 3456789012, -1000000123
             -1, -12):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    print "########## Armenian durations ###########"
    for i in (0, 1, 23, 466, 78912, 11, 14, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, None)))
    print "########## Armenian date and time ###########"
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
