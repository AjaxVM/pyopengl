'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_MESA_copy_sub_buffer'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_MESA_copy_sub_buffer')

@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.c_int,_cs.c_int,_cs.c_int,_cs.c_int)
def glXCopySubBufferMESA(dpy,drawable,x,y,width,height):pass
