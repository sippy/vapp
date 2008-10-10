#!/usr/local/bin/python
# -*- coding: KOI8-R -*-
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

__all__ = [ "RU" ]

CASE_NOMINATIVE	    = 0 # ������������ ����� [Cn] (default)
CASE_GENITIVE	    = 1 # ����������� �����  [Cg]
CASE_DATIVE	    = 2 # ��������� �����    [Cd]
CASE_ACCUSATIVE	    = 3 # ����������� �����  [Ca]
CASE_INSTRUMENTAL   = 4 # ������������ ����� [Ci]
CASE_PREPOSITIONAL  = 5 # ���������� �����   [Cp]

GENDER_NEUTER	    = 0	# [N]
GENDER_MASCULINE    = 1 # default
GENDER_FEMININE	    = 2 # [F]
#
# IS_PREFIX ������������ ��� ��������� ����� ����������� �������������:
#
#   "����"-���������
#
# � �� ����� ��� �������� GENDER_FEMININE ����
#
#   "������"
#
IS_PREFIX	    = 3

def _phrase_noop(str):
    return unicode(str, 'koi8-r')

TENS_P = \
    [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("���������")
    ]

TENS = [
    [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("���������")
    ]
	]

TENS_N_ORD = [
    [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ]
	]

TENS_F_ORD = [
    [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ]
	]

TENS_M_ORD = [
    [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("����������")
    ]
	]

