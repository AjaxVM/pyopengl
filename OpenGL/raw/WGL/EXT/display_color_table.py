'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_EXT_display_color_table'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_display_color_table')

@_f
@_p.types(_cs.GLboolean,_cs.GLushort)
def wglBindDisplayColorTableEXT(id):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLushort)
def wglCreateDisplayColorTableEXT(id):pass
@_f
@_p.types(_cs.VOID,_cs.GLushort)
def wglDestroyDisplayColorTableEXT(id):pass
@_f
@_p.types(_cs.GLboolean,arrays.GLushortArray,_cs.GLuint)
def wglLoadDisplayColorTableEXT(table,length):pass
