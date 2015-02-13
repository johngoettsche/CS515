#!/usr/bin/env python3
from lib515 import *

def main():
	substMat = readSubstMat()
	eastStr = readStr()
	souStr = readStr()
	(fMat, dirMat) = dynamic(substMat, eastStr, souStr)
	printMatrix(fMat)
	printMatrix(dirMat)
	print("done.")

def readSubstMat():
	substList = readListStr()
	print(substList)
	print(len(substList))
	
	subst = {}
	for i in substList:
		values = readListInt()
		for j in substList:
			subst[i + j] = values.pop(0)
	print(subst)
	
	gap = readInt()
	print(gap)
	
	return(gap, subst)
	
def dynamic(substMat, estStr, souStr):
	(east, south, both, neither) = range(4)
	dirLabel = "-1SX"
	(gap, subst) = substMat
	lene = len(estStr) + 2
	lens = len(souStr) + 2
	f = zeros(lens, lene)
	direc = zeros(lens, lene, neither)
	print(str(lene))
	print(str(lens))
	print()
	for e in range(1, lene): 
		for s in range(1, lens):
			if e == 0 :
				if s == 0 :
					f[0][0] = 0
				else :
					f[s][0] = f[s - 1][0] + gap
					direc[s][0] = south
			else :
				if s == 0 :
					f[0][e] = f[0][e - 1] + gap
					direc[0][e] = east
				else :
					(whichOne, f[s][e]) = maxarg([f[s][e-1]+gap, f[s-1][e]+gap, f[s-1][e-1]+subst[souStr[s-1]+estStr[e-1]]])
					direc[s][e] = (east, south, both)[whichOne]
					
	#for s in range(0, lens) :
	#	for e in range(0, lene) :
	#		print(str(f[s][e]).rjust(6))
	#	print("-")
	return (f, direc)
	
main()