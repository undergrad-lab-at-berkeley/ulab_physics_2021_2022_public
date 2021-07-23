import time
import ctypes

# C implementation of fib with Python wrapper
# gcc -shared -o fib.so -fPIC fib.c
_libc = ctypes.CDLL('fib.so')
c_fib = _libc.fib
c_fib.restype = ctypes.c_int
c_fib.argtypes = [ctypes.c_int]

# python implementation of fib
def py_fib(n):
	if n<2:
		return n
	return py_fib(n-1) + py_fib(n-2)

#benchmark
start = 0
def tik():
	global start
	start = time.time()
def tok():
	end = time.time()
	print(f'\t{end-start:3f} sec')


print('py_fib(36): ')
tik()
print(f'\t{py_fib(36)}')
tok()

print('c_fib(36): ')
tik()
print(f'\t{c_fib(36)}')
tok()