# -*- coding: iso-8859-1 -*-
"""Raw (C-style) API for OpenGL.GLU

Automatically generated by the generateraw script, do not edit!
"""
from OpenGL.raw.GLU.constants import *

from ctypes import *
from OpenGL import platform, arrays
from OpenGL.constant import Constant
from OpenGL.raw.GL import _types as GL_types
GLvoid = GL_types.GLvoid

FUNCTION_TYPE = platform.PLATFORM.functionTypeFor( platform.GLU )
from OpenGL.raw.GL._types import (
    GLint,
    GLenum,
    GLsizei,
    GLboolean,
    GLubyte,
    GLdouble,
    GLfloat,
)


class GLUnurbs(Structure):
    pass
GLUnurbs._fields_ = [
    # /usr/include/GL/glu.h 257
]
GLUnurbsObj = GLUnurbs
class GLUquadric(Structure):
    pass
GLUquadric._fields_ = [
    # /usr/include/GL/glu.h 258
]
GLUquadricObj = GLUquadric
class GLUtesselator(Structure):
    pass
GLUtesselator._fields_ = [
    # /usr/include/GL/glu.h 259
]
GLUtesselatorObj = GLUtesselator
GLUtriangulatorObj = GLUtesselator


# /usr/include/GL/glu.h 276
gluBeginCurve = platform.createBaseFunction( 
    'gluBeginCurve', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluBeginCurve( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 277
gluBeginPolygon = platform.createBaseFunction( 
    'gluBeginPolygon', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluBeginPolygon( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 278
gluBeginSurface = platform.createBaseFunction( 
    'gluBeginSurface', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluBeginSurface( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 279
gluBeginTrim = platform.createBaseFunction( 
    'gluBeginTrim', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluBeginTrim( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 280
gluBuild1DMipmapLevels = platform.createBaseFunction( 
    'gluBuild1DMipmapLevels', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLenum,GLenum,GLint,GLint,GLint,c_void_p],
    doc='gluBuild1DMipmapLevels( GLenum(target), GLint(internalFormat), GLsizei(width), GLenum(format), GLenum(type), GLint(level), GLint(base), GLint(max), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'format', 'type', 'level', 'base', 'max', 'data'),
)


# /usr/include/GL/glu.h 281
gluBuild1DMipmaps = platform.createBaseFunction( 
    'gluBuild1DMipmaps', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLenum,GLenum,c_void_p],
    doc='gluBuild1DMipmaps( GLenum(target), GLint(internalFormat), GLsizei(width), GLenum(format), GLenum(type), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'format', 'type', 'data'),
)


# /usr/include/GL/glu.h 282
gluBuild2DMipmapLevels = platform.createBaseFunction( 
    'gluBuild2DMipmapLevels', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLsizei,GLenum,GLenum,GLint,GLint,GLint,c_void_p],
    doc='gluBuild2DMipmapLevels( GLenum(target), GLint(internalFormat), GLsizei(width), GLsizei(height), GLenum(format), GLenum(type), GLint(level), GLint(base), GLint(max), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'height', 'format', 'type', 'level', 'base', 'max', 'data'),
)


# /usr/include/GL/glu.h 283
gluBuild2DMipmaps = platform.createBaseFunction( 
    'gluBuild2DMipmaps', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLsizei,GLenum,GLenum,c_void_p],
    doc='gluBuild2DMipmaps( GLenum(target), GLint(internalFormat), GLsizei(width), GLsizei(height), GLenum(format), GLenum(type), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'height', 'format', 'type', 'data'),
)


# /usr/include/GL/glu.h 284
gluBuild3DMipmapLevels = platform.createBaseFunction( 
    'gluBuild3DMipmapLevels', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLsizei,GLsizei,GLenum,GLenum,GLint,GLint,GLint,c_void_p],
    doc='gluBuild3DMipmapLevels( GLenum(target), GLint(internalFormat), GLsizei(width), GLsizei(height), GLsizei(depth), GLenum(format), GLenum(type), GLint(level), GLint(base), GLint(max), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'height', 'depth', 'format', 'type', 'level', 'base', 'max', 'data'),
)


# /usr/include/GL/glu.h 285
gluBuild3DMipmaps = platform.createBaseFunction( 
    'gluBuild3DMipmaps', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLint,GLsizei,GLsizei,GLsizei,GLenum,GLenum,c_void_p],
    doc='gluBuild3DMipmaps( GLenum(target), GLint(internalFormat), GLsizei(width), GLsizei(height), GLsizei(depth), GLenum(format), GLenum(type), c_void_p(data) ) -> GLint', 
    argNames=('target', 'internalFormat', 'width', 'height', 'depth', 'format', 'type', 'data'),
)


# /usr/include/GL/glu.h 286
gluCheckExtension = platform.createBaseFunction( 
    'gluCheckExtension', dll=platform.GLU, resultType=GLboolean, 
    argTypes=[arrays.GLubyteArray,arrays.GLubyteArray],
    doc='gluCheckExtension( arrays.GLubyteArray(extName), arrays.GLubyteArray(extString) ) -> GLboolean', 
    argNames=('extName', 'extString'),
)


# /usr/include/GL/glu.h 287
gluCylinder = platform.createBaseFunction( 
    'gluCylinder', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLdouble,GLdouble,GLdouble,GLint,GLint],
    doc='gluCylinder( POINTER(GLUquadric)(quad), GLdouble(base), GLdouble(top), GLdouble(height), GLint(slices), GLint(stacks) ) -> None', 
    argNames=('quad', 'base', 'top', 'height', 'slices', 'stacks'),
)


# /usr/include/GL/glu.h 288
gluDeleteNurbsRenderer = platform.createBaseFunction( 
    'gluDeleteNurbsRenderer', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluDeleteNurbsRenderer( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 289
gluDeleteQuadric = platform.createBaseFunction( 
    'gluDeleteQuadric', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric)],
    doc='gluDeleteQuadric( POINTER(GLUquadric)(quad) ) -> None', 
    argNames=('quad',),
)


# /usr/include/GL/glu.h 290
gluDeleteTess = platform.createBaseFunction( 
    'gluDeleteTess', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluDeleteTess( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 291
gluDisk = platform.createBaseFunction( 
    'gluDisk', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLdouble,GLdouble,GLint,GLint],
    doc='gluDisk( POINTER(GLUquadric)(quad), GLdouble(inner), GLdouble(outer), GLint(slices), GLint(loops) ) -> None', 
    argNames=('quad', 'inner', 'outer', 'slices', 'loops'),
)


# /usr/include/GL/glu.h 292
gluEndCurve = platform.createBaseFunction( 
    'gluEndCurve', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluEndCurve( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 293
gluEndPolygon = platform.createBaseFunction( 
    'gluEndPolygon', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluEndPolygon( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 294
gluEndSurface = platform.createBaseFunction( 
    'gluEndSurface', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluEndSurface( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 295
gluEndTrim = platform.createBaseFunction( 
    'gluEndTrim', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs)],
    doc='gluEndTrim( POINTER(GLUnurbs)(nurb) ) -> None', 
    argNames=('nurb',),
)


# /usr/include/GL/glu.h 296
gluErrorString = platform.createBaseFunction( 
    'gluErrorString', dll=platform.GLU, resultType=POINTER(GLubyte), 
    argTypes=[GLenum],
    doc='gluErrorString( GLenum(error) ) -> POINTER(GLubyte)', 
    argNames=('error',),
)


# /usr/include/GL/glu.h 297
gluGetNurbsProperty = platform.createBaseFunction( 
    'gluGetNurbsProperty', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLenum,arrays.GLfloatArray],
    doc='gluGetNurbsProperty( POINTER(GLUnurbs)(nurb), GLenum(property), arrays.GLfloatArray(data) ) -> None', 
    argNames=('nurb', 'property', 'data'),
)


# /usr/include/GL/glu.h 298
gluGetString = platform.createBaseFunction( 
    'gluGetString', dll=platform.GLU, resultType=POINTER(GLubyte), 
    argTypes=[GLenum],
    doc='gluGetString( GLenum(name) ) -> POINTER(GLubyte)', 
    argNames=('name',),
)


# /usr/include/GL/glu.h 299
gluGetTessProperty = platform.createBaseFunction( 
    'gluGetTessProperty', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),GLenum,arrays.GLdoubleArray],
    doc='gluGetTessProperty( POINTER(GLUtesselator)(tess), GLenum(which), arrays.GLdoubleArray(data) ) -> None', 
    argNames=('tess', 'which', 'data'),
)


# /usr/include/GL/glu.h 300
gluLoadSamplingMatrices = platform.createBaseFunction( 
    'gluLoadSamplingMatrices', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),arrays.GLfloatArray,arrays.GLfloatArray,arrays.GLintArray],
    doc='gluLoadSamplingMatrices( POINTER(GLUnurbs)(nurb), arrays.GLfloatArray(model), arrays.GLfloatArray(perspective), arrays.GLintArray(view) ) -> None', 
    argNames=('nurb', 'model', 'perspective', 'view'),
)


# /usr/include/GL/glu.h 301
gluLookAt = platform.createBaseFunction( 
    'gluLookAt', dll=platform.GLU, resultType=None, 
    argTypes=[GLdouble,GLdouble,GLdouble,GLdouble,GLdouble,GLdouble,GLdouble,GLdouble,GLdouble],
    doc='gluLookAt( GLdouble(eyeX), GLdouble(eyeY), GLdouble(eyeZ), GLdouble(centerX), GLdouble(centerY), GLdouble(centerZ), GLdouble(upX), GLdouble(upY), GLdouble(upZ) ) -> None', 
    argNames=('eyeX', 'eyeY', 'eyeZ', 'centerX', 'centerY', 'centerZ', 'upX', 'upY', 'upZ'),
)


# /usr/include/GL/glu.h 302
gluNewNurbsRenderer = platform.createBaseFunction( 
    'gluNewNurbsRenderer', dll=platform.GLU, resultType=POINTER(GLUnurbs), 
    argTypes=[],
    doc='gluNewNurbsRenderer(  ) -> POINTER(GLUnurbs)', 
    argNames=(),
)


# /usr/include/GL/glu.h 303
gluNewQuadric = platform.createBaseFunction( 
    'gluNewQuadric', dll=platform.GLU, resultType=POINTER(GLUquadric), 
    argTypes=[],
    doc='gluNewQuadric(  ) -> POINTER(GLUquadric)', 
    argNames=(),
)


# /usr/include/GL/glu.h 304
gluNewTess = platform.createBaseFunction( 
    'gluNewTess', dll=platform.GLU, resultType=POINTER(GLUtesselator), 
    argTypes=[],
    doc='gluNewTess(  ) -> POINTER(GLUtesselator)', 
    argNames=(),
)


# /usr/include/GL/glu.h 305
gluNextContour = platform.createBaseFunction( 
    'gluNextContour', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),GLenum],
    doc='gluNextContour( POINTER(GLUtesselator)(tess), GLenum(type) ) -> None', 
    argNames=('tess', 'type'),
)


