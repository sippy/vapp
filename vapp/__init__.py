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

from Agi import AgiHandler, AgiError, AgiKeyStroke
from BasePlugin import BasePlugin
from PluginHandler import PluginHandler, loadPlugins, pluginInstance
from Locale import Locale
from ConfigParser import ConfigParser, DEFAULTSECT
import sys
import os

logger = None

_translation_config = None

def default_pot_files():
    files = []
    cfg = _translation_config
    for section in cfg.sections():
        if (cfg.has_option(section, 'po_dir') and 
                cfg.has_option(section, 'text_domain')):
            files.append(os.path.join(cfg.get(section, 'po_dir'), 
                    cfg.get(section, 'text_domain') + ".pot"))
    return files

def default_prompt_dirs():
    dirs = []
    cfg = _translation_config
    for section in cfg.sections():
        if cfg.has_option(section, 'prompt_catalog_dir'):
            dirs.append(cfg.get(section, 'prompt_catalog_dir'))
    return dirs

def _init_translation_config():
    global _translation_config

    local_dir = sys.path[0]
    if local_dir == '':
        local_dir = '.'
    local_configs = [ local_dir + "/.vapp.conf" ]
    cwd = os.getcwd()
    if cwd != local_dir:
        local_configs.append(cwd + "/.vapp.conf")

    if sys.prefix == '/usr':
        sys_etc_dir = ''
    else:
        sys_etc_dir = sys.prefix

    defaults = {
        'text_domain'       : 'vapp',
        'po_dir'            : sys.prefix + '/share/vapp/po',
        'msg_catalog_dir'   : sys.prefix + '/share/locale',
        'prompt_catalog_dir': sys.prefix + '/share/vapp/prompts'
    }
    _translation_config = ConfigParser(defaults)
    _translation_config.read([sys_etc_dir + "/etc/vapp.conf"] + local_configs)

_init_translation_config()
