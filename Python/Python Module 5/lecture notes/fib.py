import time
import ctypes

# C implementation of fib with Python wrapper
# gcc -shared -o fib.so -fPIC fib.c
_libc = ctypes.CDLL('fib.so')
c_fib = _libc.fib
c_fib.restype = int
c_fib.argtypes = [ctypes.c_int]

# python implementation of fib
def py_fib(n):
	if n<2:
		return n
	return py_fib(n-1) + py_fib(n-2)

#benchmark
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