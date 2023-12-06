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

import gettext
import vapp

__all__ = [ "Locale" ]

def gettext_translation_compat(*args, **kwargs):
    try:
        return gettext.translation(*args, **kwargs)
    except TypeError:
        # codeset parameter is deprecated in python 3.11
        del kwargs['codeset']
        return gettext.translation(*args, **kwargs)

class Locale:

    def __init__(self, localename):
        self.__name = localename
        cfg = vapp._translation_config
        def_domain = cfg.get('default_config', 'text_domain')
        def_catalog = cfg.get('default_config', 'msg_catalog_dir')
        self.__prompt_path = cfg.get('default_config', 'prompt_catalog_dir')
        try:
            self.__translator = gettext_translation_compat(def_domain, def_catalog, [ localename ], codeset = 'utf-8')
            for section in cfg.sections():
                if (cfg.has_option(section, 'msg_catalog_dir') and cfg.has_option(section, 'text_domain')):
                    directory =  cfg.get(section, 'msg_catalog_dir')
                    domain =  cfg.get(section, 'text_domain')
                    try:
                        tr = gettext_translation_compat(domain, directory, [ self.__name ], codeset = 'utf-8')
                        self.__translator.add_fallback(tr)
                    except IOError:
                        pass
            self.__gettext = self.__translator.lgettext
            self.__ngettext = self.__translator.lngettext
        except IOError:
            self.__translator = None
            self.__name = "en"
            self.__gettext = gettext.gettext
            self.__ngettext = gettext.ngettext

    def gettext(self, s):
        ret = self.__gettext(s)
        if isinstance(ret, bytes):
            ret = ret.decode('utf-8')
        return ret

    def ngettext(self, singular, plural, num):
        ret = self.__ngettext(singular, plural, num)
        if isinstance(ret, bytes):
            ret = ret.decode('utf-8')
        return ret

    def name(self):
        return self.__name

    def beepFile(self):
        return self.__prompt_path + '/beep'