ONES_N_ORD = [
    [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("���ף�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("��������������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("���ף�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("��������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ]
	]

ONES_F_ORD = [
    [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ]
	]

ONES_M_ORD = [
    [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("��������������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("��������������")
    ], [
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("������������"),
	_phrase_noop("�������������"),
	_phrase_noop("������������"),
	_phrase_noop("��������������"),
	_phrase_noop("��������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("���ף����"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ]
	]

ONES_P = \
    [
	"", # ���� ����� ���
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ]

ONES_N = [
    [
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("���"),
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("���"),
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("��̣�"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("��������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�����"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ]
	]

ONES_F = [
    [
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("���"),
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("���"),
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("��̣�"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("��������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�����"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ]
	]

ONES_M = [
    [
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("���"),
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("��̣�"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("��������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("�����"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�����������"),
	_phrase_noop("������������"),
	_phrase_noop("�����������"),
	_phrase_noop("�������������"),
	_phrase_noop("�������������")
    ], [
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("�ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ]
	]

HUNDREDS = [
    [
	_phrase_noop("���"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("���������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("���"),
	_phrase_noop("�������"),
	_phrase_noop("�ң����"),
	_phrase_noop("����ң����"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("���������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("���"),
	_phrase_noop("��������"),
	_phrase_noop("��������"),
	_phrase_noop("����ң�����"),
	_phrase_noop("��������"),
	_phrase_noop("���������"),
	_phrase_noop("��������"),
	_phrase_noop("����������"),
	_phrase_noop("����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("������"),
	_phrase_noop("���������"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("���������"),
	_phrase_noop("���������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("����������"),
	_phrase_noop("�������������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("��������"),
	_phrase_noop("�ң�����"),
	_phrase_noop("����ң�����"),
	_phrase_noop("��������"),
	_phrase_noop("���������"),
	_phrase_noop("��������"),
	_phrase_noop("����������"),
	_phrase_noop("����������")
    ]
	]

HUNDREDS_M_ORD = [
    [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�ң�������"),
	_phrase_noop("����ң�������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�ң�������"),
	_phrase_noop("����ң�������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�ң�������"),
	_phrase_noop("����ң�������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ]
	]

HUNDREDS_F_ORD = [
    [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ]
	]

HUNDREDS_N_ORD = [
    [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�ң�������"),
	_phrase_noop("����ң�������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("����������"),
	_phrase_noop("�ң�������"),
	_phrase_noop("����ң�������"),
	_phrase_noop("����������"),
	_phrase_noop("�����������"),
	_phrase_noop("����������"),
	_phrase_noop("������������"),
	_phrase_noop("������������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ], [
	_phrase_noop("�����"),
	_phrase_noop("���������"),
	_phrase_noop("�ң������"),
	_phrase_noop("����ң������"),
	_phrase_noop("���������"),
	_phrase_noop("����������"),
	_phrase_noop("���������"),
	_phrase_noop("�����������"),
	_phrase_noop("�����������")
    ]
	]

MONTH = [
    [
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("���"),
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("�������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("���"),
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("�������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("���"),
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("�������")
    ], [
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("���"),
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("�������")
    ], [
	_phrase_noop("����ң�"),
	_phrase_noop("�����̣�"),
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("����"),
	_phrase_noop("�����"),
	_phrase_noop("�����"),
	_phrase_noop("��������"),
	_phrase_noop("������ң�"),
	_phrase_noop("�����ң�"),
	_phrase_noop("����ң�"),
	_phrase_noop("�����ң�")
    ], [
	_phrase_noop("������"),
	_phrase_noop("�������"),
	_phrase_noop("�����"),
	_phrase_noop("������"),
	_phrase_noop("���"),
	_phrase_noop("����"),
	_phrase_noop("����"),
	_phrase_noop("�������"),
	_phrase_noop("��������"),
	_phrase_noop("�������"),
	_phrase_noop("������"),
	_phrase_noop("�������")
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
    # ���� ����� ���������� ��� �������������:
    # M (masculine) - ������� (�� ���������)
    # F (feminine) - �������
    # N (neuter) - �������
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
    retval = unicode("")
    minus = False
    if (number < 0):
        number = -number
        minus = True
    if (number >= 1000000000):
        if (minus):
            retval = _phrase_noop("����� ����� ������ ���������")
        else:
            retval = _phrase_noop("����� ���������")
    else:
        if (minus):
            retval = _phrase_noop("�����") + " "
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
                                    _phrase_noop("���������"),
                                    _phrase_noop("����������"),
                                    _phrase_noop("����������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������")
                               ], [
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������")
                               ], [
                                    _phrase_noop("���������"),
                                    _phrase_noop("����������"),
                                    _phrase_noop("����������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                               ], gender, case) + " "
            else:
                retval += __say_number(num_millions,
                                            False,
                                            GENDER_MASCULINE,
                                            tmp_case) + " "
                singular = [
                            _phrase_noop("�������"),
                            _phrase_noop("��������"),
                            _phrase_noop("��������"),
                            _phrase_noop("�������"),
                            _phrase_noop("���������"),
                            _phrase_noop("��������")
                           ][tmp_case]
                plural1 = [
                            _phrase_noop("��������"),
                            _phrase_noop("���������"),
                            _phrase_noop("���������"),
                            _phrase_noop("��������"),
                            _phrase_noop("����������"),
                            _phrase_noop("���������")
                           ][tmp_case]
                plural2 = [
                            _phrase_noop("���������"),
                            _phrase_noop("���������"),
                            _phrase_noop("���������"),
                            _phrase_noop("���������"),
                            _phrase_noop("����������"),
                            _phrase_noop("���������")
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
                                    _phrase_noop("��������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������")
                               ], [
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������")
                               ], [
                                    _phrase_noop("��������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("���������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                                    _phrase_noop("��������"),
                               ], gender, case) + " "
            else:
                retval += __say_number(num_thousands,
                                            False,
                                            GENDER_FEMININE,
                                            tmp_case) + " "
                singular = [
                                _phrase_noop("������"), 
                                _phrase_noop("������"), 
                                _phrase_noop("������"), 
                                _phrase_noop("������"), 
                                _phrase_noop("�������"), 
                                _phrase_noop("������"), 
                           ][tmp_case]
                plural1 = [
                                _phrase_noop("������"), 
                                _phrase_noop("�����"), 
                                _phrase_noop("�������"), 
                                _phrase_noop("������"), 
                                _phrase_noop("��������"), 
                                _phrase_noop("�������"), 
                          ][tmp_case]
                plural2 = [
                            _phrase_noop("�����"),
                            _phrase_noop("�����"),
                            _phrase_noop("�������"),
                            _phrase_noop("�����"),
                            _phrase_noop("��������"),
                            _phrase_noop("�������"),
                          ][tmp_case]
                retval += ncvt(singular, plural1, plural2, num_thousands) + " "

        # the rest
        if (num > 0 or number == 0):
            retval += __say_number(num, ordinal, gender, case)
    return retval.rstrip()

def __say_number(number, ordinal, option, case = CASE_NOMINATIVE):
    retval = unicode("")
    if (number % 100 == 0 and number != 0):
        if (number > 0):
            # ����� �����
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
            # ����� �������
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
    retval = unicode("")

    now = datetime.datetime.now(date_time.tzinfo)

    if (say_date):
        if (date_time.date() == now.date()):
            retval += _phrase_noop("�������") + " "
        elif (date_time.date() == now.date() - datetime.timedelta(1)):
            retval += _phrase_noop("�����") + " "
        elif (date_time.date() == now.date() + datetime.timedelta(1)):
            retval += _phrase_noop("������") + " "
        else:
            retval += _sayNumber(date_time.day, True, GENDER_MASCULINE, case) + " "
            retval += MONTH[CASE_GENITIVE][date_time.month - 1] + " "
            retval += _sayNumber(date_time.year, True, GENDER_MASCULINE, CASE_GENITIVE) + " "
            retval += _phrase_noop("����") + " "

    if (say_time):
        retval += _phrase_noop("�") + " "
        retval += _sayNumber(date_time.hour, False, GENDER_MASCULINE, CASE_ACCUSATIVE) + " "
        if (verbose_time):
            retval += ncvt(_phrase_noop("���"),
                           _phrase_noop("�����"), # �������� �� ��������� �����
                           _phrase_noop("�����"), date_time.hour) + " "
        minute = date_time.minute
        if (minute < 10):
            retval += _phrase_noop("����") + " "
        retval += _sayNumber(minute, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        if (verbose_time):
            retval += ncvt(_phrase_noop("������"),
                           _phrase_noop("������"),
                           _phrase_noop("�����"), minute) + " "
        if (say_seconds):
            secs = date_time.second
            retval += _phrase_noop("�") + " "
            retval += _sayNumber(secs, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
            if (verbose_time):
                retval += ncvt(_phrase_noop("�������"),
                               _phrase_noop("�������"),
                               _phrase_noop("������"), secs) + " "
    return retval.rstrip()

def sayDuration(seconds, say_hours, say_minutes, flags):
    retval = unicode("")
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
        retval += _sayNumber(hours, False, GENDER_MASCULINE, CASE_NOMINATIVE) + " "
        retval += ncvt(_phrase_noop("���"),
                       _phrase_noop("�����"),
                       _phrase_noop("�����"), hours) + " "
    if (minutes > 0):
        if (hours > 0 and s == 0):
            retval += _phrase_noop("�") + " "
        retval += _sayNumber(minutes, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        retval += ncvt(_phrase_noop("������"),
                       _phrase_noop("������"),
                       _phrase_noop("�����"), minutes) + " "
    if (s > 0):
        if (hours > 0 or minutes > 0):
            retval += _phrase_noop("�") + " "
        retval += _sayNumber(s, False, GENDER_FEMININE, CASE_ACCUSATIVE) + " "
        retval += ncvt(_phrase_noop("�������"),
                       _phrase_noop("�������"),
                       _phrase_noop("������"), s) + " "
    return retval.rstrip()
