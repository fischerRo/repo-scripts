# coding: utf-8
# Created on: 04.01.2018
# Author: Roman Miroshnychenko aka Roman V.M. (roman1972@gmail.com)
"""
Functions and classes to work with files and folders
"""

from __future__ import absolute_import
import sys as _sys
from xbmcvfs import *
from .utils import PY2 as _PY2, patch_module as _patch_module

if _PY2:
    _patch_module(_sys.modules[__name__])