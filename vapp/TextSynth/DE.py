#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2010 Sippy Software, Inc. All rights reserved.
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

def _phrase_noop(str):
    return unicode(str, 'utf-8')

GENDER_FEMININE	    = 0
GENDER_MASCULINE    = 1
GENDER_NONE	    = 2

ONES_QUANTITATIVE = {
        GENDER_MASCULINE : _phrase_noop('ein'),
        GENDER_NONE : _phrase_noop('ein'),
        GENDER_FEMININE : _phrase_noop('eine')
    }

ONES = [
	_phrase_noop("null"),
	_phrase_noop("eins"),
	_phrase_noop("zwei"),
	_phrase_noop("drei"),
	_phrase_noop("vier"),
	_phrase_noop("fünf"),
	_phrase_noop("sechs"),
	_phrase_noop("sieben"),
	_phrase_noop("acht"),
	_phrase_noop("neun"),
	_phrase_noop("zehn"),
	_phrase_noop("elf"),
	_phrase_noop("zwölf"),
	_phrase_noop("dreizehn"),
	_phrase_noop("vierzehn"),
	_phrase_noop("fünfzehn"),
	_phrase_noop("sechzehn"),
	_phrase_noop("siebzehn"),
	_phrase_noop("achtzehn"),
	_phrase_noop("neunzehn")
	]

ONES_ORDINAL = [
	"",
	_phrase_noop("erste"),
	_phrase_noop("zweite"),
	_phrase_noop("dritte"),
	_phrase_noop("vierte"),
	_phrase_noop("fünfte"),
	_phrase_noop("sechste"),
	_phrase_noop("siebte"),
	_phrase_noop("achte"),
	_phrase_noop("neunte"),
	_phrase_noop("zehnte"),
	_phrase_noop("elfte"),
	_phrase_noop("zwölfte"),
	_phrase_noop("dreizehnte"),
	_phrase_noop("vierzehnte"),
	_phrase_noop("fünfzehnte"),
	_phrase_noop("sechzehnte"),
	_phrase_noop("siebzehnte"),
	_phrase_noop("achtzehnte"),
	_phrase_noop("neunzehnte")
	]

TENS = [
	_phrase_noop("zwanzig"),
	_phrase_noop("dreißig"),
	_phrase_noop("vierzig"),
	_phrase_noop("fünfzig"),
	_phrase_noop("sechzig"),
	_phrase_noop("siebzig"),
	_phrase_noop("achtzig"),
	_phrase_noop("neunzig")
	]

TENS_ORDINAL = [
	_phrase_noop("zwanzigste"),
	_phrase_noop("dreißigste"),
	_phrase_noop("vierzigste"),
	_phrase_noop("fünfzigste"),
	_phrase_noop("sechzigste"),
	_phrase_noop("siebzigste"),
	_phrase_noop("achtzigste"),
	_phrase_noop("neunzigste")
	]

MONTHS = [ 
	_phrase_noop("Januar"),
	_phrase_noop("Februar"),
	_phrase_noop("März"),
	_phrase_noop("April"),
	_phrase_noop("Mai"),
	_phrase_noop("Juni"),
	_phrase_noop("Juli"),
	_phrase_noop("August"),
	_phrase_noop("September"),
	_phrase_noop("Oktober"),
	_phrase_noop("November"),
	_phrase_noop("Dezember")
	]

def sayNumber(number, ordinal, flags):
    #
    # This method recognizes gender for numbers:
    #  M - masculine
    #  F - feminine
    #  N - no gender
    #
    gender = GENDER_MASCULINE
    if (flags != None):
        if ('M' in flags):
            gender = GENDER_MASCULINE
        elif ('F' in flags):
            gender = GENDER_FEMININE
    return _sayNumber(number, ordinal, gender)

