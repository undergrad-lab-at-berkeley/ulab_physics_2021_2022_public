import time
import ctypes

### C implementation of fib ###
# import fib function from fib.so DLL
_libc = ctypes.CDLL('fib.so')
# python wrapper for C function
def c_fib(n):
	return _libc.fib(ctypes.c_int(n))

### python implementation of fib ###
def py_fib(n):
	if n<2:
		return n
	return py_fib(n-1) + py_fib(n-2)

print('py_fib(36): ')
start = time.time()
print(f'\tresult: {py_fib(36)}')
end = time.time()
print(f'\ttime: {end-start:.3f} sec')

print('c_fib(36): ')
start = time.time()
print(f'\tresult: {c_fib(36)}')
end = time.time()
print(f'\ttime: {end-start:.3f} sec')