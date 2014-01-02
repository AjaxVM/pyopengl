'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ATI_vertex_array_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_vertex_array_object')
GL_ARRAY_OBJECT_BUFFER_ATI=_C('GL_ARRAY_OBJECT_BUFFER_ATI',0x8766)
GL_ARRAY_OBJECT_OFFSET_ATI=_C('GL_ARRAY_OBJECT_OFFSET_ATI',0x8767)
GL_DISCARD_ATI=_C('GL_DISCARD_ATI',0x8763)
GL_DYNAMIC_ATI=_C('GL_DYNAMIC_ATI',0x8761)
GL_OBJECT_BUFFER_SIZE_ATI=_C('GL_OBJECT_BUFFER_SIZE_ATI',0x8764)
GL_OBJECT_BUFFER_USAGE_ATI=_C('GL_OBJECT_BUFFER_USAGE_ATI',0x8765)
GL_PRESERVE_ATI=_C('GL_PRESERVE_ATI',0x8762)
GL_STATIC_ATI=_C('GL_STATIC_ATI',0x8760)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLuint,_cs.GLuint)
def glArrayObjectATI(array,size,type,stride,buffer,offset):pass
@_f
@_p.types(None,_cs.GLuint)
def glFreeObjectBufferATI(buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetArrayObjectfvATI(array,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetArrayObjectivATI(array,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetObjectBufferfvATI(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetObjectBufferivATI(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVariantArrayObjectfvATI(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVariantArrayObjectivATI(id,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsObjectBufferATI(buffer):pass
@_f
@_p.types(_cs.GLuint,_cs.GLsizei,ctypes.c_void_p,_cs.GLenum)
def glNewObjectBufferATI(size,pointer,usage):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,ctypes.c_void_p,_cs.GLenum)
def glUpdateObjectBufferATI(buffer,offset,size,pointer,preserve):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLuint,_cs.GLuint)
def glVariantArrayObjectATI(id,type,stride,buffer,offset):pass
