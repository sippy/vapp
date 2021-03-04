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

CASE_NOMINATIVE	    = 0 # именительный падеж [Cn] (default)
CASE_GENITIVE	    = 1 # родительный падеж  [Cg]
CASE_DATIVE	    = 2 # дательный падеж    [Cd]
CASE_ACCUSATIVE	    = 3 # винительный падеж  [Ca]
CASE_INSTRUMENTAL   = 4 # творительный падеж [Ci]
CASE_PREPOSITIONAL  = 5 # предложный падеж   [Cp]

GENDER_NEUTER	    = 0	# [N]
GENDER_MASCULINE    = 1 # default
GENDER_FEMININE	    = 2 # [F]
#
# IS_PREFIX используется для следующей формы порядкового числительного:
#
#   "одно"-милионная
#
# в то время как указание GENDER_FEMININE даст
#
#   "первая"
#
IS_PREFIX	    = 3

def _phrase_noop(s):
    return s

TENS_P = \
    [
        _phrase_noop("двадцати"),
        _phrase_noop("тридцати"),
        _phrase_noop("сорока"),
        _phrase_noop("пятидесяти"),
        _phrase_noop("шестидесяти"),
        _phrase_noop("семидесяти"),
        _phrase_noop("восьмидесяти"),
        _phrase_noop("девяносто")
    ]

TENS = [
    [
        _phrase_noop("двадцать"),
        _phrase_noop("тридцать"),
        _phrase_noop("сорок"),
        _phrase_noop("пятьдесят"),
        _phrase_noop("шестьдесят"),
        _phrase_noop("семьдесят"),
        _phrase_noop("восемьдесят"),
        _phrase_noop("девяносто")
    ], [
        _phrase_noop("двадцати"),
        _phrase_noop("тридцати"),
        _phrase_noop("сорока"),
        _phrase_noop("пятидесяти"),
        _phrase_noop("шестьдесяти"),
        _phrase_noop("семидесяти"),
        _phrase_noop("восьмидесяти"),
        _phrase_noop("девяноста")
    ], [
        _phrase_noop("двадцати"),
        _phrase_noop("тридцати"),
        _phrase_noop("сорока"),
        _phrase_noop("пятидесяти"),
        _phrase_noop("шестьдесяти"),
        _phrase_noop("семидесяти"),
        _phrase_noop("восьмидесяти"),
        _phrase_noop("девяноста")
    ], [
        _phrase_noop("двадцать"),
        _phrase_noop("тридцать"),
        _phrase_noop("сорок"),
        _phrase_noop("пятьдесят"),
        _phrase_noop("шестьдесят"),
        _phrase_noop("семидесят"),
        _phrase_noop("восемьдесят"),
        _phrase_noop("девяносто")
    ], [
        _phrase_noop("двадцатью"),
        _phrase_noop("тридцатью"),
        _phrase_noop("сорока"),
        _phrase_noop("пятьюдесятью"),
        _phrase_noop("шестьюдесятью"),
        _phrase_noop("семьюдесятью"),
        _phrase_noop("восемьюдесятью"),
        _phrase_noop("девяноста")
    ], [
        _phrase_noop("двадцати"),
        _phrase_noop("тридцати"),
        _phrase_noop("сорока"),
        _phrase_noop("пятидесяти"),
        _phrase_noop("шестьдесяти"),
        _phrase_noop("семидесяти"),
        _phrase_noop("восьмидесяти"),
        _phrase_noop("девяноста")
    ]
        ]

TENS_N_ORD = [
    [
        _phrase_noop("двадцатое"),
        _phrase_noop("тридцатое"),
        _phrase_noop("сороковое"),
        _phrase_noop("пятидесятое"),
        _phrase_noop("шестидесятое"),
        _phrase_noop("семидесятое"),
        _phrase_noop("восьмидесятое"),
        _phrase_noop("девяностое")
    ], [
        _phrase_noop("двадцатого"),
        _phrase_noop("тридцатого"),
        _phrase_noop("сорокового"),
        _phrase_noop("пятидесятого"),
        _phrase_noop("шестидесятого"),
        _phrase_noop("семидесятого"),
        _phrase_noop("восьмидесятого"),
        _phrase_noop("девяностого")
    ], [
        _phrase_noop("двадцатому"),
        _phrase_noop("тридцатому"),
        _phrase_noop("сороковому"),
        _phrase_noop("пятидесятому"),
        _phrase_noop("шестидесятому"),
        _phrase_noop("семидесятому"),
        _phrase_noop("восьмидесятому"),
        _phrase_noop("девяностому")
    ], [
        _phrase_noop("двадцатое"),
        _phrase_noop("тридцатое"),
        _phrase_noop("сороковое"),
        _phrase_noop("пятидесятое"),
        _phrase_noop("шестидесятое"),
        _phrase_noop("семидесятое"),
        _phrase_noop("восьмидесятое"),
        _phrase_noop("девяностое")
    ], [
        _phrase_noop("двадцатым"),
        _phrase_noop("тридцатым"),
        _phrase_noop("сороковым"),
        _phrase_noop("пятидесятым"),
        _phrase_noop("шестидесятым"),
        _phrase_noop("семидесятым"),
        _phrase_noop("восьмидесятым"),
        _phrase_noop("девяностым")
    ], [
        _phrase_noop("двадцатом"),
        _phrase_noop("тридцатом"),
        _phrase_noop("сороковом"),
        _phrase_noop("пятидесятом"),
        _phrase_noop("шестидесятом"),
        _phrase_noop("семидесятом"),
        _phrase_noop("восьмидесятом"),
        _phrase_noop("девяностом")
    ]
        ]

TENS_F_ORD = [
    [
        _phrase_noop("двадцатая"),
        _phrase_noop("тридцатая"),
        _phrase_noop("сороковая"),
        _phrase_noop("пятидесятая"),
        _phrase_noop("шестидесятая"),
        _phrase_noop("семидесятая"),
        _phrase_noop("восьмидесятая"),
        _phrase_noop("девяностая")
    ], [
        _phrase_noop("двадцатой"),
        _phrase_noop("тридцатой"),
        _phrase_noop("сороковой"),
        _phrase_noop("пятидесятой"),
        _phrase_noop("шестидесятой"),
        _phrase_noop("семидесятой"),
        _phrase_noop("восьмидесятой"),
        _phrase_noop("девяностой")
    ], [
        _phrase_noop("двадцатой"),
        _phrase_noop("тридцатой"),
        _phrase_noop("сороковой"),
        _phrase_noop("пятидесятой"),
        _phrase_noop("шестидесятой"),
        _phrase_noop("семидесятой"),
        _phrase_noop("восьмидесятой"),
        _phrase_noop("девяностой")
    ], [
        _phrase_noop("двадцатую"),
        _phrase_noop("тридцатую"),
        _phrase_noop("сороковую"),
        _phrase_noop("пятидесятую"),
        _phrase_noop("шестидесятую"),
        _phrase_noop("семидесятую"),
        _phrase_noop("восьмидесятую"),
        _phrase_noop("девяностую")
    ], [
        _phrase_noop("двадцатой"),
        _phrase_noop("тридцатой"),
        _phrase_noop("сороковой"),
        _phrase_noop("пятидесятой"),
        _phrase_noop("шестидесятой"),
        _phrase_noop("семидесятой"),
        _phrase_noop("восьмидесятой"),
        _phrase_noop("девяностой")
    ], [
        _phrase_noop("двадцатой"),
        _phrase_noop("тридцатой"),
        _phrase_noop("сороковой"),
        _phrase_noop("пятидесятой"),
        _phrase_noop("шестидесятой"),
        _phrase_noop("семидесятой"),
        _phrase_noop("восьмидесятой"),
        _phrase_noop("девяностой")
    ]
        ]