_GLUfuncptr = FUNCTION_TYPE(None)
# /usr/include/GL/glu.h 306
gluNurbsCallback = platform.createBaseFunction( 
    'gluNurbsCallback', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLenum,_GLUfuncptr],
    doc='gluNurbsCallback( POINTER(GLUnurbs)(nurb), GLenum(which), _GLUfuncptr(CallBackFunc) ) -> None', 
    argNames=('nurb', 'which', 'CallBackFunc'),
)

GLvoid = None
# /usr/include/GL/glu.h 307
gluNurbsCallbackData = platform.createBaseFunction( 
    'gluNurbsCallbackData', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),POINTER(GLvoid)],
    doc='gluNurbsCallbackData( POINTER(GLUnurbs)(nurb), POINTER(GLvoid)(userData) ) -> None', 
    argNames=('nurb', 'userData'),
)


# /usr/include/GL/glu.h 308
gluNurbsCallbackDataEXT = platform.createBaseFunction( 
    'gluNurbsCallbackDataEXT', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),POINTER(GLvoid)],
    doc='gluNurbsCallbackDataEXT( POINTER(GLUnurbs)(nurb), POINTER(GLvoid)(userData) ) -> None', 
    argNames=('nurb', 'userData'),
)


# /usr/include/GL/glu.h 309
gluNurbsCurve = platform.createBaseFunction( 
    'gluNurbsCurve', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLint,arrays.GLfloatArray,GLint,arrays.GLfloatArray,GLint,GLenum],
    doc='gluNurbsCurve( POINTER(GLUnurbs)(nurb), GLint(knotCount), arrays.GLfloatArray(knots), GLint(stride), arrays.GLfloatArray(control), GLint(order), GLenum(type) ) -> None', 
    argNames=('nurb', 'knotCount', 'knots', 'stride', 'control', 'order', 'type'),
)


