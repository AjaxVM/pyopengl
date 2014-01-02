'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_draw_buffers'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_draw_buffers')
GL_COLOR_ATTACHMENT0_EXT=_C('GL_COLOR_ATTACHMENT0_EXT',0x8CE0)
GL_COLOR_ATTACHMENT10_EXT=_C('GL_COLOR_ATTACHMENT10_EXT',0x8CEA)
GL_COLOR_ATTACHMENT11_EXT=_C('GL_COLOR_ATTACHMENT11_EXT',0x8CEB)
GL_COLOR_ATTACHMENT12_EXT=_C('GL_COLOR_ATTACHMENT12_EXT',0x8CEC)
GL_COLOR_ATTACHMENT13_EXT=_C('GL_COLOR_ATTACHMENT13_EXT',0x8CED)
GL_COLOR_ATTACHMENT14_EXT=_C('GL_COLOR_ATTACHMENT14_EXT',0x8CEE)
GL_COLOR_ATTACHMENT15_EXT=_C('GL_COLOR_ATTACHMENT15_EXT',0x8CEF)
GL_COLOR_ATTACHMENT1_EXT=_C('GL_COLOR_ATTACHMENT1_EXT',0x8CE1)
GL_COLOR_ATTACHMENT2_EXT=_C('GL_COLOR_ATTACHMENT2_EXT',0x8CE2)
GL_COLOR_ATTACHMENT3_EXT=_C('GL_COLOR_ATTACHMENT3_EXT',0x8CE3)
GL_COLOR_ATTACHMENT4_EXT=_C('GL_COLOR_ATTACHMENT4_EXT',0x8CE4)
GL_COLOR_ATTACHMENT5_EXT=_C('GL_COLOR_ATTACHMENT5_EXT',0x8CE5)
GL_COLOR_ATTACHMENT6_EXT=_C('GL_COLOR_ATTACHMENT6_EXT',0x8CE6)
GL_COLOR_ATTACHMENT7_EXT=_C('GL_COLOR_ATTACHMENT7_EXT',0x8CE7)
GL_COLOR_ATTACHMENT8_EXT=_C('GL_COLOR_ATTACHMENT8_EXT',0x8CE8)
GL_COLOR_ATTACHMENT9_EXT=_C('GL_COLOR_ATTACHMENT9_EXT',0x8CE9)
GL_DRAW_BUFFER0_EXT=_C('GL_DRAW_BUFFER0_EXT',0x8825)
GL_DRAW_BUFFER10_EXT=_C('GL_DRAW_BUFFER10_EXT',0x882F)
GL_DRAW_BUFFER11_EXT=_C('GL_DRAW_BUFFER11_EXT',0x8830)
GL_DRAW_BUFFER12_EXT=_C('GL_DRAW_BUFFER12_EXT',0x8831)
GL_DRAW_BUFFER13_EXT=_C('GL_DRAW_BUFFER13_EXT',0x8832)
GL_DRAW_BUFFER14_EXT=_C('GL_DRAW_BUFFER14_EXT',0x8833)
GL_DRAW_BUFFER15_EXT=_C('GL_DRAW_BUFFER15_EXT',0x8834)
GL_DRAW_BUFFER1_EXT=_C('GL_DRAW_BUFFER1_EXT',0x8826)
GL_DRAW_BUFFER2_EXT=_C('GL_DRAW_BUFFER2_EXT',0x8827)
GL_DRAW_BUFFER3_EXT=_C('GL_DRAW_BUFFER3_EXT',0x8828)
GL_DRAW_BUFFER4_EXT=_C('GL_DRAW_BUFFER4_EXT',0x8829)
GL_DRAW_BUFFER5_EXT=_C('GL_DRAW_BUFFER5_EXT',0x882A)
GL_DRAW_BUFFER6_EXT=_C('GL_DRAW_BUFFER6_EXT',0x882B)
GL_DRAW_BUFFER7_EXT=_C('GL_DRAW_BUFFER7_EXT',0x882C)
GL_DRAW_BUFFER8_EXT=_C('GL_DRAW_BUFFER8_EXT',0x882D)
GL_DRAW_BUFFER9_EXT=_C('GL_DRAW_BUFFER9_EXT',0x882E)
GL_MAX_COLOR_ATTACHMENTS_EXT=_C('GL_MAX_COLOR_ATTACHMENTS_EXT',0x8CDF)
GL_MAX_DRAW_BUFFERS_EXT=_C('GL_MAX_DRAW_BUFFERS_EXT',0x8824)
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDrawBuffersEXT(n,bufs):pass
