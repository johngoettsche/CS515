#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser
from math import sqrt

def isPrime(n) :
	root = sqrt(n)
	if root >= 2 :
		for i in range(2, int(root) + 1) :
			if n % i == 0 : return False
	return True

def main() :
	parser = OptionParser(usage="usage: %prog [options] file")
	parser.add_option("-n", "--number", dest="num", default="100", help="number of primes")
	(options, args) = parser.parse_args()
	
	num = int(options.num)
	
	print(2, end=" ")
	
	n = 3
	count = 1
	while count < num :
		if isPrime(n) : 
			print(n, end=" ")
			count += 1
		n += 2
		
main()