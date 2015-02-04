#!/usr/bin/env python3
from lib515 import *

def main() :
	while True :
		x = readListInt()
		if (x[0]<0) :
			break
		print(x, comb(x[0], x[1]))
		
combtab = {}
def comb(n, m) :
	if n in combtab :
		return combtab[(n, m)]
		
	if m==0 or n==m :
		return 1
	else 
		ans = comb(n-1, m-1) + comb(n-1, m)
		combtab[(n, m)] = ans
		combtab[(n, n - m)] = ans
		return ans

fibtab = {}
def fib(n)
	if n in fibtab :
		return fibtab[n]
		
	if n <= 2 :
		return 1
	else :
		ans = fib(n - 1) + fib(n - 2)
		fibtab[n] = ans
		return ans