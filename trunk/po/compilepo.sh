#!/bin/sh
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


if [ x"$1" = x ]
then
    echo "usage: `basename $0` <locale name>"
    exit
fi
LOCALE=$1
OUTPUT_DIR="/usr/local/share/locale/${LOCALE}/LC_MESSAGES"
DOMAIN=vapp

POFILE="${LOCALE}.po"

if [ ! -d $OUTPUT_DIR ]
then
    if [ ! -f "$POFILE" ]; then
	echo "Locale dir doesn't exist: $OUTPUT_DIR"
	exit
    else
	mkdir -p $OUTPUT_DIR
    fi
fi

if [ -f "$POFILE" ]
then
    msgfmt -o "${OUTPUT_DIR}/${DOMAIN}.mo" -c "${POFILE}"
else
    echo "Cannot find the ${POFILE} file!"
fi