TENS_M_ORD = [
    [
        _phrase_noop("двадцатый"),
        _phrase_noop("тридцатый"),
        _phrase_noop("сороковый"),
        _phrase_noop("пятидесятый"),
        _phrase_noop("шестидесятый"),
        _phrase_noop("семидесятый"),
        _phrase_noop("восьмидесятый"),
        _phrase_noop("девяностый")
    ], [
        _phrase_noop("двадцатого"),
        _phrase_noop("тридцатого"),
        _phrase_noop("сорокового"),
        _phrase_noop("пятидесятого"),
        _phrase_noop("шестидесятого"),
        _phrase_noop("семидесятого"),
        _phrase_noop("восьмидесятого"),
        _phrase_noop("девяностого")
    ], [
        _phrase_noop("двадцатому"),
        _phrase_noop("тридцатому"),
        _phrase_noop("сороковому"),
        _phrase_noop("пятидесятому"),
        _phrase_noop("шестидесятому"),
        _phrase_noop("семидесятому"),
        _phrase_noop("восьмидесятому"),
        _phrase_noop("девяностому")
    ], [
        _phrase_noop("двадцатый"),
        _phrase_noop("тридцатый"),
        _phrase_noop("сороковый"),
        _phrase_noop("пятидесятый"),
        _phrase_noop("шестидесятый"),
        _phrase_noop("семидесятый"),
        _phrase_noop("восьмидесятый"),
        _phrase_noop("девяностый")
    ], [
        _phrase_noop("двадцатым"),
        _phrase_noop("тридцатым"),
        _phrase_noop("сороковым"),
        _phrase_noop("пятидесятым"),
        _phrase_noop("шестидесятым"),
        _phrase_noop("семидесятым"),
        _phrase_noop("восьмидесятым"),
        _phrase_noop("девяностым")
    ], [
        _phrase_noop("двадцатом"),
        _phrase_noop("тридцатом"),
        _phrase_noop("сороковом"),
        _phrase_noop("пятидесятом"),
        _phrase_noop("шестидесятом"),
        _phrase_noop("семидесятом"),
        _phrase_noop("восьмидесятом"),
        _phrase_noop("девяностом")
    ]
        ]

ONES_N_ORD = [
    [
        _phrase_noop("нулевое"),
        _phrase_noop("первое"),
        _phrase_noop("второе"),
        _phrase_noop("третье"),
        _phrase_noop("четвёртое"),
        _phrase_noop("пятое"),
        _phrase_noop("шестое"),
        _phrase_noop("седьмое"),
        _phrase_noop("восьмое"),
        _phrase_noop("девятое"),
        _phrase_noop("десятое"),
        _phrase_noop("одинадцатое"),
        _phrase_noop("двенадцатое"),
        _phrase_noop("тринадцатое"),
        _phrase_noop("четырнадцатое"),
        _phrase_noop("пятнадцатое"),
        _phrase_noop("шестнадцатое"),
        _phrase_noop("семнадцатое"),
        _phrase_noop("восемнадцатое"),
        _phrase_noop("девятнадцатое")
    ], [
        _phrase_noop("нулевого"),
        _phrase_noop("первого"),
        _phrase_noop("второго"),
        _phrase_noop("третьего"),
        _phrase_noop("четвёртого"),
        _phrase_noop("пятого"),
        _phrase_noop("шестого"),
        _phrase_noop("седьмого"),
        _phrase_noop("восьмого"),
        _phrase_noop("девятого"),
        _phrase_noop("десятого"),
        _phrase_noop("одинадцатого"),
        _phrase_noop("двенадцатого"),
        _phrase_noop("тринадцатого"),
        _phrase_noop("четырнадцатого"),
        _phrase_noop("пятнадцатого"),
        _phrase_noop("шестнадцатого"),
        _phrase_noop("семнадцатого"),
        _phrase_noop("восемнадцатого"),
        _phrase_noop("девятнадцатого")
    ], [
        _phrase_noop("нулевому"),
        _phrase_noop("первому"),
        _phrase_noop("второму"),
        _phrase_noop("третьему"),
        _phrase_noop("четвёртому"),
        _phrase_noop("пятому"),
        _phrase_noop("шестому"),
        _phrase_noop("седьмому"),
        _phrase_noop("восьмому"),
        _phrase_noop("девятому"),
        _phrase_noop("десятому"),
        _phrase_noop("одинадцатому"),
        _phrase_noop("двенадцатому"),
        _phrase_noop("тринадцатому"),
        _phrase_noop("четырнадцатому"),
        _phrase_noop("пятнадцатому"),
        _phrase_noop("шестнадцатому"),
        _phrase_noop("семнадцатому"),
        _phrase_noop("восемнадцатому"),
        _phrase_noop("девятнадцатому")
    ], [
        _phrase_noop("нулевое"),
        _phrase_noop("первое"),
        _phrase_noop("второе"),
        _phrase_noop("третье"),
        _phrase_noop("четвёртое"),
        _phrase_noop("пятое"),
        _phrase_noop("шестое"),
        _phrase_noop("седьмое"),
        _phrase_noop("восьмое"),
        _phrase_noop("девятое"),
        _phrase_noop("десятое"),
        _phrase_noop("одинадцатое"),
        _phrase_noop("двенадцатое"),
        _phrase_noop("тринадцатое"),
        _phrase_noop("четырнадцатое"),
        _phrase_noop("пятнадцатое"),
        _phrase_noop("шестнадцатое"),
        _phrase_noop("семнадцатое"),
        _phrase_noop("восемнадцатое"),
        _phrase_noop("девятнадцатое")
    ], [
        _phrase_noop("нулевым"),
        _phrase_noop("первым"),
        _phrase_noop("вторым"),
        _phrase_noop("третьим"),
        _phrase_noop("четвёртым"),
        _phrase_noop("пятым"),
        _phrase_noop("шестым"),
        _phrase_noop("седьмым"),
        _phrase_noop("восьмым"),
        _phrase_noop("девятым"),
        _phrase_noop("десятым"),
        _phrase_noop("одинадцатым"),
        _phrase_noop("двенадцатым"),
        _phrase_noop("тринадцатым"),
        _phrase_noop("четырнадцатым"),
        _phrase_noop("пятнадцатым"),
        _phrase_noop("шестнадцатым"),
        _phrase_noop("семнадцатым"),
        _phrase_noop("восемнадцатым"),
        _phrase_noop("девятнадцатым")
    ], [
        _phrase_noop("нулевом"),
        _phrase_noop("первом"),
        _phrase_noop("втором"),
        _phrase_noop("третьем"),
        _phrase_noop("четвёртом"),
        _phrase_noop("пятом"),
        _phrase_noop("шестом"),
        _phrase_noop("седьмом"),
        _phrase_noop("восьмом"),
        _phrase_noop("девятом"),
        _phrase_noop("десятом"),
        _phrase_noop("одинадцатом"),
        _phrase_noop("двенадцатом"),
        _phrase_noop("тринадцатом"),
        _phrase_noop("четырнадцатом"),
        _phrase_noop("пятнадцатом"),
        _phrase_noop("шестнадцатом"),
        _phrase_noop("семнадцатом"),
        _phrase_noop("восемнадцатом"),
        _phrase_noop("девятнадцатом")
    ]
        ]

