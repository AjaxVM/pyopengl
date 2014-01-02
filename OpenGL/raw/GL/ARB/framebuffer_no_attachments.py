'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_framebuffer_no_attachments'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_framebuffer_no_attachments')
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS=_C('GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS',0x9314)
GL_FRAMEBUFFER_DEFAULT_HEIGHT=_C('GL_FRAMEBUFFER_DEFAULT_HEIGHT',0x9311)
GL_FRAMEBUFFER_DEFAULT_LAYERS=_C('GL_FRAMEBUFFER_DEFAULT_LAYERS',0x9312)
GL_FRAMEBUFFER_DEFAULT_SAMPLES=_C('GL_FRAMEBUFFER_DEFAULT_SAMPLES',0x9313)
GL_FRAMEBUFFER_DEFAULT_WIDTH=_C('GL_FRAMEBUFFER_DEFAULT_WIDTH',0x9310)
GL_MAX_FRAMEBUFFER_HEIGHT=_C('GL_MAX_FRAMEBUFFER_HEIGHT',0x9316)
GL_MAX_FRAMEBUFFER_LAYERS=_C('GL_MAX_FRAMEBUFFER_LAYERS',0x9317)
GL_MAX_FRAMEBUFFER_SAMPLES=_C('GL_MAX_FRAMEBUFFER_SAMPLES',0x9318)
GL_MAX_FRAMEBUFFER_WIDTH=_C('GL_MAX_FRAMEBUFFER_WIDTH',0x9315)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glFramebufferParameteri(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferParameteriv(target,pname,params):pass
