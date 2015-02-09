#!/usr/bin/env python
from distutils.core import setup

setup(name='tormonitor',
      version='0.1',
      scripts=['tormonitor'],
      data_files=[('share/icons/hicolor/scalable/apps', ['tormonitor.svg']),
                  ('share/applications', ['tormonitor.desktop'])],
      requires=['stem','gi']
     )
