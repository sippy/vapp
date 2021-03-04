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

__all__ = [ "TR" ]

def _phrase_noop(str):
    return unicode(str, 'utf-8')

ONES_POSTPOSITIONED = [
	_phrase_noop("0a"),
	_phrase_noop("1e"),
	_phrase_noop("2ye"),
	_phrase_noop("3e"),
	_phrase_noop("4e"),
	_phrase_noop("5e"),
	_phrase_noop("6ya"),
	_phrase_noop("7ye"),
	_phrase_noop("8e"),
	_phrase_noop("9a")
	]

ONES = [
	_phrase_noop("sifir"),  # 0
	_phrase_noop("bir"),	# 1
	_phrase_noop("iki"),	# 2
	_phrase_noop("üç"),	# 3
	_phrase_noop("dört"),	# 4
	_phrase_noop("beş"),	# 5
	_phrase_noop("alti"),	# 6
	_phrase_noop("yedi"),	# 7
	_phrase_noop("sekiz"),	# 8
	_phrase_noop("dokuz"),	# 9
	_phrase_noop("on"),	# 10
	_phrase_noop("onbir"),	# 11
	_phrase_noop("oniki"),	# 12
	_phrase_noop("onüç"),	# 13
	_phrase_noop("ondört"),	# 14
	_phrase_noop("onbeş"),	# 15
	_phrase_noop("onalti"),	# 16
	_phrase_noop("onyedi"),	# 17
	_phrase_noop("onsekiz"),# 18
	_phrase_noop("ondokuz"),# 19
	]

TENS = [
	_phrase_noop("yirmi"),	# 20
	_phrase_noop("otuz"),	# 30
	_phrase_noop("kirk"),	# 40
	_phrase_noop("elli"),	# 50
	_phrase_noop("altmış"),	# 60
	_phrase_noop("yetmiş"),	# 70
	_phrase_noop("seksen"),	# 80
	_phrase_noop("doksan")	# 90
	]

ONES_ORDINAL = [
	_phrase_noop("sifir"), 		# 0th
	_phrase_noop("birinci"), 	# 1st
	_phrase_noop("ikinci"),		# 2nd
	_phrase_noop("üçüncü"),		# 3rd
	_phrase_noop("dördüncü"),	# 4th
	_phrase_noop("beşinci"),	# 5th
	_phrase_noop("altıncı"),	# 6th
	_phrase_noop("yedinci"),	# 7th
	_phrase_noop("sekizinci"),	# 8th
	_phrase_noop("dokuzuncu"),	# 9th
	_phrase_noop("onuncu"),		# 10th
	_phrase_noop("onbirinci"),	# 11th
	_phrase_noop("onikinci"),	# 12th
	_phrase_noop("onüçüncü"),	# 13th
	_phrase_noop("ondördüncü"),	# 14th
	_phrase_noop("onbeşinci"),	# 15th
	_phrase_noop("onaltıncı"),	# 16th
	_phrase_noop("onyedinci"),	# 17th
	_phrase_noop("onsekizinci"),	# 18th
	_phrase_noop("ondokuzuncu")	# 19th
	]

TENS_ORDINAL = [
	_phrase_noop("yirminci"),	# 20th
	_phrase_noop("otuzuncu"),	# 30th
	_phrase_noop("kırkıncı"),	# 40th
	_phrase_noop("ellinci"),	# 50th
	_phrase_noop("altmışıncı"),	# 60th
	_phrase_noop("yetmişinci"),	# 70th
	_phrase_noop("sekseninci"),	# 80th
	_phrase_noop("doksanıncı")	# 90th
	]

MONTHS = [
	_phrase_noop("Ocak"), 		# January
	_phrase_noop("Şubat"),		# February
	_phrase_noop("Mart"),		# March
	_phrase_noop("Nisan"),		# April
	_phrase_noop("Mayıs"),		# May
	_phrase_noop("Haziran"),	# June
	_phrase_noop("Temmuz"),		# July
	_phrase_noop("Ağustos"),	# August
	_phrase_noop("Eylül"),		# September
	_phrase_noop("Ekim"),		# October
	_phrase_noop("Kasım"),		# November
	_phrase_noop("Aralık")		# December
	]

#
# Flags:
#
#  P - use postpositioned number
#
def sayNumber(number, ordinal, flags):
    retval = ""
    minus = False
    postposition = False
    if (flags != None and 'P' in flags):
        postposition = True
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
            retval = _phrase_noop("eksi") + " "
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
            retval += _phrase_noop("yüz") + " "
        if (num_millions > 0):
            retval += __say_number(num_millions, False)
        if ((num_hundred_millions + num_millions) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds + num_thousands + num_hundred_thousands) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("milyonuncu") + " "
            else:
                retval += _phrase_noop("milyon") + " "

        # thousands
        if (num_hundred_thousands > 0):
            if (num_hundred_thousands > 1):
                    retval += __say_number(num_hundred_thousands, False)
            retval += _phrase_noop("yüz") + " "
        if (num_thousands > 1):
            retval += __say_number(num_thousands, False)
        if ((num_hundred_thousands + num_thousands) > 0):
            tmp_ordinal = ordinal
            if ((num + num_hundreds) > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("bininci") + " "
            else:
                retval += _phrase_noop("bin") + " "

        # the rest
        if (num_hundreds > 0):
            if num_hundreds > 1:
                retval += __say_number(num_hundreds, False)
            tmp_ordinal = ordinal
            if (num > 0):
                tmp_ordinal = False
            if (tmp_ordinal):
                retval += _phrase_noop("yüzüncü") + " "
            else:
                retval += _phrase_noop("yüz") + " "
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal, postposition)

    return retval.rstrip()

def __say_number(number, ordinal, postposition = False):
    retval = ""
    if (number < 20):
        if (ordinal):
            retval = ONES_ORDINAL[number] + " "
        elif (postposition):
            retval = ONES_POSTPOSITIONED[number] + " "
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
        elif (postposition):
            retval += ONES_POSTPOSITIONED[ones] + " "
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
        retval += " " + _phrase_noop("saat")
    if (minutes > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(minutes, False, None)
        retval += " " + _phrase_noop("dakika")
    if (s > 0):
        if (retval != ""):
            retval += " "
        retval += sayNumber(s, False, None)
        retval += " " + _phrase_noop("saniye")
    return retval

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    now = datetime.datetime.now(date_time.tzinfo)
    #
    # Date
    #
    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("bugün") + " "	# today
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("dün") + " "	# yesterday
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("yarın") + " " 	# tomorrow
        else:
            retval += sayNumber(date_time.day, False, "") + " "
            retval += MONTHS[date_time.month - 1] + " "
            if (now.year != date_time.year):
                retval += sayNumber(date_time.year, False, "") + " "
    #
    # Time
    #
    if (say_time):
        prefix = _phrase_noop("Öğleden Sonra") # PM
        hour = date_time.hour
        if (hour >= 12):
            hour -= 12
            prefix = _phrase_noop("Öğleden Önce") # AM
        if (hour == 0):
            hour = 12
        retval += prefix + " " + _phrase_noop("saat") + " "
        retval += sayNumber(hour, False, "") + " "

        minute = date_time.minute
        if (minute > 0):
            retval += sayNumber(minute, False, "") + " "

    return retval.rstrip()