# /usr/include/GL/glu.h 310
gluNurbsProperty = platform.createBaseFunction( 
    'gluNurbsProperty', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLenum,GLfloat],
    doc='gluNurbsProperty( POINTER(GLUnurbs)(nurb), GLenum(property), GLfloat(value) ) -> None', 
    argNames=('nurb', 'property', 'value'),
)


# /usr/include/GL/glu.h 311
gluNurbsSurface = platform.createBaseFunction( 
    'gluNurbsSurface', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLint,arrays.GLfloatArray,GLint,arrays.GLfloatArray,GLint,GLint,arrays.GLfloatArray,GLint,GLint,GLenum],
    doc='gluNurbsSurface( POINTER(GLUnurbs)(nurb), GLint(sKnotCount), arrays.GLfloatArray(sKnots), GLint(tKnotCount), arrays.GLfloatArray(tKnots), GLint(sStride), GLint(tStride), arrays.GLfloatArray(control), GLint(sOrder), GLint(tOrder), GLenum(type) ) -> None', 
    argNames=('nurb', 'sKnotCount', 'sKnots', 'tKnotCount', 'tKnots', 'sStride', 'tStride', 'control', 'sOrder', 'tOrder', 'type'),
)


# /usr/include/GL/glu.h 312
gluOrtho2D = platform.createBaseFunction( 
    'gluOrtho2D', dll=platform.GLU, resultType=None, 
    argTypes=[GLdouble,GLdouble,GLdouble,GLdouble],
    doc='gluOrtho2D( GLdouble(left), GLdouble(right), GLdouble(bottom), GLdouble(top) ) -> None', 
    argNames=('left', 'right', 'bottom', 'top'),
)


