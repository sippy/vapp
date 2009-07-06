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

def _phrase_noop(str):
    return unicode(str)

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

ONES_ORDINAL = [
	"",
	_phrase_noop("primero"),
	_phrase_noop("segundo"),
	_phrase_noop("tercero"),
	_phrase_noop("cuarto"),
	_phrase_noop("quinto"),
	_phrase_noop("sexto"),
	_phrase_noop("séptimo"),
	_phrase_noop("octavo"),
	_phrase_noop("noveno"),
	_phrase_noop("décimo"),
	_phrase_noop("undécimo"),
	_phrase_noop("duodécimo"),
	_phrase_noop("decimotercero"),
	_phrase_noop("decimocuarto"),
	_phrase_noop("decimoquinto"),
	_phrase_noop("decimosexto"),
	_phrase_noop("decimoséptimo"),
	_phrase_noop("decimoctavo"),
	_phrase_noop("decimonoveno")
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

TENS_ORDINAL = [
	_phrase_noop("vigésimo"),
	_phrase_noop("trigésimo"),
	_phrase_noop("cuadragésimo"),
	_phrase_noop("quincuagésimo"),
	_phrase_noop("sexagésimo"),
	_phrase_noop("septuagésimo"),
	_phrase_noop("octogésimo"),
	_phrase_noop("nonagésimo")
	]

MONTHS = [ 
	_phrase_noop("Enero"),
	_phrase_noop("Febrero"),
	_phrase_noop("Marzo"),
	_phrase_noop("Abril"),
	_phrase_noop("Mayo"),
	_phrase_noop("Junio"),
	_phrase_noop("Julio"),
	_phrase_noop("Agosto"),
	_phrase_noop("Septiembre"),
	_phrase_noop("Octubre"),
	_phrase_noop("Noviembre"),
	_phrase_noop("Diciembre")
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
    #
    # Warning. Ordinals are correct for numbers up to 99 only.
    #
    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("less than minus one billion") # TODO
        else:
            retval = _phrase_noop("más de mil millones")
    else:
        if (minus):
            retval = _phrase_noop("menos") + " "
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
            retval += __say_number(num_thousands, False, GENDER_MASCULINE)
            retval += _phrase_noop("mil") + " "

        # hundreds
        if (num_hundreds > 0):
            if (num_hundreds > 1):
                retval += __say_number(num_hundreds, False, GENDER_MASCULINE)
                retval += _phrase_noop("cientos") + " "
            else:
                retval += _phrase_noop("ciento") + " "
        # less than a hundred
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
            retval = TENS_ORDINAL[tens - 2] + " "
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

def sayDigits(num, flags):
    retval = ""
    prev_o = False
    for i in str(num):
        if (i == '-'):
            pass
        i = int(i)
        if (i == 1):
            retval += UNOS[GENDER_NONE] + " "
        else:
            retval += ONES[i] + " "
    
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

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    retval = ""
    if (say_date):
        retval += sayNumber(date_time.day, True, "") + " "
        retval += _phrase_noop("de") + " "
        retval += MONTHS[date_time.month - 1] + " "
        retval += _phrase_noop("de") + " "
        retval += sayNumber(date_time.year, False, "") + " "

    if (say_time):
        retval += _phrase_noop("a") + " "
        hour = date_time.hour
        if hour == 1:
            retval += _phrase_noop("la") + " "
        else:
            retval += _phrase_noop("las") + " "
        retval += sayNumber(hour, False, "") + " "
        minute = date_time.minute
        if (minute > 0):
            retval += _phrase_noop("y") + " "
            retval += sayNumber(minute, False, "") + " "
   return retval.rstrip()
