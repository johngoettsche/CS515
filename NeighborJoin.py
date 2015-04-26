#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser
from random import *

def calcD(dist):
	D = []
	for i in range(0, len(dist)):
		row = []
		sumdi = 0
		sumdj = 0
		for j in range(0, i):
			for z in range(0, len(dist)):
				if (z != i) and (z != j):
					if i > z: sumdi += dist[i][z]
					else: sumdi += dist[z][i]
					if j > z: sumdj += dist[j][z]
					else: sumdj += dist[z][j]
			ri = sumdi / (len(dist) - 2)
			rj = sumdj / (len(dist) - 2)
			row.append(dist[i][j] - (ri + rj))
		D.append(row)
	return D
	
def calcEdges(dist, D, merge):


	for k in range(0, len(merge)):
		if merge[k] is tuple:
			
		
			(left, right) = merge[k]
			left = dist[left, right] + D[
			

def main():
	names = readListStr()
	dist = [[]]
	for i in range(0, len(names) - 1):
		dist.append(readListNum())
	size = len(names) * [1]
	ok = len(names) * [True]
	height = len(names) * [0]
	length = len(names) * [0]
	merge = list(range(0, len(names)))
	
	print(names)
	print("dist: ", dist)
	D = calcD(dist)
	print("D: ", D)
	
	for joins in range(1, len(names)):
		theMin = None
		for i in range(0, len(D)):
			if ok[i]:
				for j in range(0, i):
					if ok[j] and ((theMin == None) or (D[i][j] < theMin)):
						theMin = D[i][j]
						ij = (i, j)
						
		(i, j) = ij
		ok[i] = ok[j] = False
		print("ok: ", ok)
	
		k = len(D)
		sizek = size[i] + size[j]
		
		#height.append(dist[i][j] / 2)
		
		newDRow = []
		newDistRow = []
		for z in range(0, k):
			if ok[z]:
				if i > z: Diz = D[i][z]
				else: Diz = D[z][i]
				if j > z: Djz = D[j][z]
				else: Djz = D[z][j]
				if i > z: diz = dist[i][z]
				else: diz = dist[z][i]
				if j > z: djz = dist[j][z]
				else: djz = dist[z][j]
				newDistRow.append((size[i] * diz + size[j] * djz) / sizek)
				newDRow.append((size[i] * Diz + size[j] * Djz) / sizek)
			else :
				newDistRow.append(None)
				newDRow.append(None)
		
		D.append(newDRow)
		dist.append(newDistRow)
		merge.append(ij)
		size.append(sizek)
		ok.append(True)
	
#	print("height: ", height)
	print("merge: ", merge)
	print("size: ", size)
	print("ok: ", ok)
	print("D: ", D)
	print("dist: ", dist)
main()