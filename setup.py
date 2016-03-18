#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['or_circularsmoother'],
    package_dir={'': 'src'}
)

setup(**d)
