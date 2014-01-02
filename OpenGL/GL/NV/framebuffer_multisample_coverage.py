'''OpenGL extension NV.framebuffer_multisample_coverage

This module customises the behaviour of the 
OpenGL.raw.GL.NV.framebuffer_multisample_coverage to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/framebuffer_multisample_coverage.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.framebuffer_multisample_coverage import *

def glInitFramebufferMultisampleCoverageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION