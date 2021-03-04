#!/usr/local/bin/python
# -*- coding: utf-8 -*-
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

# Georgian language module

import datetime

def _phrase_noop(str):
    return unicode(str, 'utf-8')

GENDER_FEMININE	    = 0
GENDER_MASCULINE    = 1
GENDER_NONE	    = 2

ONES_START = [
	_phrase_noop("ნულოვან"),       # 0
	_phrase_noop("ერთ"),       # 1
	_phrase_noop("ორ"),        # 2
	_phrase_noop("სამ"),       # 3
	_phrase_noop("ოთხ"),       # 4
	_phrase_noop("ხუთ"),       # 5
	_phrase_noop("ექვს"),      # 6
	_phrase_noop("შვიდ"),      # 7
	_phrase_noop("რვა"),        # 8
	_phrase_noop("ცხრა"),       # 9
	_phrase_noop("ათ"),        # 10
	_phrase_noop("თერთმეტ"),   # 11
	_phrase_noop("თორმეტ"),    # 12
	_phrase_noop("ცამეტ"),     # 13
	_phrase_noop("თოთხმეტ"),   # 14
	_phrase_noop("თხუთმეტ"),   # 15
	_phrase_noop("თექვსმეტ"),  # 16
	_phrase_noop("ჩვიდმეტ"),   # 17
	_phrase_noop("თვრამეტ"),   # 18
	_phrase_noop("ცხრამეტ")    # 19
	]

ONES = [
	_phrase_noop("ნული"),       # 0
	_phrase_noop("ერთი"),       # 1
	_phrase_noop("ორი"),        # 2
	_phrase_noop("სამი"),       # 3
	_phrase_noop("ოთხი"),       # 4
	_phrase_noop("ხუთი"),       # 5
	_phrase_noop("ექვსი"),      # 6
	_phrase_noop("შვიდი"),      # 7
	_phrase_noop("რვა"),        # 8
	_phrase_noop("ცხრა"),       # 9
	_phrase_noop("ათი"),        # 10
	_phrase_noop("თერთმეტი"),   # 11
	_phrase_noop("თორმეტი"),    # 12
	_phrase_noop("ცამეტი"),     # 13
	_phrase_noop("თოთხმეტი"),   # 14
	_phrase_noop("თხუთმეტი"),   # 15
	_phrase_noop("თექვსმეტი"),  # 16
	_phrase_noop("ჩვიდმეტი"),   # 17
	_phrase_noop("თვრამეტი"),   # 18
	_phrase_noop("ცხრამეტი")    # 19
	]

ONES_ORDINAL = [
        "placeholder",
        _phrase_noop("მეერთე"),     # 1st (special form to use in big numerals)
        _phrase_noop("მეორე"),      # 2nd
        _phrase_noop("მესამე"),     # 3rd
        _phrase_noop("მეოთხე"),     # 4th
        _phrase_noop("მეხუთე"),     # 5th
        _phrase_noop("მეექვსე"),    # 6th
        _phrase_noop("მეშვიდე"),    # 7th
        _phrase_noop("მერვე"),      # 8th
        _phrase_noop("მეცხრე"),     # 9th
        _phrase_noop("მეათე"),      # 10th
        _phrase_noop("მეთერთმეტე"), # 11th
        _phrase_noop("მეთორმეტე"),  # 12th
        _phrase_noop("მეცამეტე"),   # 13th
        _phrase_noop("მეთოთხმეტე"), # 14th
        _phrase_noop("მეთხუთმეტე"), # 15th
        _phrase_noop("მეთექვსმეტე"),# 16th
        _phrase_noop("მეჩვიდმეტე"), # 17th
        _phrase_noop("მეთვრამეტე"), # 18th
        _phrase_noop("მეცხრამეტე"), # 19th
        ]

TWELVES = [
        "placeholder",
	_phrase_noop("ოცი"),        # 20
	_phrase_noop("ორმოცი"),     # 40
	_phrase_noop("სამოცი"),     # 60
	_phrase_noop("ოთხმოცი"),    # 80
	]

