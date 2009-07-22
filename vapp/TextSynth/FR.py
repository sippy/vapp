#!/usr/local/bin/python
# -*- coding: ISO-8859-1 -*-
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

MASCULINE = 1
FEMININE = 2

def _phrase_noop(str):
    return unicode(str, 'ISO-8859-1')

ONES_M = [
	_phrase_noop("zéro"),
	_phrase_noop("un"),
	_phrase_noop("deux"),
	_phrase_noop("trois"),
	_phrase_noop("quatre"),
	_phrase_noop("cinq"),
	_phrase_noop("six"),
	_phrase_noop("sept"),
	_phrase_noop("huit"),
	_phrase_noop("neuf"),
	_phrase_noop("dix"),
	_phrase_noop("onze"),
	_phrase_noop("douze"),
	_phrase_noop("treize"),
	_phrase_noop("quatorze"),
	_phrase_noop("quinze"),
	_phrase_noop("seize"),
	_phrase_noop("dix-sept"),
	_phrase_noop("dix-huit"),
	_phrase_noop("dix-neuf"),
	_phrase_noop("vingt"),
	_phrase_noop("vingt et un"),
	_phrase_noop("vingt-deux"),
	_phrase_noop("vingt-trois"),
	_phrase_noop("vingt-quatre"),
	_phrase_noop("vingt-cinq"),
	_phrase_noop("vingt-six"),
	_phrase_noop("vingt-sept"),
	_phrase_noop("vingt-huit"),
	_phrase_noop("vingt-neuf")
	]

ONES_F = [
	_phrase_noop("zéro"),
	_phrase_noop("une"),
	_phrase_noop("deux"),
	_phrase_noop("trois"),
	_phrase_noop("quatre"),
	_phrase_noop("cinq"),
	_phrase_noop("six"),
	_phrase_noop("sept"),
	_phrase_noop("huit"),
	_phrase_noop("neuf"),
	_phrase_noop("dix"),
	_phrase_noop("onze"),
	_phrase_noop("douze"),
	_phrase_noop("treize"),
	_phrase_noop("quatorze"),
	_phrase_noop("quinze"),
	_phrase_noop("seize"),
	_phrase_noop("dix-sept"),
	_phrase_noop("dix-huit"),
	_phrase_noop("dix-neuf"),
	_phrase_noop("vingt"),
	_phrase_noop("vingt et une"),
	_phrase_noop("vingt-deux"),
	_phrase_noop("vingt-trois"),
	_phrase_noop("vingt-quatre"),
	_phrase_noop("vingt-cinq"),
	_phrase_noop("vingt-six"),
	_phrase_noop("vingt-sept"),
	_phrase_noop("vingt-huit"),
	_phrase_noop("vingt-neuf")
	]

TENS = [
	_phrase_noop("trente"),
	_phrase_noop("quarante"),
	_phrase_noop("cinquante"),
	_phrase_noop("soixante"),
	_phrase_noop("soixante-dix"),
	_phrase_noop("quatre-vingt"),
	_phrase_noop("quatre-vingt-dix")
	]

TENS_PLUS_ONE_M = [
	_phrase_noop("trente et un"),
	_phrase_noop("quarante et un"),
	_phrase_noop("cinquante et un"),
	_phrase_noop("soixante et un"),
	_phrase_noop("soixante et onze"),
	_phrase_noop("quatre-vingt-un"),
	_phrase_noop("quatre-vingt-onze")
	]

TENS_PLUS_ONE_F = [
	_phrase_noop("trente et une"),
	_phrase_noop("quarante et une"),
	_phrase_noop("cinquante et une"),
	_phrase_noop("soixante et une"),
	_phrase_noop("soixante et onze"),
	_phrase_noop("quatre-vingt-un"),
	_phrase_noop("quatre-vingt-onze")
	]

MONTHS = [ 
	_phrase_noop("janvier"),
	_phrase_noop("février"),
	_phrase_noop("mars"),
	_phrase_noop("avril"),
	_phrase_noop("mai"),
	_phrase_noop("juin"),
	_phrase_noop("juillet"),
	_phrase_noop("août"),
	_phrase_noop("septembre"),
	_phrase_noop("octobre"),
	_phrase_noop("novembre"),
	_phrase_noop("décembre")
	]

def __say_number(number, gender = MASCULINE):
    retval = ""
    if gender == MASCULINE:
        ONES = ONES_M
        TENS_PLUS_ONE = TENS_PLUS_ONE_M
    else:
        ONES = ONES_F
        TENS_PLUS_ONE = TENS_PLUS_ONE_F
    if (number == 0):
        return _phrase_noop("zéro") + " "
    if (number < 30):
        return ONES[number] + " "
    tens = int(number / 10)
    ones = number % 10
    if (ones == 1):
        return TENS_PLUS_ONE[tens - 3] + " "
    elif (ones == 0):
        return TENS[tens - 3]
    if (number > 70 and number < 80):
        return TENS[tens - 4] + " " + ONES[10 + ones] + " "
    if (number > 90):
        return TENS[tens - 4] + " " + ONES[10 + ones] + " "
    retval = TENS[tens - 3] + " "
    if ones > 0:
        retval += ONES[ones] + " "
    return retval