# /usr/include/GL/glu.h 313
gluPartialDisk = platform.createBaseFunction( 
    'gluPartialDisk', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLdouble,GLdouble,GLint,GLint,GLdouble,GLdouble],
    doc='gluPartialDisk( POINTER(GLUquadric)(quad), GLdouble(inner), GLdouble(outer), GLint(slices), GLint(loops), GLdouble(start), GLdouble(sweep) ) -> None', 
    argNames=('quad', 'inner', 'outer', 'slices', 'loops', 'start', 'sweep'),
)


# /usr/include/GL/glu.h 314
gluPerspective = platform.createBaseFunction( 
    'gluPerspective', dll=platform.GLU, resultType=None, 
    argTypes=[GLdouble,GLdouble,GLdouble,GLdouble],
    doc='gluPerspective( GLdouble(fovy), GLdouble(aspect), GLdouble(zNear), GLdouble(zFar) ) -> None', 
    argNames=('fovy', 'aspect', 'zNear', 'zFar'),
)


# /usr/include/GL/glu.h 315
gluPickMatrix = platform.createBaseFunction( 
    'gluPickMatrix', dll=platform.GLU, resultType=None, 
    argTypes=[GLdouble,GLdouble,GLdouble,GLdouble,arrays.GLintArray],
    doc='gluPickMatrix( GLdouble(x), GLdouble(y), GLdouble(delX), GLdouble(delY), arrays.GLintArray(viewport) ) -> None', 
    argNames=('x', 'y', 'delX', 'delY', 'viewport'),
)


# /usr/include/GL/glu.h 316
gluProject = platform.createBaseFunction( 
    'gluProject', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLdouble,GLdouble,GLdouble,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLintArray,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='gluProject( GLdouble(objX), GLdouble(objY), GLdouble(objZ), arrays.GLdoubleArray(model), arrays.GLdoubleArray(proj), arrays.GLintArray(view), arrays.GLdoubleArray(winX), arrays.GLdoubleArray(winY), arrays.GLdoubleArray(winZ) ) -> GLint', 
    argNames=('objX', 'objY', 'objZ', 'model', 'proj', 'view', 'winX', 'winY', 'winZ'),
)


