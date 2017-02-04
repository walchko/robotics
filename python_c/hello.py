
import numpy
import ctypes

_libhello = numpy.ctypeslib.load_library('libhello', './lib')

_libhello.hello.argtypes = [ctypes.c_int]
_libhello.hello.restype  =  ctypes.c_int

def hello(n):
    return _libhello.hello(int(n))