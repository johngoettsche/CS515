#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser

def main() :
	parser = OptionParser(usage="usage: %prog [options] file")
	parser.add_option("-a", "--alphabet", dest="alpha", default="abcdefghijklmnopqrstuvwxyz", help="characters to consider")
	parser.add_option("-n", "--number", dest="num", default="100", help="number")
	parser.add_option("-s", "--spaces", dest="spaces", action="store_true", default=False, help="allow spaces")
	(options, args) = parser.parse_args()
	
	if len(args) != 1 :
		parser.print_help()
		exit(1)
	filename = args[0]
	examplein = open(filename, "r")
	example = examplein.read().lower()
	
	total = 0
	count1 = {}
	count2 = {}
	for i in alpha :
		count1[i] = 0
		for j in alpha :
			count2[i+j] = 0
	last = None
	for c in example :
		if c in alpha :
			total += 1
			count2[last+c] += 1
		count1[c] +=1
		last = c
		
	for i in alpha :
		for j in alpha :
			if count2[i+j] != 0 :
				count2[i+j] /= count1[i]
	
	for i in alpha :
		count1[i] /= total
		
	print(count1)
	
main()