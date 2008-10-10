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


def _phrase_noop(str):
    return unicode(str, 'utf-8')

ONES = [
	_phrase_noop("ศูนย์"),
	_phrase_noop("หนึ่ง"),
	_phrase_noop("สอง"),
	_phrase_noop("สาม"),
	_phrase_noop("สี่"),
	_phrase_noop("ห้า"),
	_phrase_noop("หก"),
	_phrase_noop("เจ็ด"),
	_phrase_noop("แปด"),
	_phrase_noop("เก้า"),
	_phrase_noop("สิบ"),
	_phrase_noop("สิบเอ็ด"),
	_phrase_noop("สิบสอง"),
	_phrase_noop("สิบสาม"),
	_phrase_noop("สิบสี่"),
	_phrase_noop("สิบห้า"),
	_phrase_noop("สิบหก"),
	_phrase_noop("สิบเจ็ด"),
	_phrase_noop("สิบแปด"),
	_phrase_noop("สิบเก้า")
	]

ONES_ORDINAL = [
	]

TENS = [
	_phrase_noop("ยี่สิบ"),
	_phrase_noop("สามสิบ"),
	_phrase_noop("สี่สิบ"),
	_phrase_noop("ห้าสิบ"),
	_phrase_noop("หกสิบ"),
	_phrase_noop("เจ็ดสิบ"),
	_phrase_noop("แปดสิบ"),
	_phrase_noop("เก้าสิบ")
	]

TENS_ORDINAL = [
	]

MONTHS = [ 
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
        num_thousands = int(number / 1000) % 10
        num_ten_thousands = int(number / 10000) % 10
        num_hundred_thousands = int(number / 100000) % 10
        num_millions = int(number / 1000000) % 100
        num_hundred_millions = int(number / 100000000) % 10

        # millions
#	    if (num_hundred_millions > 0):
#		retval += __say_number(num_hundred_millions, False)
#		retval += _phrase_noop("ร้อย") + " "
        if (num_millions > 0):
            retval += __say_number(num_millions, False)
            retval += _phrase_noop("ล้าน") + " "

        # thousands
        if (num_hundred_thousands > 0):
            retval += __say_number(num_hundred_thousands, False)
            retval += _phrase_noop("แสน") + " "
        if (num_ten_thousands > 0):
            retval += __say_number(num_ten_thousands, False)
            retval += _phrase_noop("หมื่น") + " "
        if (num_thousands > 0):
            retval += __say_number(num_thousands, False)
            retval += _phrase_noop("พัน") + " "

        # the rest
        if (num_hundreds > 0):
            retval += __say_number(num_hundreds, False)
            retval += _phrase_noop("ร้อย") + " "
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
        elif(ones == 1):
            retval += _phrase_noop("เอ็ด")
        else:
            retval += ONES[ones] + " "
    return retval

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (i.isdigit()):
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
    s = int(s % 60)
    if (hours > 0):
        retval += sayNumber(hours, False, None)
        retval += " " + _phrase_noop("ชั่วโมง")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(minutes, False, None)
        retval += " " + _phrase_noop("นาที")
    if (s > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(s, False, None)
        retval += " " + _phrase_noop("วินาที")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    # TODO
    return ""