def sayNumber(number, ordinal, flags):
    retval = ""
    minus = False
    gender = MASCULINE
    if (flags != None and 'F' in flags):
        gender = FEMININE
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("moins que sans un milliard")
        else:
            retval = _phrase_noop("plus d'un milliard")
    else:
        if (minus):
            retval = _phrase_noop("moins") + " "
        num = number % 100
        num_hundreds = int((number % 1000) / 100)
        num_thousands = int(number / 1000) % 100
        num_hundred_thousands = int(number / 100000) % 10
        num_millions = int(number / 1000000) % 100
        num_hundred_millions = int(number / 100000000) % 10

        # millions
        if (num_hundred_millions > 0):
            if (num_hundred_millions == 1):
                retval += _phrase_noop("cent") + " "
            else:
                retval += __say_number(num_hundred_millions)
                retval += _phrase_noop("cents") + " "
        if (num_millions > 0):
            retval += __say_number(num_millions)
        if ((num_hundred_millions + num_millions) > 0):
            if (num_hundred_millions == 0 and num_millions == 1):
                retval += _phrase_noop("million") + " "
            else:
                retval += _phrase_noop("millions") + " "

        # thousands
        if (num_hundred_thousands > 0):
            if (num_hundred_thousands == 1):
                retval += _phrase_noop("cent") + " "
            else:
                retval += __say_number(num_hundred_thousands)
                retval += _phrase_noop("cents") + " "
        if ((num_hundred_thousands + num_thousands) > 0):
            if (num_hundred_thousands == 0 and num_thousands == 1):
                retval += _phrase_noop("mille") + " "
            else:
                retval += __say_number(num_thousands)
                retval += _phrase_noop("milliers") + " "

        # the rest
        if (num_hundreds > 0):
            if (num_hundreds == 1):
                retval += _phrase_noop("cent") + " "
            else:
                retval += __say_number(num_hundreds)
                retval += _phrase_noop("cents") + " "
        if (num > 0 or number == 0):
            retval += __say_number(num, gender)

    return retval.rstrip()

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if i.isdigit():
            retval += ONES_M[int(i)] + " "
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
        retval += sayNumber(hours, False, "F") + " "
        if (hours == 1):
            retval += _phrase_noop("heure") + " "
        else:
            retval += _phrase_noop("heures") + " "
    if (minutes > 0):
        retval += sayNumber(minutes, False, "F") + " "
        if (minutes == 1):
            retval += _phrase_noop("minute") + " "
        else:
            retval += _phrase_noop("minutes") + " "
    if (s > 0 or seconds == 0):
        retval += sayNumber(s, False, "F") + " "
        if (s == 1):
            retval += _phrase_noop("seconde") + " "
        else:
            retval += _phrase_noop("secondes") + " "
    return retval.rstrip()

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    now = datetime.datetime.now(date_time.tzinfo)

    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("aujourd'hui") + " " 	# today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("hier") + " " 		# yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("demain") + " "		# tomorrow
        else:
            if (date_time.day == 1):
                retval += _phrase_noop("premier") + " "
            else:
                retval += sayNumber(date_time.day, False, "") + " "
            retval += MONTHS[date_time.month - 1] + " "
            retval += sayNumber(date_time.year, False, "") + " "

    if (say_time):
        retval += _phrase_noop("à") + " "
        hour = date_time.hour
        retval += sayNumber(hour, False, "") + " "
        minute = date_time.minute
        if (minute > 0):
            retval += sayNumber(minute, False, "") + " "
        if (say_seconds and date_time.second != 0):
            secs = date_time.second
            retval += _phrase_noop("et") + " "
            retval += sayNumber(secs, False, "") + " "
            if (secs == 1):
                retval += _phrase_noop("seconde") + " "
            else:
                retval += _phrase_noop("secondes") + " "
    return retval.rstrip()

if (__name__ == "__main__"):
    print "########## French numbers ###########"
    for i in range(0, 100):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    for i in (123, 234, 345, 678, 876, 
             1234, 2345, 12345, 456789, 1234567, 12345678, 234567891, 3456789012, -1000000123
             -1, -12):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    val = "1234560987"
    res = sayDigits(val, None)
    print "########## Digit string ###########"
    print("%s: %s" % (val, res))
    print "########## French durations ###########"
    for i in (0, 1, 23, 466, 78912, 11, 14, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, None)))
    print "########## French date and time ###########"
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
