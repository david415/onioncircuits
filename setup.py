#!/usr/bin/env python3
#
# Onion Circuits - a GTK applicaton to display Tor circuits and streams
# Copyright (C) 2016  Tails developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup, Command
from DistUtilsExtra.command import *

setup(name='onioncircuits',
      version='0.2',
      description='a GTK applicaton to display Tor circuits and streams',
      author='Tails developers',
      author_email='tails@boum.org',
      license='GNU GPL v3',
      scripts=['onioncircuits'],
      data_files=[('share/icons/hicolor/scalable/apps', ['onioncircuits.svg']),
                  ('share/applications', ['onioncircuits.desktop'])],
      requires=['stem', 'gi'],
      cmdclass = { "build" : build_extra.build_extra,
                   "build_i18n" :  build_i18n.build_i18n,
                   "build_help" :  build_help.build_help,
                   "build_icons" :  build_icons.build_icons,
                   "clean": clean_i18n.clean_i18n,
                 }
     )
