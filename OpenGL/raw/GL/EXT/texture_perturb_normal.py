'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_texture_perturb_normal'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_perturb_normal')
GL_PERTURB_EXT=_C('GL_PERTURB_EXT',0x85AE)
GL_TEXTURE_NORMAL_EXT=_C('GL_TEXTURE_NORMAL_EXT',0x85AF)
@_f
@_p.types(None,_cs.GLenum)
def glTextureNormalEXT(mode):pass