# /usr/include/GL/glu.h 317
gluPwlCurve = platform.createBaseFunction( 
    'gluPwlCurve', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUnurbs),GLint,arrays.GLfloatArray,GLint,GLenum],
    doc='gluPwlCurve( POINTER(GLUnurbs)(nurb), GLint(count), arrays.GLfloatArray(data), GLint(stride), GLenum(type) ) -> None', 
    argNames=('nurb', 'count', 'data', 'stride', 'type'),
)


# /usr/include/GL/glu.h 318
gluQuadricCallback = platform.createBaseFunction( 
    'gluQuadricCallback', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLenum,_GLUfuncptr],
    doc='gluQuadricCallback( POINTER(GLUquadric)(quad), GLenum(which), _GLUfuncptr(CallBackFunc) ) -> None', 
    argNames=('quad', 'which', 'CallBackFunc'),
)


# /usr/include/GL/glu.h 319
gluQuadricDrawStyle = platform.createBaseFunction( 
    'gluQuadricDrawStyle', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLenum],
    doc='gluQuadricDrawStyle( POINTER(GLUquadric)(quad), GLenum(draw) ) -> None', 
    argNames=('quad', 'draw'),
)


# /usr/include/GL/glu.h 320
gluQuadricNormals = platform.createBaseFunction( 
    'gluQuadricNormals', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLenum],
    doc='gluQuadricNormals( POINTER(GLUquadric)(quad), GLenum(normal) ) -> None', 
    argNames=('quad', 'normal'),
)


# /usr/include/GL/glu.h 321
gluQuadricOrientation = platform.createBaseFunction( 
    'gluQuadricOrientation', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLenum],
    doc='gluQuadricOrientation( POINTER(GLUquadric)(quad), GLenum(orientation) ) -> None', 
    argNames=('quad', 'orientation'),
)


# /usr/include/GL/glu.h 322
gluQuadricTexture = platform.createBaseFunction( 
    'gluQuadricTexture', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLboolean],
    doc='gluQuadricTexture( POINTER(GLUquadric)(quad), GLboolean(texture) ) -> None', 
    argNames=('quad', 'texture'),
)


# /usr/include/GL/glu.h 323
gluScaleImage = platform.createBaseFunction( 
    'gluScaleImage', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLenum,GLsizei,GLsizei,GLenum,c_void_p,GLsizei,GLsizei,GLenum,POINTER(GLvoid)],
    doc='gluScaleImage( GLenum(format), GLsizei(wIn), GLsizei(hIn), GLenum(typeIn), c_void_p(dataIn), GLsizei(wOut), GLsizei(hOut), GLenum(typeOut), POINTER(GLvoid)(dataOut) ) -> GLint', 
    argNames=('format', 'wIn', 'hIn', 'typeIn', 'dataIn', 'wOut', 'hOut', 'typeOut', 'dataOut'),
)


# /usr/include/GL/glu.h 324
gluSphere = platform.createBaseFunction( 
    'gluSphere', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUquadric),GLdouble,GLint,GLint],
    doc='gluSphere( POINTER(GLUquadric)(quad), GLdouble(radius), GLint(slices), GLint(stacks) ) -> None', 
    argNames=('quad', 'radius', 'slices', 'stacks'),
)


# /usr/include/GL/glu.h 325
gluTessBeginContour = platform.createBaseFunction( 
    'gluTessBeginContour', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluTessBeginContour( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 326
gluTessBeginPolygon = platform.createBaseFunction( 
    'gluTessBeginPolygon', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),POINTER(GLvoid)],
    doc='gluTessBeginPolygon( POINTER(GLUtesselator)(tess), POINTER(GLvoid)(data) ) -> None', 
    argNames=('tess', 'data'),
)


# /usr/include/GL/glu.h 327
gluTessCallback = platform.createBaseFunction( 
    'gluTessCallback', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),GLenum,_GLUfuncptr],
    doc='gluTessCallback( POINTER(GLUtesselator)(tess), GLenum(which), _GLUfuncptr(CallBackFunc) ) -> None', 
    argNames=('tess', 'which', 'CallBackFunc'),
)