TWELVES_ORDINAL = [
        "placeholder",
        _phrase_noop("მეოცე"),      # 20th
        _phrase_noop("მეორმოცე"),   # 40th
        _phrase_noop("მესამოცე"),   # 60th
        _phrase_noop("მეოთხმოცე"),  # 80th
        ]

TWELVES_START = [
        "placeholder",
	_phrase_noop("ოცდა"),       # 20
	_phrase_noop("ორმოცდა"),    # 40
	_phrase_noop("სამოცდა"),    # 60
	_phrase_noop("ოთხმოცდა"),   # 80
	]

HUNDREDS_START = [
        "placeholder",
        _phrase_noop("ას"),         # 100
        _phrase_noop("ორას"),       # 200
        _phrase_noop("სამას"),      # 300
        _phrase_noop("ოთხას"),      # 400
        _phrase_noop("ხუთას"),      # 500
        _phrase_noop("ექვსას"),     # 600
        _phrase_noop("შვიდას"),     # 700
        _phrase_noop("რვაას"),      # 800
        _phrase_noop("ცხრაას"),     # 900
        ]

HUNDREDS = [
        "placeholder",
        _phrase_noop("ასი"),        # 100
        _phrase_noop("ორასი"),      # 200
        _phrase_noop("სამასი"),     # 300
        _phrase_noop("ოთხასი"),     # 400
        _phrase_noop("ხუთასი"),     # 500
        _phrase_noop("ექვსასი"),    # 600
        _phrase_noop("შვიდასი"),    # 700
        _phrase_noop("რვაასი"),     # 800
        _phrase_noop("ცხრაასი"),    # 900
        ]

HUNDREDS_ORDINAL = [
        "placeholder",
        _phrase_noop("მეასე"),      # 100th
        _phrase_noop("მეორასე"),    # 200th
        _phrase_noop("მესამასე"),   # 300th
        _phrase_noop("მეოთხასე"),   # 400th
        _phrase_noop("მეხუთასე"),   # 500th
        _phrase_noop("მეექვსასე"),  # 600th
        _phrase_noop("შვიდამესე"),  # 700th
        _phrase_noop("მერვაასე"),   # 800th
        _phrase_noop("მეცხრაასე"),  # 900th
        ]

MONTHS = [
	_phrase_noop("იანვარი"),    # Jan
	_phrase_noop("თებერვალი"),  # Feb
	_phrase_noop("მარტი"),      # Mar
	_phrase_noop("აპრილი"),     # Apr
	_phrase_noop("მაისი"),      # May
	_phrase_noop("ივნისი"),     # Jun
	_phrase_noop("ივლისი"),     # Jul
	_phrase_noop("აგვისტო"),    # Aug
	_phrase_noop("სექტემბერი"), # Sep
	_phrase_noop("ოქტომბერი"),  # Oct
	_phrase_noop("ნოემბერი"),   # Nov
	_phrase_noop("დეკემბერი")   # Dec
	]

def sayNumber(number, ordinal, flags):
    bound = False
    if flags != None and "B" in flags:
        bound = True
    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            return _phrase_noop("ნაკლებია, ვიდრე მინუს ერთი მილიარდი") # less than minus one billion
        else:
            return _phrase_noop("ერთ მილიარდზე მეტი") # more than one billion
    if number == 0:
        if bound:
            return _phrase_noop("ნულოვან") # zero
        else:
            return _phrase_noop("ნული") # zero

    if (minus):
        retval = _phrase_noop("მინუსი") + " " # minus
    if ordinal and number == 1:
        return retval + _phrase_noop("პირველი") # 1st
    num = number % 1000
    num_thousands = (number / 1000) % 1000
    num_millions = (number / 1000000) % 1000

    if num_millions > 0:
        if num_millions > 1:
            retval += __say_number(num_millions, False, False) + " "
        if num + num_thousands > 0:
            retval += _phrase_noop("მილიონ") + " " # million
        else:
            if ordinal:
                retval += _phrase_noop("მემილიონე") + " " # million
            else:
                retval += _phrase_noop("მილიონი") + " " # million
    if num_thousands > 0:
        if num_thousands > 1:
            retval += __say_number(num_thousands, False, False) + " "
        if num > 0:
            retval += _phrase_noop("ათას") + " " # thousand
        else:
            if ordinal:
                retval += _phrase_noop("მეათასე") + " " # thousand
            else:
                retval += _phrase_noop("ათასი") + " " # thousand
    if num > 0:
        retval += __say_number(num, ordinal, bound)

    return retval.rstrip()

