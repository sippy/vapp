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

def _phrase_noop(str):
    return str

GENDER_FEMININE	    = 0
GENDER_MASCULINE    = 1
GENDER_NONE	    = 2

UNOS = [
	_phrase_noop("una"), # feminine
	_phrase_noop("un"),  # masculine
	_phrase_noop("uno"), # no gender
	]

ONES = [
	_phrase_noop("cero"),
	"placeholder", # use UNOS[] instead
	_phrase_noop("dos"),
	_phrase_noop("tres"),
	_phrase_noop("cuatro"),
	_phrase_noop("cinco"),
	_phrase_noop("seis"),
	_phrase_noop("siete"),
	_phrase_noop("ocho"),
	_phrase_noop("nueve"),
	_phrase_noop("diez"),
	_phrase_noop("once"),
	_phrase_noop("doce"),
	_phrase_noop("trece"),
	_phrase_noop("catorce"),
	_phrase_noop("quince"),
	_phrase_noop("dieziseis"),
	_phrase_noop("diezisiete"),
	_phrase_noop("dieziocho"),
	_phrase_noop("diezinueve")
	]

# FIXME!
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
	_phrase_noop("twelveth"),
	_phrase_noop("thirteenth"),
	_phrase_noop("fourteenth"),
	_phrase_noop("fifteenth"),
	_phrase_noop("sisxteenth"),
	_phrase_noop("seventeenth"),
	_phrase_noop("eighteenth"),
	_phrase_noop("nineteenth")
	]

TENS = [
	_phrase_noop("veinte"),
	_phrase_noop("treinta"),
	_phrase_noop("cuareinta"),
	_phrase_noop("cincuenta"),
	_phrase_noop("sesenta"),
	_phrase_noop("setenta"),
	_phrase_noop("ochenta"),
	_phrase_noop("noventa")
	]

# FIXME!
TENS_ORDINAL = [
	_phrase_noop("twentieth"),
	_phrase_noop("thirtieth"),
	_phrase_noop("fourtieth"),
	_phrase_noop("fiftieth"),
	_phrase_noop("sixtieth"),
	_phrase_noop("seventieth"),
	_phrase_noop("eightieth"),
	_phrase_noop("ninetieth")
	]

# FIXME!
MONTHS = [ 
	_phrase_noop("January"),
	_phrase_noop("February"),
	_phrase_noop("March"),
	_phrase_noop("April"),
	_phrase_noop("May"),
	_phrase_noop("Jun"),
	_phrase_noop("July"),
	_phrase_noop("August"),
	_phrase_noop("September"),
	_phrase_noop("October"),
	_phrase_noop("November"),
	_phrase_noop("December")
	]

def sayNumber(number, ordinal, flags):
    #
    # This method recognizes gender for numbers:
    #  M - masculine
    #  F - feminine
    #  N - no gender
    #
    gender = GENDER_NONE
    if (flags != None):
        if ('M' in flags):
            gender = GENDER_MASCULINE
        elif ('F' in flags):
            gender = GENDER_FEMININE
    return _sayNumber(number, ordinal, gender)

def _sayNumber(number, ordinal, gender):
    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("less than minus one billion") # TODO
        else:
            retval = _phrase_noop("more than one billion") # TODO
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
            if (num_hundred_millions > 1):
                retval += __say_number(num_hundred_millions, False, GENDER_MASCULINE)
                retval += _phrase_noop("cientos") + " "
            else:
                retval += _phrase_noop("ciento") + " "
        if ((num_hundred_millions + num_millions) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds + num_thousands + num_hundred_thousands) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("millionth") + " " # TODO
            else:
                if (num_millions > 1 or num_hundred_millions > 0):
                    retval += __say_number(num_millions, False, GENDER_MASCULINE)
                    retval += _phrase_noop("millones") + " "
                else:
                    retval += _phrase_noop("millon") + " "

        # thousands
        if (num_hundred_thousands > 0):
            if (num_hundred_thousands > 1):
                retval += __say_number(num_hundred_thousands, False, GENDER_MASCULINE)
                retval += _phrase_noop("cientos") + " "
            else:
                retval += _phrase_noop("ciento") + " "
        if ((num_hundred_thousands + num_thousands) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("thousandth") + " " # TODO
            else:
                retval += __say_number(num_thousands, False, GENDER_MASCULINE)
                retval += _phrase_noop("mil") + " "

        # the rest
        if (num_hundreds > 0):
            if (num_hundreds > 1):
                retval += __say_number(num_hundreds, False, GENDER_MASCULINE)
                retval += _phrase_noop("cientos") + " "
            else:
                retval += _phrase_noop("ciento") + " "
            tmp_ordinal = ordinal
            if (num > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("hundredth") + " " # TODO
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal, gender)

    return retval.rstrip()

def __say_number(number, ordinal, gender):
    retval = ""
    if (number < 20):
        if (ordinal):
            retval = ONES_ORDINAL[number] + " "
        elif (number == 1):
            retval = UNOS[gender] + " "
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
    if (tens > 0 and ones > 0):
        retval += _phrase_noop("y") + " "
    if (ones > 0):
        if (ordinal):
            retval += ONES_ORDINAL[ones] + " "
        elif (ones == 1):
            retval += UNOS[gender] + " "
        else:
            retval += ONES[ones] + " "
    return retval

# FIXME!
def sayDigits(num, flags):
    retval = ""
    prev_o = False
    for i in str(num):
        if (i == '-'):
            pass
        elif (int(i) == 0):
            if (prev_o):
                retval += _phrase_noop("double o") + " "
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
        retval += _sayNumber(hours, False, GENDER_FEMININE)
        if (hours == 1):
            retval += " " + _phrase_noop("hora")
        else:
            retval += " " + _phrase_noop("horas")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += _sayNumber(minutes, False, GENDER_MASCULINE)
        if (minutes == 1):
            retval += " " + _phrase_noop("minuto")
        else:
            retval += " " + _phrase_noop("minutos")
    if (s > 0):
        if (retval != ""):
            retval += " "
        retval += _sayNumber(s, False, GENDER_MASCULINE)
        if (s == 1):
            retval += " " + _phrase_noop("segundo")
        else:
            retval += " " + _phrase_noop("segundos")
    return retval

# FIXME!
def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    if (say_date):
        retval += MONTHS[date_time.month - 1] + " "
        retval += sayNumber(date_time.day, True, "") + " "
        yh = int(date_time.year / 100)
        yl = date_time.year % 100
        if (yl > 0):
            retval += sayNumber(yh, False, "") + " "
            if (yl < 10):
                retval += _phrase_noop("oh") + " "
            retval += sayNumber(yl, False, "") + " "
        else:
            retval += sayNumber(date_time.year, False, "") + " "

    if (say_time):
        retval += _phrase_noop("at") + " "
        suffix = _phrase_noop("PM")
        hour = date_time.hour
        if (hour > 12):
            hour -= 12
            suffix = _phrase_noop("PMh")
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
