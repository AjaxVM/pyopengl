'''OpenGL extension EXT.framebuffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.framebuffer_object to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/framebuffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.framebuffer_object import *

def glInitFramebufferObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy 

glGenFramebuffersEXT = wrapper.wrapper(glGenFramebuffersEXT).setOutput(
                'framebuffers', 
                lambda x: (x,), 
                'n')
                
glGenRenderbuffersEXT = wrapper.wrapper(glGenRenderbuffersEXT).setOutput(
                'renderbuffers', 
                lambda x: (x,), 
                'n')

@lazy( glDeleteFramebuffersEXT )
def glDeleteFramebuffersEXT( baseOperation, n, framebuffers=None ):
    """glDeleteFramebuffersEXT( framebuffers ) -> None 
    """
    if framebuffers is None:
        framebuffers = arrays.GLuintArray.asArray( n )
        n = arrays.GLuintArray.arraySize( framebuffers )
    return baseOperation( n, framebuffers )

#glBindRenderbufferEXT # doesn't require wrapping
#glBindFramebufferEXT  # doesn't require wrapping
#glBindRenderbufferEXT # doesn't require wrapping
#glCheckFramebufferStatusEXT
#glDeleteFramebuffersEXT # should be wrapped to eliminate 'length'
#glDeleteRenderbuffersEXT # should be wrapped to eliminate 'length'
#glFramebufferRenderbufferEXT
#glFramebufferTexture1DEXT
#glFramebufferTexture2DEXT
#glFramebufferTexture3DEXT
#glGenFramebuffersEXT  # wrapped
#glGenRenderbuffersEXT # wrapped
#glGenerateMipmapEXT
#glGetFramebufferAttachmentParameterivEXT
#glGetRenderbufferParameterivEXT
#glInitFramebufferObjectEXT
#glIsFramebufferEXT
#glIsRenderbufferEXT
#glRenderbufferStorageEXT # doesn't require wrapping                                          
#glget.addGLGetConstant( GL_MAX_COLOR_ATTACHMENTS_EXT, (1,))
#glget.addGLGetConstant( GL_FRAMEBUFFER_BINDING_EXT, (1,))
#glget.addGLGetConstant( GL_RENDERBUFFER_BINDING_EXT, (1,))
#glget.addGLGetConstant( GL_MAX_RENDERBUFFER_SIZE_EXT, (1,))