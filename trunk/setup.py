#!/usr/bin/env python

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

import os, sys
from distutils.command.install import install as _install
from distutils.core import setup, Extension
import glob

VERSION = "0.25"

LICENSE = """
        The vapp library is distributed under version 2 of GNU Public 
        License (GPL). For a license to use the vapp software under 
        conditions other than those described here, or to purchase 
        support for this software, please contact Sippy Software, Inc.
"""

DESCRIPTION = """
IVR application framework designed to use the Asterisk AGI or 
OpenPBX OGI protocol.
"""

class install(_install):
    def run(self):
        print "compiling gettext files"
        os.chdir("po")
        for fname in glob.glob("*.po"):
            os.spawnl(os.P_WAIT, "./compilepo.sh", "./compilepo.sh", fname[:-3], self.root)
        os.chdir(os.pardir)
        _install.run(self)

tmp = os.walk('prompts')
prompts = []
for root, dirs, files in tmp:
    if '.svn' in dirs:
        dirs.remove('.svn')
    if len(files) == 0:
        continue
    prompt_files = []
    for f in files:
        prompt_files.append(os.path.join(root, f))
    prompts.append((os.path.join('share/vapp', root), prompt_files))

setup(name = "vapp",
      version = VERSION,
      description = "Python implementation of Asterisk AGI and OpenPBX OGI interface",
      author = "Sippy Software, Inc.",
      author_email = "support@sippysoft.com",
      license = LICENSE,
      url = "http://www.sippysoft.com",
      long_description = DESCRIPTION,
      packages = [ 'vapp', 'vapp.TextSynth', 'vapp.SpeechSynth',
                   'vapp.voicemail' ],
      scripts = [ 'scripts/vapp_prompt_utils.py' ],
      data_files = [ ('share/vapp/po/', [ 'po/vapp.pot' ]) ] + prompts,
      platforms = "Python 2.4 and later",
      cmdclass = { 'install' : install }
      )
