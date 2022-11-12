from distutils.core import setup, Extension
import numpy
import os
os.environ['LDFLAGS'] = '-framework Carbon'

# define the extension module
twed = Extension('twed', sources=['twed.c'])

# run the setup
setup(ext_modules=[twed])
