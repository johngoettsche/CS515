#!/usr/bin/env python3
from lib515 import *

def main():
	substMat = readSubstMat()
	eastStr = readStr()
	souStr = readStr()
	(fMat, dirMat, map) = dynamic(substMat, eastStr, souStr)
	
	print("\nThe directions:")
	printMatrix(map)
	print("\nThe scores:")
	printMatrix(fMat)
	(estRes, souRes, score) = path(dirMat, fMat, eastStr, souStr)
	print("\nScore: %6s"%score)
	print("Alignment")
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
	lene = len(estStr) + 1
	lens = len(souStr) + 1
	f = zeros(lens, lene)
	map = zeros(lens, lene, ".")
	direc = zeros(lens, lene, neither)
	for e in range(0, lene): 
		for s in range(0, lens):
			if e == 0 :
				if s == 0 :
					f[s][e] = 0
				else :
					f[s][e] = f[s - 1][e] + gap
					direc[s][e] = south
					map[s][e] = "|"
			else :
				if s == 0 :
					f[s][e] = f[s][e - 1] + gap
					direc[s][e] = east
					map[s][e] = "-"
				else :
					if s == lens :
						southGap = f[s-1][e]
					else :
						southGap = f[s-1][e]+gap
					(whichOne, f[s][e]) = argmax([f[s-1][e-1]+subst[souStr[s-1]+estStr[e-1]], f[s][e-1]+gap, southGap])
					direc[s][e] = (both, east, south)[whichOne]
					map[s][e] = ("\\", "-", "|")[whichOne]
	return (f, direc, map)
	
def path(dirMat, fMat, estStr, souStr):
	(east, south, both, neither) = range(4)
	s = len(souStr)
	southLine = [fMat[len(souStr)][e] for e in range(len(estStr) + 1)]
	(e, score) = argmax(southLine)
	estRes = ""
	souRes = ""
	while dirMat[s][e] != neither :
		if dirMat[s][e] == east :
			estRes = estStr[e - 1] + estRes
			souRes = "-" + souRes
			e = e - 1
		if dirMat[s][e] == south :
			estRes = "|" + estRes
			souRes = souStr[s - 1] + souRes
			s = s - 1
		if dirMat[s][e] == both :
			estRes = estStr[e - 1] + estRes
			souRes = souStr[s - 1] + souRes
			e = e - 1
			s = s - 1
	return (estRes, souRes, score)
	
main()