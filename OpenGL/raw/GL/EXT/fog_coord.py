'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_fog_coord'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_fog_coord')
GL_CURRENT_FOG_COORDINATE_EXT=_C('GL_CURRENT_FOG_COORDINATE_EXT',0x8453)
GL_FOG_COORDINATE_ARRAY_EXT=_C('GL_FOG_COORDINATE_ARRAY_EXT',0x8457)
GL_FOG_COORDINATE_ARRAY_POINTER_EXT=_C('GL_FOG_COORDINATE_ARRAY_POINTER_EXT',0x8456)
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT=_C('GL_FOG_COORDINATE_ARRAY_STRIDE_EXT',0x8455)
GL_FOG_COORDINATE_ARRAY_TYPE_EXT=_C('GL_FOG_COORDINATE_ARRAY_TYPE_EXT',0x8454)
GL_FOG_COORDINATE_EXT=_C('GL_FOG_COORDINATE_EXT',0x8451)
GL_FOG_COORDINATE_SOURCE_EXT=_C('GL_FOG_COORDINATE_SOURCE_EXT',0x8450)
GL_FRAGMENT_DEPTH_EXT=_C('GL_FRAGMENT_DEPTH_EXT',0x8452)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glFogCoordPointerEXT(type,stride,pointer):pass
# Calculate length of pointer from type:FogPointerTypeEXT
@_f
@_p.types(None,_cs.GLdouble)
def glFogCoorddEXT(coord):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glFogCoorddvEXT(coord):pass
@_f
@_p.types(None,_cs.GLfloat)
def glFogCoordfEXT(coord):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glFogCoordfvEXT(coord):pass