def _sayNumber(number, ordinal, gender):
    if number == 0:
        return ONES[0]

    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True

    if (number >= 1000000000):
        if (minus):
            return _phrase_noop("weniger als minus eine Milliarde")
        else:
            return _phrase_noop("mehr als eine Million")

    if (minus):
        retval = _phrase_noop("minus") + " "
    num = number % 100
    num_hundreds = int((number % 1000) / 100)
    num_thousands = int(number / 1000) % 100
    num_hundred_thousands = int(number / 100000) % 10
    num_millions = int(number / 1000000) % 100
    num_hundred_millions = int(number / 100000000) % 10

    # millions
    if (num_hundred_millions > 0):
        retval += __say_number(num_hundred_millions, False, gender)
        retval += _phrase_noop("hundert") + " "
    if ((num_hundred_millions + num_millions) > 0):
        retval += __say_number(num_millions, False, gender)
        if (num_millions > 1 or num_hundred_millions > 0):
            retval += _phrase_noop("Millionen") + " "
        else:
            retval += _phrase_noop("Million") + " "

    # thousands
    if (num_hundred_thousands > 0):
        retval += __say_number(num_hundred_thousands, False, gender)
        retval += _phrase_noop("hundert") + " "
    if ((num_hundred_thousands + num_thousands) > 0):
        retval += __say_number(num_thousands, False, gender)
        retval += _phrase_noop("tausend") + " "

    # hundreds
    if (num_hundreds > 0):
        retval += __say_number(num_hundreds, False, gender)
        retval += _phrase_noop("hundert") + " "
    # less than a hundred
    if (num > 0 or number == 0):
        retval += __say_number(num, ordinal, gender)

    return retval.rstrip()

def __say_number(number, ordinal, gender):
    retval = ""
    if number == 1:
        if ordinal:
            return ONES_ORDINAL[gender] + " "
        else:
            return ONES_QUANTITATIVE[gender] + " "

    if (number < 20):
        if (ordinal):
            retval = ONES_ORDINAL[number] + " "
        else:
            retval = ONES[number] + " "
        return retval
    tens = int(number / 10)
    ones = number % 10

    if ones > 0:
        retval += ONES[ones] + " " + _phrase_noop("und") + " "
    if ordinal:
        retval += TENS_ORDINAL[tens - 2] + " "
    else:
        retval += TENS[tens - 2] + " "

    return retval

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (i == '-'):
            pass
        i = int(i)
        retval += ONES[i] + " "
    return retval.rstrip()

def sayDuration(seconds, say_hours, say_minutes, say_seconds, flags):
    retval = ""
    if seconds == 0:
        retval += ONES[0] + " "
        if say_seconds:
            return retval + _phrase_noop("Sekunden")
        elif say_minutes:
            return retval + _phrase_noop("Minuten")
        else:
            return retval + _phrase_noop("Stunden")

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
        retval += _sayNumber(hours, False, GENDER_FEMININE)
        if (hours == 1):
            retval += " " + _phrase_noop("Stunde")
        else:
            retval += " " + _phrase_noop("Stunden")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += _sayNumber(minutes, False, GENDER_FEMININE)
        if (minutes == 1):
            retval += " " + _phrase_noop("Minute")
        else:
            retval += " " + _phrase_noop("Minuten")
    if (s > 0):
        if (retval != ""):
            retval += " "
        retval += _sayNumber(s, False, GENDER_FEMININE)
        if (s == 1):
            retval += " " + _phrase_noop("Sekunde")
        else:
            retval += " " + _phrase_noop("Sekunden")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("heute") + " " # today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("gestern") + " " # yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("morgen") + " " # tomorrow
        else:
            retval += _phrase_noop("der") + " "
            retval += sayNumber(date_time.day, True, "") + " "
            retval += MONTHS[date_time.month - 1] + " "
            if date_time.year >= 2000:
                retval += sayNumber(date_time.year, False, "") + " "
            else:
                retval += sayNumber(int(date_time.year / 100), False, "") + " "
                retval += _phrase_noop("hundert") + " "
                retval += sayNumber(date_time.year % 100, False, "") + " "

    if (say_time):
        hour = date_time.hour
        retval += sayNumber(hour, False, "") + " "
        retval += _phrase_noop("Uhr") + " "
        minute = date_time.minute
        if (minute > 0):
            retval += sayNumber(minute, False, "") + " "
    return retval.rstrip()

if (__name__ == "__main__"):
    import datetime
    print("########## German numbers ###########")
    for i in (123, 234, 345, 678, 876, 
             1234, 2345, 12345, 456789, 1234567, 12345678, 234567891, 3456789012, -1000000123
             -1, -12):
        print("%d: %s" % (i, sayNumber(i, False, "")))
    val = "1234560987"
    res = sayDigits(val, None)
    print("########## Digit string ###########")
    print("%s: %s" % (val, res))
    print("########## German durations ###########")
    for i in (0, 1, 23, 466, 78912, 11, 14, 100, 1004, 10003, 100002, 1000001):
        h = int(i / 3600)
        m = int(i / 60) % 60
        s = i % 60
        print("%02d:%02d:%02d - %s" % (h, m, s, sayDuration(i, True, True, True, None)))
    print("########## German date and time ###########")
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