ONES_F_ORD = [
    [
        _phrase_noop("нулевая"),
        _phrase_noop("первая"),
        _phrase_noop("вторая"),
        _phrase_noop("третья"),
        _phrase_noop("четвёртая"),
        _phrase_noop("пятая"),
        _phrase_noop("шестая"),
        _phrase_noop("седьмая"),
        _phrase_noop("восьмая"),
        _phrase_noop("девятая"),
        _phrase_noop("десятая"),
        _phrase_noop("одинадцатая"),
        _phrase_noop("двенадцатая"),
        _phrase_noop("тринадцатая"),
        _phrase_noop("четырнадцатая"),
        _phrase_noop("пятнадцатая"),
        _phrase_noop("шестнадцатая"),
        _phrase_noop("семнадцатая"),
        _phrase_noop("восемнадцатая"),
        _phrase_noop("девятнадцатая")
    ], [
        _phrase_noop("нулевой"),
        _phrase_noop("первой"),
        _phrase_noop("второй"),
        _phrase_noop("третьей"),
        _phrase_noop("четвёртой"),
        _phrase_noop("пятой"),
        _phrase_noop("шестой"),
        _phrase_noop("седьмой"),
        _phrase_noop("восьмой"),
        _phrase_noop("девятой"),
        _phrase_noop("десятой"),
        _phrase_noop("одинадцатой"),
        _phrase_noop("двенадцатой"),
        _phrase_noop("тринадцатой"),
        _phrase_noop("четырнадцатой"),
        _phrase_noop("пятнадцатой"),
        _phrase_noop("шестнадцатой"),
        _phrase_noop("семнадцатой"),
        _phrase_noop("восемнадцатой"),
        _phrase_noop("девятнадцатой")
    ], [
        _phrase_noop("нулевой"),
        _phrase_noop("первой"),
        _phrase_noop("второй"),
        _phrase_noop("третьей"),
        _phrase_noop("четвёртой"),
        _phrase_noop("пятой"),
        _phrase_noop("шестой"),
        _phrase_noop("седьмой"),
        _phrase_noop("восьмой"),
        _phrase_noop("девятой"),
        _phrase_noop("десятой"),
        _phrase_noop("одинадцатой"),
        _phrase_noop("двенадцатой"),
        _phrase_noop("тринадцатой"),
        _phrase_noop("четырнадцатой"),
        _phrase_noop("пятнадцатой"),
        _phrase_noop("шестнадцатой"),
        _phrase_noop("семнадцатой"),
        _phrase_noop("восемнадцатой"),
        _phrase_noop("девятнадцатой")
    ], [
        _phrase_noop("нулевую"),
        _phrase_noop("первую"),
        _phrase_noop("вторую"),
        _phrase_noop("третью"),
        _phrase_noop("четвёртую"),
        _phrase_noop("пятую"),
        _phrase_noop("шестую"),
        _phrase_noop("седьмую"),
        _phrase_noop("восьмую"),
        _phrase_noop("девятую"),
        _phrase_noop("десятую"),
        _phrase_noop("одинадцатую"),
        _phrase_noop("двенадцатую"),
        _phrase_noop("тринадцатую"),
        _phrase_noop("четырнадцатую"),
        _phrase_noop("пятнадцатую"),
        _phrase_noop("шестнадцатую"),
        _phrase_noop("семнадцатую"),
        _phrase_noop("восемнадцатую"),
        _phrase_noop("девятнадцатую")
    ], [
        _phrase_noop("нулевой"),
        _phrase_noop("первой"),
        _phrase_noop("второй"),
        _phrase_noop("третьей"),
        _phrase_noop("четвёртой"),
        _phrase_noop("пятой"),
        _phrase_noop("шестой"),
        _phrase_noop("седьмой"),
        _phrase_noop("восьмой"),
        _phrase_noop("девятой"),
        _phrase_noop("десятой"),
        _phrase_noop("одинадцатой"),
        _phrase_noop("двенадцатой"),
        _phrase_noop("тринадцатой"),
        _phrase_noop("четырнадцатой"),
        _phrase_noop("пятнадцатой"),
        _phrase_noop("шестнадцатой"),
        _phrase_noop("семнадцатой"),
        _phrase_noop("восемнадцатой"),
        _phrase_noop("девятнадцатой")
    ], [
        _phrase_noop("нулевой"),
        _phrase_noop("первой"),
        _phrase_noop("второй"),
        _phrase_noop("третьей"),
        _phrase_noop("четвёртой"),
        _phrase_noop("пятой"),
        _phrase_noop("шестой"),
        _phrase_noop("седьмой"),
        _phrase_noop("восьмой"),
        _phrase_noop("девятой"),
        _phrase_noop("десятой"),
        _phrase_noop("одинадцатой"),
        _phrase_noop("двенадцатой"),
        _phrase_noop("тринадцатой"),
        _phrase_noop("четырнадцатой"),
        _phrase_noop("пятнадцатой"),
        _phrase_noop("шестнадцатой"),
        _phrase_noop("семнадцатой"),
        _phrase_noop("восемнадцатой"),
        _phrase_noop("девятнадцатой")
    ]
        ]

