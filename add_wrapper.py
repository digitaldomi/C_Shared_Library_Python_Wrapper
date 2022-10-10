from ctypes import *
from sys import platform

shared_lib_path = "./libfoo.so"
if platform.startswith('win32'):
    shared_lib_path = "./libfoo.dll"
try:
    add_lib = CDLL(shared_lib_path)
    print("Successfully loaded ", add_lib)
except Exception as e:
    print(e)

add_lib.foo()
