'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_texture_gather'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_texture_gather')
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB=_C('GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB',0x8F9F)
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB=_C('GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB',0x8E5F)
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB=_C('GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB',0x8E5E)

