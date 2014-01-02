'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SUN_global_alpha'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SUN_global_alpha')
GL_GLOBAL_ALPHA_FACTOR_SUN=_C('GL_GLOBAL_ALPHA_FACTOR_SUN',0x81DA)
GL_GLOBAL_ALPHA_SUN=_C('GL_GLOBAL_ALPHA_SUN',0x81D9)
@_f
@_p.types(None,_cs.GLbyte)
def glGlobalAlphaFactorbSUN(factor):pass
@_f
@_p.types(None,_cs.GLdouble)
def glGlobalAlphaFactordSUN(factor):pass
@_f
@_p.types(None,_cs.GLfloat)
def glGlobalAlphaFactorfSUN(factor):pass
@_f
@_p.types(None,_cs.GLint)
def glGlobalAlphaFactoriSUN(factor):pass
@_f
@_p.types(None,_cs.GLshort)
def glGlobalAlphaFactorsSUN(factor):pass
@_f
@_p.types(None,_cs.GLubyte)
def glGlobalAlphaFactorubSUN(factor):pass
@_f
@_p.types(None,_cs.GLuint)
def glGlobalAlphaFactoruiSUN(factor):pass
@_f
@_p.types(None,_cs.GLushort)
def glGlobalAlphaFactorusSUN(factor):pass
