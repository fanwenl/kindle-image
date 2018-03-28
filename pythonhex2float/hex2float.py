#from ctypes import *
#def convert(s):
#    i = int(s, 16)                   # convert from hex to a Python int
#    cp = pointer(c_int(i))           # make this into a c integer
#    fp = cast(cp, POINTER(c_double))  # cast the int pointer to a float pointer
#    return fp.contents.value         # dereference the pointer, get the float
#print(convert("404201D8F54FC275"))

import struct
'double 类型的'
a = struct.unpack('<d',bytes.fromhex('B6953D618E915A40'))[0]
print(a)
'struct.error: unpack requires a bytes object of length 4'

#import struct
#'float 类型的'
#a = struct.unpack('!f',bytes.fromhex('ffffffff'))[0]
#print(a)
#'如果在float类型中使用8字节的double将出现下面的错误'
#'struct.error: unpack requires a bytes object of length 4'