# /usr/include/GL/glu.h 328
gluTessEndContour = platform.createBaseFunction( 
    'gluTessEndContour', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluTessEndContour( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 329
gluTessEndPolygon = platform.createBaseFunction( 
    'gluTessEndPolygon', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator)],
    doc='gluTessEndPolygon( POINTER(GLUtesselator)(tess) ) -> None', 
    argNames=('tess',),
)


# /usr/include/GL/glu.h 330
gluTessNormal = platform.createBaseFunction( 
    'gluTessNormal', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),GLdouble,GLdouble,GLdouble],
    doc='gluTessNormal( POINTER(GLUtesselator)(tess), GLdouble(valueX), GLdouble(valueY), GLdouble(valueZ) ) -> None', 
    argNames=('tess', 'valueX', 'valueY', 'valueZ'),
)


# /usr/include/GL/glu.h 331
gluTessProperty = platform.createBaseFunction( 
    'gluTessProperty', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),GLenum,GLdouble],
    doc='gluTessProperty( POINTER(GLUtesselator)(tess), GLenum(which), GLdouble(data) ) -> None', 
    argNames=('tess', 'which', 'data'),
)


# /usr/include/GL/glu.h 332
gluTessVertex = platform.createBaseFunction( 
    'gluTessVertex', dll=platform.GLU, resultType=None, 
    argTypes=[POINTER(GLUtesselator),arrays.GLdoubleArray,POINTER(GLvoid)],
    doc='gluTessVertex( POINTER(GLUtesselator)(tess), arrays.GLdoubleArray(location), POINTER(GLvoid)(data) ) -> None', 
    argNames=('tess', 'location', 'data'),
)


# /usr/include/GL/glu.h 333
gluUnProject = platform.createBaseFunction( 
    'gluUnProject', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLdouble,GLdouble,GLdouble,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLintArray,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='gluUnProject( GLdouble(winX), GLdouble(winY), GLdouble(winZ), arrays.GLdoubleArray(model), arrays.GLdoubleArray(proj), arrays.GLintArray(view), arrays.GLdoubleArray(objX), arrays.GLdoubleArray(objY), arrays.GLdoubleArray(objZ) ) -> GLint', 
    argNames=('winX', 'winY', 'winZ', 'model', 'proj', 'view', 'objX', 'objY', 'objZ'),
)


