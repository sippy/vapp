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
    return str

ONES = [
	_phrase_noop("zero"),
	_phrase_noop("one"),
	_phrase_noop("two"),
	_phrase_noop("three"),
	_phrase_noop("four"),
	_phrase_noop("five"),
	_phrase_noop("six"),
	_phrase_noop("seven"),
	_phrase_noop("eight"),
	_phrase_noop("nine"),
	_phrase_noop("ten"),
	_phrase_noop("eleven"),
	_phrase_noop("twelve"),
	_phrase_noop("thirteen"),
	_phrase_noop("fourteen"),
	_phrase_noop("fifteen"),
	_phrase_noop("sixteen"),
	_phrase_noop("seventeen"),
	_phrase_noop("eighteen"),
	_phrase_noop("nineteen")
	]

ONES_ORDINAL = [
	_phrase_noop("zeroth"),
	_phrase_noop("first"),
	_phrase_noop("second"),
	_phrase_noop("third"),
	_phrase_noop("fourth"),
	_phrase_noop("fifth"),
	_phrase_noop("sixth"),
	_phrase_noop("seventh"),
	_phrase_noop("eightth"),
	_phrase_noop("nineth"),
	_phrase_noop("tenth"),
	_phrase_noop("eleventh"),
	_phrase_noop("twelfth"),
	_phrase_noop("thirteenth"),
	_phrase_noop("fourteenth"),
	_phrase_noop("fifteenth"),
	_phrase_noop("sixteenth"),
	_phrase_noop("seventeenth"),
	_phrase_noop("eighteenth"),
	_phrase_noop("nineteenth")
	]

TENS = [
	_phrase_noop("twenty"),
	_phrase_noop("thirty"),
	_phrase_noop("fourty"),
	_phrase_noop("fifty"),
	_phrase_noop("sixty"),
	_phrase_noop("seventy"),
	_phrase_noop("eighty"),
	_phrase_noop("ninety")
	]

TENS_ORDINAL = [
	_phrase_noop("twentieth"),
	_phrase_noop("thirtieth"),
	_phrase_noop("fortieth"),
	_phrase_noop("fiftieth"),
	_phrase_noop("sixtieth"),
	_phrase_noop("seventieth"),
	_phrase_noop("eightieth"),
	_phrase_noop("ninetieth")
	]

MONTHS = [ 
	_phrase_noop("January"),
	_phrase_noop("February"),
	_phrase_noop("March"),
	_phrase_noop("April"),
	_phrase_noop("May"),
	_phrase_noop("June"),
	_phrase_noop("July"),
	_phrase_noop("August"),
	_phrase_noop("September"),
	_phrase_noop("October"),
	_phrase_noop("November"),
	_phrase_noop("December")
	]

def sayNumber(number, ordinal, flags):
    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("less than minus one billion")
        else:
            retval = _phrase_noop("more than one billion")
    else:
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
            retval += __say_number(num_hundred_millions, False)
            retval += _phrase_noop("hundred") + " "
        if (num_millions > 0):
            retval += __say_number(num_millions, False)
        if ((num_hundred_millions + num_millions) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds + num_thousands + num_hundred_thousands) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("millionth") + " "
            else:
                retval += _phrase_noop("million") + " "

        # thousands
        if (num_hundred_thousands > 0):
            retval += __say_number(num_hundred_thousands, False)
            retval += _phrase_noop("hundred") + " "
        if (num_thousands > 0):
            retval += __say_number(num_thousands, False)
        if ((num_hundred_thousands + num_thousands) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("thousandth") + " "
            else:
                retval += _phrase_noop("thousand") + " "

        # the rest
        if (num_hundreds > 0):
            retval += __say_number(num_hundreds, False)
            tmp_ordinal = ordinal
            if (num > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("hundredth") + " "
            else:
                retval += _phrase_noop("hundred") + " "
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal)

    return retval.rstrip()

def __say_number(number, ordinal):
    retval = ""
    if (number < 20):
        if (ordinal):
            retval = ONES_ORDINAL[number] + " "
        else:
            retval = ONES[number] + " "
        return retval
    tens = int(number / 10)
    ones = number % 10
    if (tens > 0):
        if (ordinal):
            if (ones == 0):
                retval = TENS_ORDINAL[tens - 2] + " "
            else:
                retval = TENS[tens - 2] + " "
        else:
            retval = TENS[tens - 2] + " "
    if (ones > 0):
        if (ordinal):
            retval += ONES_ORDINAL[ones] + " "
        else:
            retval += ONES[ones] + " "
    return retval

def sayDigits(num, flags):
    retval = ""
    prev_o = False
    for i in str(num):
        if (not i.isdigit()):
            prev_o = False
        elif (int(i) == 0):
            if (prev_o):
                retval += _phrase_noop("double oh") + " "
                prev_o = False
            else:
                prev_o = True
        else:
            if (prev_o):
                retval += _phrase_noop("oh") + " "
                prev_o = False
            retval += ONES[int(i)] + " "
    if (prev_o):
        retval += _phrase_noop("oh")
    
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
        retval += sayNumber(hours, False, None)
        if (hours == 1):
            retval += " " + _phrase_noop("hour")
        else:
            retval += " " + _phrase_noop("hours")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(minutes, False, None)
        if (minutes == 1):
            retval += " " + _phrase_noop("minute")
        else:
            retval += " " + _phrase_noop("minutes")
    if (s > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(s, False, None)
        if (s == 1):
            retval += " " + _phrase_noop("second")
        else:
            retval += " " + _phrase_noop("seconds")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    now = datetime.datetime.now(date_time.tzinfo)

    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("today") + " "
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("yesterday") + " "
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("tomorrow") + " "
        else:
            retval += MONTHS[date_time.month - 1] + " "
            retval += sayNumber(date_time.day, True, "") + " "
            yh = int(date_time.year / 100)
            yl = date_time.year % 100
            if (yl > 0 and date_time.year < 2000):
                retval += sayNumber(yh, False, "") + " "
                if (yl < 10):
                    retval += _phrase_noop("oh") + " "
                retval += sayNumber(yl, False, "") + " "
            else:
                retval += sayNumber(date_time.year, False, "") + " "

    if (say_time):
        retval += _phrase_noop("at") + " "
        suffix = _phrase_noop("A-M")
        hour = date_time.hour
        if (hour >= 12):
            hour -= 12
            suffix = _phrase_noop("P-M")
        if (hour == 0):
            hour = 12
        retval += sayNumber(hour, False, "") + " "
        minute = date_time.minute
        if (minute > 0):
            if (minute < 10):
                retval += _phrase_noop("oh") + " "
            retval += sayNumber(minute, False, "") + " "
        if (say_seconds):
            secs = date_time.second
            retval += _phrase_noop("and") + " "
            retval += sayNumber(secs, False, "") + " "
            if (secs == 1):
                retval += _phrase_noop("second") + " "
            else:
                retval += _phrase_noop("seconds") + " "
        retval += suffix
    return retval.rstrip()

if __name__ == "__main__":
    tmp = datetime.datetime.now()
    now = datetime.datetime(tmp.year, tmp.month, tmp.day, tmp.hour, tmp.minute, tmp.second)
    now = datetime.datetime(tmp.year, tmp.month, tmp.day, 10, 47, 44)
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
