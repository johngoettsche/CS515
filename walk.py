#!/usr/bin/env python3

table = [[0 for x in range(13)] for x in range(13)]
tableWidths = [0 for x in range(-1, 13)]
def w(N, E) :
	if table[N][E] != 0 :
		return table[N][E]
	else :
		if N == 0 or E == 0:
			table[N][E] = 1
		else :
			table[N][E] = w(N - 1, E) + w(N, E - 1)
		return table[N][E]
		
def setColWidth() :
	tableWidths[-1] = 2
	for n in range(0, 13) :
		for e in range(0, 13) :
			if len(str(table[n][e])) > tableWidths[e] :
				tableWidths[e] = len(str(table[n][e]))
				
def printTable() :
	for n in range(-1, 13) :
		for e in range(-1, 13) :
			if n < 0 or e < 0 :
				if n == e :
					print("x".rjust(tableWidths[e]), end=" ")
				else :
					if n < 0 :
						print(str(e).rjust(tableWidths[e]), end=" ")
					if e < 0 :
						print(str(n).rjust(tableWidths[e]), end=" ")
			else :
				print(str(table[n][e]).rjust(tableWidths[e]), end=" ")
		print()

def main() :
	for n in range(0, 13) :
		for e in range(0, 13) :
			w(n, e)
	setColWidth()
	printTable()
			
main()
		