ONES_M_ORD = [
    [
        _phrase_noop("нулевой"),
        _phrase_noop("первый"),
        _phrase_noop("второй"),
        _phrase_noop("третий"),
        _phrase_noop("четвёртый"),
        _phrase_noop("пятый"),
        _phrase_noop("шестой"),
        _phrase_noop("седьмой"),
        _phrase_noop("восьмой"),
        _phrase_noop("девятый"),
        _phrase_noop("десятый"),
        _phrase_noop("одинадцатый"),
        _phrase_noop("двенадцатый"),
        _phrase_noop("тринадцатый"),
        _phrase_noop("четырнадцатый"),
        _phrase_noop("пятнадцатый"),
        _phrase_noop("шестнадцатый"),
        _phrase_noop("семнадцатый"),
        _phrase_noop("восемнадцатый"),
        _phrase_noop("девятнадцатый")
    ], [
        _phrase_noop("нулевого"),
        _phrase_noop("первого"),
        _phrase_noop("второго"),
        _phrase_noop("третего"),
        _phrase_noop("четвёртого"),
        _phrase_noop("пятого"),
        _phrase_noop("шестого"),
        _phrase_noop("седьмого"),
        _phrase_noop("восьмого"),
        _phrase_noop("девятого"),
        _phrase_noop("десятого"),
        _phrase_noop("одинадцатого"),
        _phrase_noop("двенадцатого"),
        _phrase_noop("тринадцатого"),
        _phrase_noop("четырнадцатого"),
        _phrase_noop("пятнадцатого"),
        _phrase_noop("шестнадцатого"),
        _phrase_noop("семнадцатого"),
        _phrase_noop("восемнадцатого"),
        _phrase_noop("девятнадцатого")
    ], [
        _phrase_noop("нулевому"),
        _phrase_noop("первому"),
        _phrase_noop("второму"),
        _phrase_noop("третему"),
        _phrase_noop("четвёртому"),
        _phrase_noop("пятому"),
        _phrase_noop("шестому"),
        _phrase_noop("седьмому"),
        _phrase_noop("восьмому"),
        _phrase_noop("девятому"),
        _phrase_noop("десятому"),
        _phrase_noop("одинадцатому"),
        _phrase_noop("двенадцатому"),
        _phrase_noop("тринадцатому"),
        _phrase_noop("четырнадцатому"),
        _phrase_noop("пятнадцатому"),
        _phrase_noop("шестнадцатому"),
        _phrase_noop("семнадцатому"),
        _phrase_noop("восемнадцатому"),
        _phrase_noop("девятнадцатому")
    ], [
        _phrase_noop("нулевого"),
        _phrase_noop("первого"),
        _phrase_noop("второго"),
        _phrase_noop("третего"),
        _phrase_noop("четвёртого"),
        _phrase_noop("пятого"),
        _phrase_noop("шестого"),
        _phrase_noop("седьмого"),
        _phrase_noop("восьмого"),
        _phrase_noop("девятого"),
        _phrase_noop("десятого"),
        _phrase_noop("одинадцатого"),
        _phrase_noop("двенадцатого"),
        _phrase_noop("тринадцатого"),
        _phrase_noop("четырнадцатого"),
        _phrase_noop("пятнадцатого"),
        _phrase_noop("шестнадцатого"),
        _phrase_noop("семнадцатого"),
        _phrase_noop("восемнадцатого"),
        _phrase_noop("девятнадцатого")
    ], [
        _phrase_noop("нулевым"),
        _phrase_noop("первым"),
        _phrase_noop("вторым"),
        _phrase_noop("третьим"),
        _phrase_noop("четвёртым"),
        _phrase_noop("пятым"),
        _phrase_noop("шестым"),
        _phrase_noop("седьмым"),
        _phrase_noop("восьмым"),
        _phrase_noop("девятым"),
        _phrase_noop("десятым"),
        _phrase_noop("одинадцатым"),
        _phrase_noop("двенадцатым"),
        _phrase_noop("тринадцатым"),
        _phrase_noop("четырнадцатым"),
        _phrase_noop("пятнадцатым"),
        _phrase_noop("шестнадцатым"),
        _phrase_noop("семнадцатым"),
        _phrase_noop("восемнадцатым"),
        _phrase_noop("девятнадцатым")
    ], [
        _phrase_noop("нулевом"),
        _phrase_noop("первом"),
        _phrase_noop("втором"),
        _phrase_noop("третьем"),
        _phrase_noop("четвёртом"),
        _phrase_noop("пятом"),
        _phrase_noop("шестом"),
        _phrase_noop("седьмом"),
        _phrase_noop("восьмом"),
        _phrase_noop("девятом"),
        _phrase_noop("десятом"),
        _phrase_noop("одинадцатом"),
        _phrase_noop("двенадцатом"),
        _phrase_noop("тринадцатом"),
        _phrase_noop("четырнадцатом"),
        _phrase_noop("пятнадцатом"),
        _phrase_noop("шестнадцатом"),
        _phrase_noop("семнадцатом"),
        _phrase_noop("восемнадцатом"),
        _phrase_noop("девятнадцатом")
    ]
        ]