def __say_number(number, ordinal, bound):
    if not ordinal:
        hundreds = HUNDREDS
        twelves = TWELVES
        ones = ONES
    else:
        hundreds = HUNDREDS_ORDINAL
        twelves = TWELVES_ORDINAL
        ones = ONES_ORDINAL
    if bound:
        ones = ONES_START
    retval = ""
    num = number % 20
    num_twelves = (number % 100) / 20
    num_hundreds = number / 100
    if num_hundreds > 0:
        if num_twelves + num > 0:
            retval += HUNDREDS_START[num_hundreds] + " "
        else:
            retval += hundreds[num_hundreds] + " "
    if num_twelves > 0:
        if num > 0:
            retval += TWELVES_START[num_twelves] + " "
        else:
            retval += twelves[num_twelves] + " "
    if num > 0:
        retval += ones[num] + " "
    return retval.rstrip()

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if not i.isdigit():
            pass
        i = int(i)
        retval += ONES[i] + " "

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
    if hours > 0:
        retval += sayNumber(hours, False, "B") + " "
        retval += _phrase_noop("საათზე") + " " # hours
    if minutes > 0:
        retval += sayNumber(minutes, False, "B") + " "
        retval += _phrase_noop("წუთი") + " " # minutes
    if s > 0 or (hours + minutes) == 0:
        retval += sayNumber(s, False, "B") + " "
        retval += _phrase_noop("წამში") + " " # seconds
    return retval.rstrip()

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    if (say_date):
        now = datetime.datetime.now()
        if (date_time.date() == now.date()):
            retval += _phrase_noop("დღეს") + " " # today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("გუშინ") + " " # yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("ხვალ") + " " # tomorrow
        else:
            retval += sayNumber(date_time.year, False, "") + " "
            retval += _phrase_noop("წლის") + " "
            retval += sayNumber(date_time.day, False, "") + " "
            retval += MONTHS[date_time.month - 1] + " "

    if (say_time):
        retval += sayNumber(date_time.hour, False, "") + " "
        retval += _phrase_noop("საათი") + " "
        if date_time.minute > 0:
            retval += sayNumber(date_time.minute, False, "") + " "
            retval += _phrase_noop("წუთი") + " "
    return retval.rstrip()

if (__name__ == "__main__"):
    print("########## Numbers ###########")
    for i in range(0, 100):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    for i in (123, 234, 345, 678, 876,
             1234, 2345, 12345, 456789, 1234567, 12345678, 234567891, 3456789012, -1000000123
             -1, -12):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    val = "1234560987"
    res = sayDigits(val, None)
    print("########## Ordinal numbers ###########")
    for i in range(0, 30):
        print("%d: %s" % (i, sayNumber(i, True, "")))
    print("########## Digit string ###########")
    print("%s: %s" % (val, res))
    print("########## Durations ###########")
    for i in (0, 1, 23, 466, 78912, 11, 14, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, True, None)))
    print("########## Date and time ###########")
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
              (datetime.datetime(2014, 9, 29, 10, 47), ''),
        ):
        print("%s - %s %s" % (str(i[0]), sayDatetime(i[0], True, True, True, None), i[1]))
