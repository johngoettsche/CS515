#!/usr/bin/env python3
from lib515 import *

def main():
	substMat = readSubstMat()
	eastStr = readStr()
	souStr = readStr()
	(fMat, dirMat) = dynamic(substMat, eastStr, souStr)
	printMatrix(fMat)
	print()
	printMatrix(dirMat)
	(estRes, souRes) = path(dirMat, eastStr, souStr)
	print(estRes)
	print(souRes)

def readSubstMat():
	substList = readListStr()
	subst = {}
	for i in substList:
		values = readListNum()
		for j in substList:
			subst[i + j] = values.pop(0)
	gap = readNum()	
	return(gap, subst)
	
def dynamic(substMat, estStr, souStr):
	(east, south, both, neither) = range(4)
	(gap, subst) = substMat
	lene = len(estStr) + 2
	lens = len(souStr) + 2
	f = zeros(lens, lene)
	direc = zeros(lens, lene, neither)
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
					(whichOne, f[s][e]) = argmax([f[s][e-1]+gap, f[s-1][e]+gap, f[s-1][e-1]+subst[souStr[s-2]+estStr[e-2]]])
					direc[s][e] = (east, south, both)[whichOne]
	return (f, direc)
	
def path(dirMat, estStr, souStr):
	(east, south, both, neither) = range(4)
	e = len(estStr) + 1
	s = len(souStr) + 1
	estRes = ""
	souRes = ""
	while dirMat[s][e] != neither :
		if dirMat[s][e] == east :
			estRes = estStr[e - 2] + estRes
			souRes = "-" + souRes
			e = e - 1
		if dirMat[s][e] == south :
			estRes = "|" + estRes
			souRes = souStr[s - 2] + souRes
			s = s - 1
		if dirMat[s][e] == both :
			estRes = estStr[e - 2] + estRes
			souRes = souStr[s - 2] + souRes
			e = e - 1
			s = s - 1
	return (estRes, souRes)

main()