# /usr/include/GL/glu.h 334
gluUnProject4 = platform.createBaseFunction( 
    'gluUnProject4', dll=platform.GLU, resultType=GLint, 
    argTypes=[GLdouble,GLdouble,GLdouble,GLdouble,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLintArray,GLdouble,GLdouble,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='gluUnProject4( GLdouble(winX), GLdouble(winY), GLdouble(winZ), GLdouble(clipW), arrays.GLdoubleArray(model), arrays.GLdoubleArray(proj), arrays.GLintArray(view), GLdouble(nearVal), GLdouble(farVal), arrays.GLdoubleArray(objX), arrays.GLdoubleArray(objY), arrays.GLdoubleArray(objZ), arrays.GLdoubleArray(objW) ) -> GLint', 
    argNames=('winX', 'winY', 'winZ', 'clipW', 'model', 'proj', 'view', 'nearVal', 'farVal', 'objX', 'objY', 'objZ', 'objW'),
)

__all__ = [
    'GLU_AUTO_LOAD_MATRIX',
    'GLU_BEGIN',
    'GLU_CCW',
    'GLU_CULLING',
    'GLU_CW',
    'GLU_DISPLAY_MODE',
    'GLU_DOMAIN_DISTANCE',
    'GLU_EDGE_FLAG',
    'GLU_END',
    'GLU_ERROR',
    'GLU_EXTENSIONS',
    'GLU_EXTERIOR',
    'GLU_FALSE',
    'GLU_FILL',
    'GLU_FLAT',
    'GLU_INCOMPATIBLE_GL_VERSION',
    'GLU_INSIDE',
    'GLU_INTERIOR',
    'GLU_INVALID_ENUM',
    'GLU_INVALID_OPERATION',
    'GLU_INVALID_VALUE',
    'GLU_LINE',
    'GLU_MAP1_TRIM_2',
    'GLU_MAP1_TRIM_3',
    'GLU_NONE',
    'GLU_NURBS_BEGIN',
    'GLU_NURBS_BEGIN_DATA',
    'GLU_NURBS_BEGIN_DATA_EXT',
    'GLU_NURBS_BEGIN_EXT',
    'GLU_NURBS_COLOR',
    'GLU_NURBS_COLOR_DATA',
    'GLU_NURBS_COLOR_DATA_EXT',
    'GLU_NURBS_COLOR_EXT',
    'GLU_NURBS_END',
    'GLU_NURBS_END_DATA',
    'GLU_NURBS_END_DATA_EXT',
    'GLU_NURBS_END_EXT',
    'GLU_NURBS_ERROR',
    'GLU_NURBS_ERROR1',
    'GLU_NURBS_ERROR10',
    'GLU_NURBS_ERROR11',
    'GLU_NURBS_ERROR12',
    'GLU_NURBS_ERROR13',
    'GLU_NURBS_ERROR14',
    'GLU_NURBS_ERROR15',
    'GLU_NURBS_ERROR16',
    'GLU_NURBS_ERROR17',
    'GLU_NURBS_ERROR18',
    'GLU_NURBS_ERROR19',
    'GLU_NURBS_ERROR2',
    'GLU_NURBS_ERROR20',
    'GLU_NURBS_ERROR21',
    'GLU_NURBS_ERROR22',
    'GLU_NURBS_ERROR23',
    'GLU_NURBS_ERROR24',
    'GLU_NURBS_ERROR25',
    'GLU_NURBS_ERROR26',
    'GLU_NURBS_ERROR27',
    'GLU_NURBS_ERROR28',
    'GLU_NURBS_ERROR29',
    'GLU_NURBS_ERROR3',
    'GLU_NURBS_ERROR30',
    'GLU_NURBS_ERROR31',
    'GLU_NURBS_ERROR32',
    'GLU_NURBS_ERROR33',
    'GLU_NURBS_ERROR34',
    'GLU_NURBS_ERROR35',
    'GLU_NURBS_ERROR36',
    'GLU_NURBS_ERROR37',
    'GLU_NURBS_ERROR4',
    'GLU_NURBS_ERROR5',
    'GLU_NURBS_ERROR6',
    'GLU_NURBS_ERROR7',
    'GLU_NURBS_ERROR8',
    'GLU_NURBS_ERROR9',
    'GLU_NURBS_MODE',
    'GLU_NURBS_MODE_EXT',
    'GLU_NURBS_NORMAL',
    'GLU_NURBS_NORMAL_DATA',
    'GLU_NURBS_NORMAL_DATA_EXT',
    'GLU_NURBS_NORMAL_EXT',
    'GLU_NURBS_RENDERER',
    'GLU_NURBS_RENDERER_EXT',
    'GLU_NURBS_TESSELLATOR',
    'GLU_NURBS_TESSELLATOR_EXT',
    'GLU_NURBS_TEXTURE_COORD',
    'GLU_NURBS_TEXTURE_COORD_DATA',
    'GLU_NURBS_TEX_COORD_DATA_EXT',
    'GLU_NURBS_TEX_COORD_EXT',
    'GLU_NURBS_VERTEX',
    'GLU_NURBS_VERTEX_DATA',
    'GLU_NURBS_VERTEX_DATA_EXT',
    'GLU_NURBS_VERTEX_EXT',
    'GLU_OBJECT_PARAMETRIC_ERROR',
    'GLU_OBJECT_PARAMETRIC_ERROR_EXT',
    'GLU_OBJECT_PATH_LENGTH',
    'GLU_OBJECT_PATH_LENGTH_EXT',
    'GLU_OUTLINE_PATCH',
    'GLU_OUTLINE_POLYGON',
    'GLU_OUTSIDE',
    'GLU_OUT_OF_MEMORY',
    'GLU_PARAMETRIC_ERROR',
    'GLU_PARAMETRIC_TOLERANCE',
    'GLU_PATH_LENGTH',
    'GLU_POINT',
    'GLU_SAMPLING_METHOD',
    'GLU_SAMPLING_TOLERANCE',
    'GLU_SILHOUETTE',
    'GLU_SMOOTH',
    'GLU_TESS_BEGIN',
    'GLU_TESS_BEGIN_DATA',
    'GLU_TESS_BOUNDARY_ONLY',
    'GLU_TESS_COMBINE',
    'GLU_TESS_COMBINE_DATA',
    'GLU_TESS_COORD_TOO_LARGE',
    'GLU_TESS_EDGE_FLAG',
    'GLU_TESS_EDGE_FLAG_DATA',
    'GLU_TESS_END',
    'GLU_TESS_END_DATA',
    'GLU_TESS_ERROR',
    'GLU_TESS_ERROR1',
    'GLU_TESS_ERROR2',
    'GLU_TESS_ERROR3',
    'GLU_TESS_ERROR4',
    'GLU_TESS_ERROR5',
    'GLU_TESS_ERROR6',
    'GLU_TESS_ERROR7',
    'GLU_TESS_ERROR8',
    'GLU_TESS_ERROR_DATA',
    'GLU_TESS_MAX_COORD',
    'GLU_TESS_MISSING_BEGIN_CONTOUR',
    'GLU_TESS_MISSING_BEGIN_POLYGON',
    'GLU_TESS_MISSING_END_CONTOUR',
    'GLU_TESS_MISSING_END_POLYGON',
    'GLU_TESS_NEED_COMBINE_CALLBACK',
    'GLU_TESS_TOLERANCE',
    'GLU_TESS_VERTEX',
    'GLU_TESS_VERTEX_DATA',
    'GLU_TESS_WINDING_ABS_GEQ_TWO',
    'GLU_TESS_WINDING_NEGATIVE',
    'GLU_TESS_WINDING_NONZERO',
    'GLU_TESS_WINDING_ODD',
    'GLU_TESS_WINDING_POSITIVE',
    'GLU_TESS_WINDING_RULE',
    'GLU_TRUE',
    'GLU_UNKNOWN',
    'GLU_U_STEP',
    'GLU_VERSION',
    'GLU_VERSION_1_1',
    'GLU_VERSION_1_2',
    'GLU_VERSION_1_3',
    'GLU_VERTEX',
    'GLU_V_STEP',
    'GLUnurbs',
    'GLUnurbsObj',
    'GLUquadric',
    'GLUquadricObj',
    'GLUtesselator',
    'GLUtesselatorObj',
    'GLUtriangulatorObj',
    'GLboolean',
    'GLdouble',
    'GLenum',
    'GLfloat',
    'GLint',
    'GLsizei',
    'GLubyte',
    'GLvoid',
    '_GLUfuncptr',
    'gluBeginCurve',
    'gluBeginPolygon',
    'gluBeginSurface',
    'gluBeginTrim',
    'gluBuild1DMipmapLevels',
    'gluBuild1DMipmaps',
    'gluBuild2DMipmapLevels',
    'gluBuild2DMipmaps',
    'gluBuild3DMipmapLevels',
    'gluBuild3DMipmaps',
    'gluCheckExtension',
    'gluCylinder',
    'gluDeleteNurbsRenderer',
    'gluDeleteQuadric',
    'gluDeleteTess',
    'gluDisk',
    'gluEndCurve',
    'gluEndPolygon',
    'gluEndSurface',
    'gluEndTrim',
    'gluErrorString',
    'gluGetNurbsProperty',
    'gluGetString',
    'gluGetTessProperty',
    'gluLoadSamplingMatrices',
    'gluLookAt',
    'gluNewNurbsRenderer',
    'gluNewQuadric',
    'gluNewTess',
    'gluNextContour',
    'gluNurbsCallback',
    'gluNurbsCallbackData',
    'gluNurbsCallbackDataEXT',
    'gluNurbsCurve',
    'gluNurbsProperty',
    'gluNurbsSurface',
    'gluOrtho2D',
    'gluPartialDisk',
    'gluPerspective',
    'gluPickMatrix',
    'gluProject',
    'gluPwlCurve',
    'gluQuadricCallback',
    'gluQuadricDrawStyle',
    'gluQuadricNormals',
    'gluQuadricOrientation',
    'gluQuadricTexture',
    'gluScaleImage',
    'gluSphere',
    'gluTessBeginContour',
    'gluTessBeginPolygon',
    'gluTessCallback',
    'gluTessEndContour',
    'gluTessEndPolygon',
    'gluTessNormal',
    'gluTessProperty',
    'gluTessVertex',
    'gluUnProject',
    'gluUnProject4'
]
