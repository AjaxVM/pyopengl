'''OpenGL extension NV.native_query

This module customises the behaviour of the 
OpenGL.raw.EGL.NV.native_query to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/native_query.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.NV.native_query import *

def glInitNativeQueryNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION