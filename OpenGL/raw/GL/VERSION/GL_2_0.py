'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_2_0'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_2_0')
GL_ACTIVE_ATTRIBUTES=_C('GL_ACTIVE_ATTRIBUTES',0x8B89)
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH=_C('GL_ACTIVE_ATTRIBUTE_MAX_LENGTH',0x8B8A)
GL_ACTIVE_UNIFORMS=_C('GL_ACTIVE_UNIFORMS',0x8B86)
GL_ACTIVE_UNIFORM_MAX_LENGTH=_C('GL_ACTIVE_UNIFORM_MAX_LENGTH',0x8B87)
GL_ATTACHED_SHADERS=_C('GL_ATTACHED_SHADERS',0x8B85)
GL_BLEND_EQUATION_ALPHA=_C('GL_BLEND_EQUATION_ALPHA',0x883D)
GL_BLEND_EQUATION_RGB=_C('GL_BLEND_EQUATION_RGB',0x8009)
GL_BOOL=_C('GL_BOOL',0x8B56)
GL_BOOL_VEC2=_C('GL_BOOL_VEC2',0x8B57)
GL_BOOL_VEC3=_C('GL_BOOL_VEC3',0x8B58)
GL_BOOL_VEC4=_C('GL_BOOL_VEC4',0x8B59)
GL_COMPILE_STATUS=_C('GL_COMPILE_STATUS',0x8B81)
GL_COORD_REPLACE=_C('GL_COORD_REPLACE',0x8862)
GL_CURRENT_PROGRAM=_C('GL_CURRENT_PROGRAM',0x8B8D)
GL_CURRENT_VERTEX_ATTRIB=_C('GL_CURRENT_VERTEX_ATTRIB',0x8626)
GL_DELETE_STATUS=_C('GL_DELETE_STATUS',0x8B80)
GL_DRAW_BUFFER0=_C('GL_DRAW_BUFFER0',0x8825)
GL_DRAW_BUFFER1=_C('GL_DRAW_BUFFER1',0x8826)
GL_DRAW_BUFFER10=_C('GL_DRAW_BUFFER10',0x882F)
GL_DRAW_BUFFER11=_C('GL_DRAW_BUFFER11',0x8830)
GL_DRAW_BUFFER12=_C('GL_DRAW_BUFFER12',0x8831)
GL_DRAW_BUFFER13=_C('GL_DRAW_BUFFER13',0x8832)
GL_DRAW_BUFFER14=_C('GL_DRAW_BUFFER14',0x8833)
GL_DRAW_BUFFER15=_C('GL_DRAW_BUFFER15',0x8834)
GL_DRAW_BUFFER2=_C('GL_DRAW_BUFFER2',0x8827)
GL_DRAW_BUFFER3=_C('GL_DRAW_BUFFER3',0x8828)
GL_DRAW_BUFFER4=_C('GL_DRAW_BUFFER4',0x8829)
GL_DRAW_BUFFER5=_C('GL_DRAW_BUFFER5',0x882A)
GL_DRAW_BUFFER6=_C('GL_DRAW_BUFFER6',0x882B)
GL_DRAW_BUFFER7=_C('GL_DRAW_BUFFER7',0x882C)
GL_DRAW_BUFFER8=_C('GL_DRAW_BUFFER8',0x882D)
GL_DRAW_BUFFER9=_C('GL_DRAW_BUFFER9',0x882E)
GL_FLOAT_MAT2=_C('GL_FLOAT_MAT2',0x8B5A)
GL_FLOAT_MAT3=_C('GL_FLOAT_MAT3',0x8B5B)
GL_FLOAT_MAT4=_C('GL_FLOAT_MAT4',0x8B5C)
GL_FLOAT_VEC2=_C('GL_FLOAT_VEC2',0x8B50)
GL_FLOAT_VEC3=_C('GL_FLOAT_VEC3',0x8B51)
GL_FLOAT_VEC4=_C('GL_FLOAT_VEC4',0x8B52)
GL_FRAGMENT_SHADER=_C('GL_FRAGMENT_SHADER',0x8B30)
GL_FRAGMENT_SHADER_DERIVATIVE_HINT=_C('GL_FRAGMENT_SHADER_DERIVATIVE_HINT',0x8B8B)
GL_INFO_LOG_LENGTH=_C('GL_INFO_LOG_LENGTH',0x8B84)
GL_INT_VEC2=_C('GL_INT_VEC2',0x8B53)
GL_INT_VEC3=_C('GL_INT_VEC3',0x8B54)
GL_INT_VEC4=_C('GL_INT_VEC4',0x8B55)
GL_LINK_STATUS=_C('GL_LINK_STATUS',0x8B82)
GL_LOWER_LEFT=_C('GL_LOWER_LEFT',0x8CA1)
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS=_C('GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS',0x8B4D)
GL_MAX_DRAW_BUFFERS=_C('GL_MAX_DRAW_BUFFERS',0x8824)
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS=_C('GL_MAX_FRAGMENT_UNIFORM_COMPONENTS',0x8B49)
GL_MAX_TEXTURE_COORDS=_C('GL_MAX_TEXTURE_COORDS',0x8871)
GL_MAX_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TEXTURE_IMAGE_UNITS',0x8872)
GL_MAX_VARYING_FLOATS=_C('GL_MAX_VARYING_FLOATS',0x8B4B)
GL_MAX_VERTEX_ATTRIBS=_C('GL_MAX_VERTEX_ATTRIBS',0x8869)
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS=_C('GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS',0x8B4C)
GL_MAX_VERTEX_UNIFORM_COMPONENTS=_C('GL_MAX_VERTEX_UNIFORM_COMPONENTS',0x8B4A)
GL_POINT_SPRITE=_C('GL_POINT_SPRITE',0x8861)
GL_POINT_SPRITE_COORD_ORIGIN=_C('GL_POINT_SPRITE_COORD_ORIGIN',0x8CA0)
GL_SAMPLER_1D=_C('GL_SAMPLER_1D',0x8B5D)
GL_SAMPLER_1D_SHADOW=_C('GL_SAMPLER_1D_SHADOW',0x8B61)
GL_SAMPLER_2D=_C('GL_SAMPLER_2D',0x8B5E)
GL_SAMPLER_2D_SHADOW=_C('GL_SAMPLER_2D_SHADOW',0x8B62)
GL_SAMPLER_3D=_C('GL_SAMPLER_3D',0x8B5F)
GL_SAMPLER_CUBE=_C('GL_SAMPLER_CUBE',0x8B60)
GL_SHADER_SOURCE_LENGTH=_C('GL_SHADER_SOURCE_LENGTH',0x8B88)
GL_SHADER_TYPE=_C('GL_SHADER_TYPE',0x8B4F)
GL_SHADING_LANGUAGE_VERSION=_C('GL_SHADING_LANGUAGE_VERSION',0x8B8C)
GL_STENCIL_BACK_FAIL=_C('GL_STENCIL_BACK_FAIL',0x8801)
GL_STENCIL_BACK_FUNC=_C('GL_STENCIL_BACK_FUNC',0x8800)
GL_STENCIL_BACK_PASS_DEPTH_FAIL=_C('GL_STENCIL_BACK_PASS_DEPTH_FAIL',0x8802)
GL_STENCIL_BACK_PASS_DEPTH_PASS=_C('GL_STENCIL_BACK_PASS_DEPTH_PASS',0x8803)
GL_STENCIL_BACK_REF=_C('GL_STENCIL_BACK_REF',0x8CA3)
GL_STENCIL_BACK_VALUE_MASK=_C('GL_STENCIL_BACK_VALUE_MASK',0x8CA4)
GL_STENCIL_BACK_WRITEMASK=_C('GL_STENCIL_BACK_WRITEMASK',0x8CA5)
GL_UPPER_LEFT=_C('GL_UPPER_LEFT',0x8CA2)
GL_VALIDATE_STATUS=_C('GL_VALIDATE_STATUS',0x8B83)
GL_VERTEX_ATTRIB_ARRAY_ENABLED=_C('GL_VERTEX_ATTRIB_ARRAY_ENABLED',0x8622)
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED=_C('GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',0x886A)
GL_VERTEX_ATTRIB_ARRAY_POINTER=_C('GL_VERTEX_ATTRIB_ARRAY_POINTER',0x8645)
GL_VERTEX_ATTRIB_ARRAY_SIZE=_C('GL_VERTEX_ATTRIB_ARRAY_SIZE',0x8623)
GL_VERTEX_ATTRIB_ARRAY_STRIDE=_C('GL_VERTEX_ATTRIB_ARRAY_STRIDE',0x8624)
GL_VERTEX_ATTRIB_ARRAY_TYPE=_C('GL_VERTEX_ATTRIB_ARRAY_TYPE',0x8625)
GL_VERTEX_PROGRAM_POINT_SIZE=_C('GL_VERTEX_PROGRAM_POINT_SIZE',0x8642)
GL_VERTEX_PROGRAM_TWO_SIDE=_C('GL_VERTEX_PROGRAM_TWO_SIDE',0x8643)
GL_VERTEX_SHADER=_C('GL_VERTEX_SHADER',0x8B31)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glAttachShader(program,shader):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glBindAttribLocation(program,index,name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparate(modeRGB,modeAlpha):pass
@_f
@_p.types(None,_cs.GLuint)
def glCompileShader(shader):pass
@_f
@_p.types(_cs.GLuint,)
def glCreateProgram():pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum)
def glCreateShader(type):pass
@_f
@_p.types(None,_cs.GLuint)
def glDeleteProgram(program):pass
@_f
@_p.types(None,_cs.GLuint)
def glDeleteShader(shader):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glDetachShader(program,shader):pass
@_f
@_p.types(None,_cs.GLuint)
def glDisableVertexAttribArray(index):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDrawBuffers(n,bufs):pass
@_f
@_p.types(None,_cs.GLuint)
def glEnableVertexAttribArray(index):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetActiveAttrib(program,index,bufSize,length,size,type,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetActiveUniform(program,index,bufSize,length,size,type,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLuintArray)
def glGetAttachedShaders(program,maxCount,count,shaders):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetAttribLocation(program,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetProgramInfoLog(program,bufSize,length,infoLog):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetProgramiv(program,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetShaderInfoLog(shader,bufSize,length,infoLog):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetShaderSource(shader,bufSize,length,source):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetShaderiv(shader,pname,params):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetUniformLocation(program,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLfloatArray)
def glGetUniformfv(program,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLintArray)
def glGetUniformiv(program,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLvoidpArray)
def glGetVertexAttribPointerv(index,pname,pointer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLdoubleArray)
def glGetVertexAttribdv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVertexAttribfv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribiv(index,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsProgram(program):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsShader(shader):pass
@_f
@_p.types(None,_cs.GLuint)
def glLinkProgram(program):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),arrays.GLintArray)
def glShaderSource(shader,count,string,length):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFuncSeparate(face,func,ref,mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glStencilMaskSeparate(face,mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOpSeparate(face,sfail,dpfail,dppass):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat)
def glUniform1f(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform1fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glUniform1i(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform1iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat)
def glUniform2f(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform2fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform2i(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform2iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glUniform3f(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform3fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform3i(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform3iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glUniform4f(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform4fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform4i(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform4iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix2fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix3fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix4fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint)
def glUseProgram(program):pass
@_f
@_p.types(None,_cs.GLuint)
def glValidateProgram(program):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble)
def glVertexAttrib1d(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttrib1dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat)
def glVertexAttrib1f(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib1fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLshort)
def glVertexAttrib1s(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttrib1sv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble)
def glVertexAttrib2d(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttrib2dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib2f(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib2fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLshort,_cs.GLshort)
def glVertexAttrib2s(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttrib2sv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttrib3d(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttrib3dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib3f(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib3fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertexAttrib3s(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttrib3sv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVertexAttrib4Nbv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttrib4Niv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttrib4Nsv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte)
def glVertexAttrib4Nub(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVertexAttrib4Nubv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttrib4Nuiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib4Nusv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVertexAttrib4bv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttrib4d(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttrib4dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib4f(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib4fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttrib4iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertexAttrib4s(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttrib4sv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVertexAttrib4ubv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttrib4uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttrib4usv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribPointer(index,size,type,normalized,stride,pointer):pass
# Calculate length of pointer from type:VertexAttribPointerType