ONES_P = \
    [
        "", # этой формы нет
        _phrase_noop("одно"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ]

ONES_N = [
    [
        _phrase_noop("ноль"),
        _phrase_noop("одно"),
        _phrase_noop("два"),
        _phrase_noop("три"),
        _phrase_noop("четыре"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восемь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("ноля"),
        _phrase_noop("одного"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("нолю"),
        _phrase_noop("одному"),
        _phrase_noop("двум"),
        _phrase_noop("трём"),
        _phrase_noop("четырём"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("ноль"),
        _phrase_noop("одно"),
        _phrase_noop("два"),
        _phrase_noop("три"),
        _phrase_noop("четыре"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восьмь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("нолём"),
        _phrase_noop("одним"),
        _phrase_noop("двумя"),
        _phrase_noop("тремя"),
        _phrase_noop("четырьмя"),
        _phrase_noop("пятью"),
        _phrase_noop("шестью"),
        _phrase_noop("семью"),
        _phrase_noop("восьмью"),
        _phrase_noop("девятью"),
        _phrase_noop("десятью"),
        _phrase_noop("одинадцатью"),
        _phrase_noop("двенадцатью"),
        _phrase_noop("тринадцатью"),
        _phrase_noop("четырнадцатью"),
        _phrase_noop("пятнадцатью"),
        _phrase_noop("шестнадцатью"),
        _phrase_noop("семнадцатью"),
        _phrase_noop("восемнадцатью"),
        _phrase_noop("девятнадцатью")
    ], [
        _phrase_noop("ноле"),
        _phrase_noop("одном"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ]
        ]

ONES_F = [
    [
        _phrase_noop("ноль"),
        _phrase_noop("одна"),
        _phrase_noop("две"),
        _phrase_noop("три"),
        _phrase_noop("четыре"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восемь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("ноля"),
        _phrase_noop("одной"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("нолю"),
        _phrase_noop("одной"),
        _phrase_noop("двум"),
        _phrase_noop("трём"),
        _phrase_noop("четырём"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("ноль"),
        _phrase_noop("одну"),
        _phrase_noop("две"),
        _phrase_noop("три"),
        _phrase_noop("четыре"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восемь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("нолём"),
        _phrase_noop("одной"),
        _phrase_noop("двумя"),
        _phrase_noop("тремя"),
        _phrase_noop("четырьмя"),
        _phrase_noop("пятью"),
        _phrase_noop("шестью"),
        _phrase_noop("семью"),
        _phrase_noop("восьмью"),
        _phrase_noop("девятью"),
        _phrase_noop("десятью"),
        _phrase_noop("одинадцатью"),
        _phrase_noop("двенадцатью"),
        _phrase_noop("тринадцатью"),
        _phrase_noop("четырнадцатью"),
        _phrase_noop("пятнадцатью"),
        _phrase_noop("шестнадцатью"),
        _phrase_noop("семнадцатью"),
        _phrase_noop("восемнадцатью"),
        _phrase_noop("девятнадцатью")
    ], [
        _phrase_noop("ноле"),
        _phrase_noop("одной"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ]
        ]

ONES_M = [
    [
        _phrase_noop("ноль"),
        _phrase_noop("один"),
        _phrase_noop("два"),
        _phrase_noop("три"),
        _phrase_noop("четыре"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восемь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("ноля"),
        _phrase_noop("одного"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("нолю"),
        _phrase_noop("одному"),
        _phrase_noop("двум"),
        _phrase_noop("трём"),
        _phrase_noop("четырём"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ], [
        _phrase_noop("ноль"),
        _phrase_noop("одного"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пять"),
        _phrase_noop("шесть"),
        _phrase_noop("семь"),
        _phrase_noop("восьмь"),
        _phrase_noop("девять"),
        _phrase_noop("десять"),
        _phrase_noop("одинадцать"),
        _phrase_noop("двенадцать"),
        _phrase_noop("тринадцать"),
        _phrase_noop("четырнадцать"),
        _phrase_noop("пятнадцать"),
        _phrase_noop("шестнадцать"),
        _phrase_noop("семнадцать"),
        _phrase_noop("восемнадцать"),
        _phrase_noop("девятнадцать")
    ], [
        _phrase_noop("нолём"),
        _phrase_noop("одним"),
        _phrase_noop("двумя"),
        _phrase_noop("тремя"),
        _phrase_noop("четырьмя"),
        _phrase_noop("пятью"),
        _phrase_noop("шестью"),
        _phrase_noop("семью"),
        _phrase_noop("восьмью"),
        _phrase_noop("девятью"),
        _phrase_noop("десятью"),
        _phrase_noop("одинадцатью"),
        _phrase_noop("двенадцатью"),
        _phrase_noop("тринадцатью"),
        _phrase_noop("четырнадцатью"),
        _phrase_noop("пятнадцатью"),
        _phrase_noop("шестнадцатью"),
        _phrase_noop("семнадцатью"),
        _phrase_noop("восемнадцатью"),
        _phrase_noop("девятнадцатью")
    ], [
        _phrase_noop("ноле"),
        _phrase_noop("одном"),
        _phrase_noop("двух"),
        _phrase_noop("трёх"),
        _phrase_noop("четырёх"),
        _phrase_noop("пяти"),
        _phrase_noop("шести"),
        _phrase_noop("семи"),
        _phrase_noop("восьми"),
        _phrase_noop("девяти"),
        _phrase_noop("десяти"),
        _phrase_noop("одинадцати"),
        _phrase_noop("двенадцати"),
        _phrase_noop("тринадцати"),
        _phrase_noop("четырнадцати"),
        _phrase_noop("пятнадцати"),
        _phrase_noop("шестнадцати"),
        _phrase_noop("семнадцати"),
        _phrase_noop("восемнадцати"),
        _phrase_noop("девятнадцати")
    ]
        ]

HUNDREDS = [
    [
        _phrase_noop("сто"),
        _phrase_noop("двести"),
        _phrase_noop("триста"),
        _phrase_noop("четыреста"),
        _phrase_noop("пятьсот"),
        _phrase_noop("шестьсот"),
        _phrase_noop("семьсот"),
        _phrase_noop("восемьсот"),
        _phrase_noop("девятьсот")
    ], [
        _phrase_noop("ста"),
        _phrase_noop("двухсот"),
        _phrase_noop("трёхсот"),
        _phrase_noop("четырёхсот"),
        _phrase_noop("пятисот"),
        _phrase_noop("шестисот"),
        _phrase_noop("семисот"),
        _phrase_noop("восьмисот"),
        _phrase_noop("девятисот")
    ], [
        _phrase_noop("ста"),
        _phrase_noop("двумстам"),
        _phrase_noop("тремстам"),
        _phrase_noop("четырёмстам"),
        _phrase_noop("пятистам"),
        _phrase_noop("шестистам"),
        _phrase_noop("семистам"),
        _phrase_noop("восьмистам"),
        _phrase_noop("девятистам")
    ], [
        _phrase_noop("сотню"),
        _phrase_noop("двести"),
        _phrase_noop("триста"),
        _phrase_noop("четыреста"),
        _phrase_noop("пятьсот"),
        _phrase_noop("шестьсот"),
        _phrase_noop("семьсот"),
        _phrase_noop("восемьсот"),
        _phrase_noop("девятьсот")
    ], [
        _phrase_noop("сотней"),
        _phrase_noop("двумястами"),
        _phrase_noop("тремястами"),
        _phrase_noop("четырьмястами"),
        _phrase_noop("пятистами"),
        _phrase_noop("шестистами"),
        _phrase_noop("семистами"),
        _phrase_noop("восьмистами"),
        _phrase_noop("девятистами")
    ], [
        _phrase_noop("сотне"),
        _phrase_noop("двухстах"),
        _phrase_noop("трёхстах"),
        _phrase_noop("четырёхстах"),
        _phrase_noop("пятистах"),
        _phrase_noop("шестистах"),
        _phrase_noop("семистах"),
        _phrase_noop("восьмистах"),
        _phrase_noop("девятистах")
    ]
        ]

HUNDREDS_M_ORD = [
    [
        _phrase_noop("сотый"),
        _phrase_noop("двухсотый"),
        _phrase_noop("трёхсотый"),
        _phrase_noop("четырёхсотый"),
        _phrase_noop("пятисотый"),
        _phrase_noop("шестисотый"),
        _phrase_noop("семисотый"),
        _phrase_noop("восьмисотый"),
        _phrase_noop("девятисотый")
    ], [
        _phrase_noop("сотого"),
        _phrase_noop("двухсотого"),
        _phrase_noop("трёхсотого"),
        _phrase_noop("четырёхсотого"),
        _phrase_noop("пятисотого"),
        _phrase_noop("шестисотого"),
        _phrase_noop("семисотого"),
        _phrase_noop("восьмисотого"),
        _phrase_noop("девятисотого")
    ], [
        _phrase_noop("сотому"),
        _phrase_noop("двухсотому"),
        _phrase_noop("трёхсотому"),
        _phrase_noop("четырёхсотому"),
        _phrase_noop("пятисотому"),
        _phrase_noop("шестисотому"),
        _phrase_noop("семисотому"),
        _phrase_noop("восьмисотому"),
        _phrase_noop("девятисотому")
    ], [
        _phrase_noop("сотого"),
        _phrase_noop("двухсотого"),
        _phrase_noop("трёхсотого"),
        _phrase_noop("четырёхсотого"),
        _phrase_noop("пятисотого"),
        _phrase_noop("шестисотого"),
        _phrase_noop("семисотого"),
        _phrase_noop("восьмисотого"),
        _phrase_noop("девятисотого")
    ], [
        _phrase_noop("сотым"),
        _phrase_noop("двухсотым"),
        _phrase_noop("трёхсотым"),
        _phrase_noop("четырёхсотым"),
        _phrase_noop("пятисотым"),
        _phrase_noop("шестисотым"),
        _phrase_noop("семисотым"),
        _phrase_noop("восьмисотым"),
        _phrase_noop("девятисотым")
    ], [
        _phrase_noop("сотом"),
        _phrase_noop("двухсотом"),
        _phrase_noop("трёхсотом"),
        _phrase_noop("четырёхсотом"),
        _phrase_noop("пятисотом"),
        _phrase_noop("шестисотом"),
        _phrase_noop("семисотом"),
        _phrase_noop("восьмисотом"),
        _phrase_noop("девятисотом")
    ]
        ]

HUNDREDS_F_ORD = [
    [
        _phrase_noop("сотая"),
        _phrase_noop("двухсотая"),
        _phrase_noop("трёхсотая"),
        _phrase_noop("четырёхсотая"),
        _phrase_noop("пятисотая"),
        _phrase_noop("шестисотая"),
        _phrase_noop("семисотая"),
        _phrase_noop("восьмисотая"),
        _phrase_noop("девятисотая")
    ], [
        _phrase_noop("сотой"),
        _phrase_noop("двухсотой"),
        _phrase_noop("трёхсотой"),
        _phrase_noop("четырёхсотой"),
        _phrase_noop("пятисотой"),
        _phrase_noop("шестисотой"),
        _phrase_noop("семисотой"),
        _phrase_noop("восьмисотой"),
        _phrase_noop("девятисотой")
    ], [
        _phrase_noop("сотой"),
        _phrase_noop("двухсотой"),
        _phrase_noop("трёхсотой"),
        _phrase_noop("четырёхсотой"),
        _phrase_noop("пятисотой"),
        _phrase_noop("шестисотой"),
        _phrase_noop("семисотой"),
        _phrase_noop("восьмисотой"),
        _phrase_noop("девятисотой")
    ], [
        _phrase_noop("сотую"),
        _phrase_noop("двухсотую"),
        _phrase_noop("трёхсотую"),
        _phrase_noop("четырёхсотую"),
        _phrase_noop("пятисотую"),
        _phrase_noop("шестисотую"),
        _phrase_noop("семисотую"),
        _phrase_noop("восьмисотую"),
        _phrase_noop("девятисотую")
    ], [
        _phrase_noop("сотой"),
        _phrase_noop("двухсотой"),
        _phrase_noop("трёхсотой"),
        _phrase_noop("четырёхсотой"),
        _phrase_noop("пятисотой"),
        _phrase_noop("шестисотой"),
        _phrase_noop("семисотой"),
        _phrase_noop("восьмисотой"),
        _phrase_noop("девятисотой")
    ], [
        _phrase_noop("сотой"),
        _phrase_noop("двухсотой"),
        _phrase_noop("трёхсотой"),
        _phrase_noop("четырёхсотой"),
        _phrase_noop("пятисотой"),
        _phrase_noop("шестисотой"),
        _phrase_noop("семисотой"),
        _phrase_noop("восьмисотой"),
        _phrase_noop("девятисотой")
    ]
        ]

HUNDREDS_N_ORD = [
    [
        _phrase_noop("сотое"),
        _phrase_noop("двухсотое"),
        _phrase_noop("трёхсотое"),
        _phrase_noop("четырёхсотое"),
        _phrase_noop("пятисотое"),
        _phrase_noop("шестисотое"),
        _phrase_noop("семисотое"),
        _phrase_noop("восьмисотое"),
        _phrase_noop("девятисотое")
    ], [
        _phrase_noop("сотого"),
        _phrase_noop("двухсотого"),
        _phrase_noop("трёхсотого"),
        _phrase_noop("четырёхсотого"),
        _phrase_noop("пятисотого"),
        _phrase_noop("шестисотого"),
        _phrase_noop("семисотого"),
        _phrase_noop("восьмисотого"),
        _phrase_noop("девятисотого")
    ], [
        _phrase_noop("сотому"),
        _phrase_noop("двухсотому"),
        _phrase_noop("трёхсотому"),
        _phrase_noop("четырёхсотому"),
        _phrase_noop("пятисотому"),
        _phrase_noop("шестисотому"),
        _phrase_noop("семисотому"),
        _phrase_noop("восьмисотому"),
        _phrase_noop("девятисотому")
    ], [
        _phrase_noop("сотое"),
        _phrase_noop("двухсотое"),
        _phrase_noop("трёхсотое"),
        _phrase_noop("четырёхсотое"),
        _phrase_noop("пятисотое"),
        _phrase_noop("шестисотое"),
        _phrase_noop("семисотое"),
        _phrase_noop("восьмисотое"),
        _phrase_noop("девятисотое")
    ], [
        _phrase_noop("сотым"),
        _phrase_noop("двухсотым"),
        _phrase_noop("трёхсотым"),
        _phrase_noop("четырёхсотым"),
        _phrase_noop("пятисотым"),
        _phrase_noop("шестисотым"),
        _phrase_noop("семисотым"),
        _phrase_noop("восьмисотым"),
        _phrase_noop("девятисотым")
    ], [
        _phrase_noop("сотом"),
        _phrase_noop("двухсотом"),
        _phrase_noop("трёхсотом"),
        _phrase_noop("четырёхсотом"),
        _phrase_noop("пятисотом"),
        _phrase_noop("шестисотом"),
        _phrase_noop("семисотом"),
        _phrase_noop("восьмисотом"),
        _phrase_noop("девятисотом")
    ]
        ]

MONTH = [
    [
        _phrase_noop("январь"),
        _phrase_noop("февраль"),
        _phrase_noop("март"),
        _phrase_noop("апрель"),
        _phrase_noop("май"),
        _phrase_noop("июнь"),
        _phrase_noop("июль"),
        _phrase_noop("август"),
        _phrase_noop("сентябрь"),
        _phrase_noop("октябрь"),
        _phrase_noop("ноябрь"),
        _phrase_noop("декабрь")
    ], [
        _phrase_noop("января"),
        _phrase_noop("февраля"),
        _phrase_noop("марта"),
        _phrase_noop("апреля"),
        _phrase_noop("мая"),
        _phrase_noop("июня"),
        _phrase_noop("июля"),
        _phrase_noop("августа"),
        _phrase_noop("сентября"),
        _phrase_noop("октября"),
        _phrase_noop("ноября"),
        _phrase_noop("декабря")
    ], [
        _phrase_noop("январю"),
        _phrase_noop("февралю"),
        _phrase_noop("марту"),
        _phrase_noop("апрелю"),
        _phrase_noop("маю"),
        _phrase_noop("июню"),
        _phrase_noop("июлю"),
        _phrase_noop("августу"),
        _phrase_noop("сентябрю"),
        _phrase_noop("октябрю"),
        _phrase_noop("ноябрю"),
        _phrase_noop("декабрю")
    ], [
        _phrase_noop("январь"),
        _phrase_noop("февраль"),
        _phrase_noop("март"),
        _phrase_noop("апрель"),
        _phrase_noop("май"),
        _phrase_noop("июнь"),
        _phrase_noop("июль"),
        _phrase_noop("август"),
        _phrase_noop("сентябрь"),
        _phrase_noop("октябрь"),
        _phrase_noop("ноябрь"),
        _phrase_noop("декабрь")
    ], [
        _phrase_noop("январём"),
        _phrase_noop("февралём"),
        _phrase_noop("мартом"),
        _phrase_noop("апрелем"),
        _phrase_noop("маем"),
        _phrase_noop("июнем"),
        _phrase_noop("июлем"),
        _phrase_noop("августом"),
        _phrase_noop("сентябрём"),
        _phrase_noop("октябрём"),
        _phrase_noop("ноябрём"),
        _phrase_noop("декабрём")
    ], [
        _phrase_noop("январе"),
        _phrase_noop("феврале"),
        _phrase_noop("марте"),
        _phrase_noop("апреле"),
        _phrase_noop("мае"),
        _phrase_noop("июне"),
        _phrase_noop("июле"),
        _phrase_noop("августе"),
        _phrase_noop("сентябре"),
        _phrase_noop("октябре"),
        _phrase_noop("ноябре"),
        _phrase_noop("декабре")
    ]
        ]

def ncvt(singular, plural1, plural2, num):
    if (num % 10 == 1 and num % 100 != 11):
        return singular
    elif (num % 10 >= 2 and num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20)):
        return plural1
    else:
        return plural2

def gcvt(masculine, feminine, neuter, gender, case):
    if (gender == GENDER_MASCULINE):
        return masculine[case]
    if (gender == GENDER_FEMININE):
        return feminine[case]
    if (gender == GENDER_NEUTER):
        return neuter[case]

def parse_case(flags):
    case = CASE_NOMINATIVE
    if (flags != None):
        if ('Cg' in flags):
            case = CASE_GENITIVE
        elif ('Cd' in flags):
            case = CASE_DATIVE
        elif ('Ca' in flags):
            case = CASE_ACCUSATIVE
        elif ('Ci' in flags):
            case = CASE_INSTRUMENTAL
        elif ('Cp' in flags):
            case = CASE_PREPOSITIONAL
    return case

def sayNumber(number, ordinal, flags):
    #
    # Этот метод распознает род числительного:
    # M (masculine) - мужской (по умолчанию)
    # F (feminine) - женский
    # N (neuter) - средний
    #
    gender = GENDER_MASCULINE
    case = parse_case(flags)
    if (flags != None):
        if ('N' in flags):
            gender = GENDER_NEUTER
        elif ('F' in flags):
            gender = GENDER_FEMININE
    return _sayNumber(number, ordinal, gender, case)

def _sayNumber(number, ordinal, gender, case):
    retval = ""
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("менее минус одного миллиарда")
        else:
            retval = _phrase_noop("более миллиарда")
    else:
        if (minus):
            retval = _phrase_noop("минус") + " "
        num = number % 1000
        num_thousands = int(number / 1000) % 1000
        num_millions = int(number / 1000000) % 1000

        # millions
        if (num_millions > 0):
            tmp_ordinal = ordinal
            tmp_case = case
            if ((num + num_thousands) > 0):
                tmp_ordinal = False
                tmp_case = CASE_NOMINATIVE
            if (tmp_ordinal):
                retval += __say_number(num_millions,
                                            True, IS_PREFIX) + " "
                retval += gcvt([
                                    _phrase_noop("милионный"),
                                    _phrase_noop("милионного"),
                                    _phrase_noop("милионному"),
                                    _phrase_noop("милионный"),
                                    _phrase_noop("милионным"),
                                    _phrase_noop("милионном")
                               ], [
                                    _phrase_noop("милионная"),
                                    _phrase_noop("милионной"),
                                    _phrase_noop("милионной"),
                                    _phrase_noop("милионную"),
                                    _phrase_noop("милионной"),
                                    _phrase_noop("милионной")
                               ], [
                                    _phrase_noop("милионное"),
                                    _phrase_noop("милионного"),
                                    _phrase_noop("милионному"),
                                    _phrase_noop("милионное"),
                                    _phrase_noop("милионным"),
                                    _phrase_noop("милионном"),
                               ], gender, case) + " "
            else:
                retval += __say_number(num_millions,
                                            False,
                                            GENDER_MASCULINE,
                                            tmp_case) + " "
                singular = [
                            _phrase_noop("миллион"),
                            _phrase_noop("миллиона"),
                            _phrase_noop("миллиону"),
                            _phrase_noop("миллион"),
                            _phrase_noop("миллионом"),
                            _phrase_noop("миллионе")
                           ][tmp_case]
                plural1 = [
                            _phrase_noop("миллиона"),
                            _phrase_noop("миллионов"),
                            _phrase_noop("миллионам"),
                            _phrase_noop("миллиона"),
                            _phrase_noop("миллионами"),
                            _phrase_noop("миллионах")
                           ][tmp_case]
                plural2 = [
                            _phrase_noop("миллионов"),
                            _phrase_noop("миллионов"),
                            _phrase_noop("миллионам"),
                            _phrase_noop("миллионов"),
                            _phrase_noop("миллионами"),
                            _phrase_noop("миллионах")
                          ][tmp_case]
                retval += ncvt(singular, plural1, plural2, num_millions) + " "

        # thousands
        if (num_thousands > 0):
            tmp_ordinal = ordinal
            tmp_case = case
            if (num > 0):
                tmp_ordinal = False
                tmp_case = CASE_NOMINATIVE

            if (tmp_ordinal):
                retval += __say_number(num_thousands,
                                            True, IS_PREFIX) + " "
                retval += gcvt([
                                    _phrase_noop("тысячный"),
                                    _phrase_noop("тысячного"),
                                    _phrase_noop("тысячному"),
                                    _phrase_noop("тысячный"),
                                    _phrase_noop("тысячным"),
                                    _phrase_noop("тысячном")
                               ], [
                                    _phrase_noop("тысячная"),
                                    _phrase_noop("тысячной"),
                                    _phrase_noop("тысячной"),
                                    _phrase_noop("тысячную"),
                                    _phrase_noop("тысячной"),
                                    _phrase_noop("тысячной")
                               ], [
                                    _phrase_noop("тысячное"),
                                    _phrase_noop("тысячного"),
                                    _phrase_noop("тысячному"),
                                    _phrase_noop("тысячное"),
                                    _phrase_noop("тысячным"),
                                    _phrase_noop("тысячном"),
                               ], gender, case) + " "
            else:
                retval += __say_number(num_thousands,
                                            False,
                                            GENDER_FEMININE,
                                            tmp_case) + " "
                singular = [
                                _phrase_noop("тысяча"),
                                _phrase_noop("тысячи"),
                                _phrase_noop("тысяче"),
                                _phrase_noop("тысячу"),
                                _phrase_noop("тысячью"),
                                _phrase_noop("тысяче"),
                           ][tmp_case]
                plural1 = [
                                _phrase_noop("тысячи"),
                                _phrase_noop("тысяч"),
                                _phrase_noop("тысячам"),
                                _phrase_noop("тысячи"),
                                _phrase_noop("тысячами"),
                                _phrase_noop("тысячах"),
                          ][tmp_case]
                plural2 = [
                            _phrase_noop("тысяч"),
                            _phrase_noop("тысяч"),
                            _phrase_noop("тысячам"),
                            _phrase_noop("тысяч"),
                            _phrase_noop("тысячами"),
                            _phrase_noop("тысячах"),
                          ][tmp_case]
                retval += ncvt(singular, plural1, plural2, num_thousands) + " "

        # the rest
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal, gender, case)
    return retval.rstrip()

def __say_number(number, ordinal, option, case = CASE_NOMINATIVE):
    retval = ""
    if (number % 100 == 0 and number != 0):
        if (number > 0):
            # целая сотня
            idx = int(number / 100) - 1
            if (option == IS_PREFIX):
                return HUNDREDS[CASE_NOMINATIVE][idx]
            if (ordinal):
                if (option == GENDER_MASCULINE):
                    return HUNDREDS_M_ORD[case][idx]
                if (option == GENDER_FEMININE):
                    return HUNDREDS_F_ORD[case][idx]
                if (option == GENDER_NEUTER):
                    return HUNDREDS_N_ORD[case][idx]
            else:
                return HUNDREDS[case][idx]
    else:
        if (number > 100):
            retval += HUNDREDS[CASE_NOMINATIVE][int(number / 100) - 1] + " "
        num = number % 100
        if (num < 20):
            if (ordinal):
                if (option == GENDER_MASCULINE):
                    retval += ONES_M_ORD[case][num]
                elif (option == GENDER_FEMININE):
                    retval += ONES_F_ORD[case][num]
                elif (option == GENDER_NEUTER):
                    retval += ONES_N_ORD[case][num]
                elif (option == IS_PREFIX):
                    retval += ONES_P[num]
            else:
                if (option == GENDER_MASCULINE):
                    retval += ONES_M[case][num]
                elif (option == GENDER_FEMININE):
                    retval += ONES_F[case][num]
                elif (option == GENDER_NEUTER):
                    retval += ONES_N[case][num]
        elif (num % 10 == 0):
            # целый десяток
            idx = int(num / 10) - 2
            if (ordinal):
                if (option == GENDER_MASCULINE):
                    retval += TENS_M_ORD[case][idx]
                elif (option == GENDER_FEMININE):
                    retval += TENS_F_ORD[case][idx]
                elif (option == GENDER_NEUTER):
                    retval += TENS_N_ORD[case][idx]
                elif (option == IS_PREFIX):
                    retval += TENS_P[idx]
            else:
                retval += TENS[case][idx]
        else:
            retval += TENS[CASE_NOMINATIVE][int(num / 10) - 2] + " "
            idx = num % 10
            if (ordinal):
                if (option == GENDER_MASCULINE):
                    retval += ONES_M_ORD[case][idx]
                elif (option == GENDER_FEMININE):
                    retval += ONES_F_ORD[case][idx]
                elif (option == GENDER_NEUTER):
                    retval += ONES_N_ORD[case][idx]
                elif (option == IS_PREFIX):
                    retval += ONES_P[idx]
            else:
                if (option == GENDER_MASCULINE):
                    retval += ONES_M[case][idx]
                elif (option == GENDER_FEMININE):
                    retval += ONES_F[case][idx]
                elif (option == GENDER_NEUTER):
                    retval += ONES_N[case][idx]
    return retval

def sayDigits(num, flags):
    retval = ""
    for i in str(num):
        if (not i.isdigit()):
            continue
        retval += ONES_M[0][int(i)] + " "

    return retval.rstrip()

def sayDatetime(date_time, say_date, say_time, say_seconds, flags):
    case = parse_case(flags)
    verbose_time = True
    if ('V' in flags):
        verbose_time = False
    retval = ""

    now = datetime.datetime.now(date_time.tzinfo)

    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("сегодня") + " "
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("вчера") + " "
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("завтра") + " "
        else:
            retval += _sayNumber(date_time.day, True, GENDER_MASCULINE, case) + " "
            retval += MONTH[CASE_GENITIVE][date_time.month - 1] + " "
            retval += _sayNumber(date_time.year, True, GENDER_MASCULINE, CASE_GENITIVE) + " "
            retval += _phrase_noop("года") + " "

    if (say_time):
        retval += _phrase_noop("в") + " "
        retval += _sayNumber(date_time.hour, False, GENDER_MASCULINE, CASE_ACCUSATIVE) + " "
        if (verbose_time):
            retval += ncvt(_phrase_noop("час"),
                           _phrase_noop("часаа"), # ударение на последнем слоге
                           _phrase_noop("часов"), date_time.hour) + " "
        minute = date_time.minute
        if (minute < 10):
            retval += _phrase_noop("ноль") + " "
        retval += _sayNumber(minute, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        if (verbose_time):
            retval += ncvt(_phrase_noop("минуту"),
                           _phrase_noop("минуты"),
                           _phrase_noop("минут"), minute) + " "
        if (say_seconds):
            secs = date_time.second
            retval += _phrase_noop("и") + " "
            retval += _sayNumber(secs, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
            if (verbose_time):
                retval += ncvt(_phrase_noop("секунду"),
                               _phrase_noop("секунды"),
                               _phrase_noop("секунд"), secs) + " "
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
        retval += _sayNumber(hours, False, GENDER_MASCULINE, CASE_NOMINATIVE) + " "
        retval += ncvt(_phrase_noop("час"),
                       _phrase_noop("часаа"),
                       _phrase_noop("часов"), hours) + " "
    if (minutes > 0):
        if (hours > 0 and s == 0):
            retval += _phrase_noop("и") + " "
        retval += _sayNumber(minutes, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        retval += ncvt(_phrase_noop("минуту"),
                       _phrase_noop("минуты"),
                       _phrase_noop("минут"), minutes) + " "
    if (s > 0):
        if (hours > 0 or minutes > 0):
            retval += _phrase_noop("и") + " "
        retval += _sayNumber(s, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        retval += ncvt(_phrase_noop("секунду"),
                       _phrase_noop("секунды"),
                       _phrase_noop("секунд"), s) + " "
    return retval.rstrip()
