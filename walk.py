#!/usr/bin/env python3

def w(N, E) :
	if N == 0 or E == 0:
		return 1
	else :
		return w(N - 1, E) + w(N, E - 1)

def main() :
	table = [[0 for x in range(13)] for x in range(13)]
	for n in range(0, 13) :
		for e in range(0, 13) :
			table[n][e] = w(n, e)
			print(table[n][e])
			
main()
		