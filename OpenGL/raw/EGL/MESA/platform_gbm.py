'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_MESA_platform_gbm'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_MESA_platform_gbm')
EGL_PLATFORM_GBM_MESA=_C('EGL_PLATFORM_GBM_MESA',0x31D7)

