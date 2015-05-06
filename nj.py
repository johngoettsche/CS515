#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser
from random import *

#3 continued
def calcD(i, j, merge, dist, ok) :
	di = dj = 0.0
	n = 0
	for z in range(0, len(merge)) :
		if ok[z] :
			n += 1
			if z != i :
				if i > z :
					di += dist[i][z]
				else : 
					di += dist[z][i]
			if z != j :
				if j > z : 
					dj += dist[j][z]
				else : 
					dj += dist[z][j]

	ri = di / (n - 2)
	rj = dj / (n - 2)

#	if dist[i][j] == None : dist[i][j] = 0
	D = dist[i][j] - (ri + rj)
	return (D, ri, rj)
	
def okLen(ok) :
	n = 0
	for o in ok :
		if o == True : n += 1
	return n
			
def main():
	names = readListStr()
	dist = [[]]
#2
	for i in range(0, len(names) - 1):
		dist.append(readListNum())
	size = len(names) * [1]
	ok = len(names) * [True]
	edge = len(names) * [0]
	height = len(names) * [0]
	length = len(names) * [0]
	merge = list(range(0, len(names)))
	
	while okLen(ok) > 2:
		theMin = None
		for i in range(0, len(merge)):
			if ok[i]:
				for j in range(0, i):
					if ok[j]:
#3
						(D, ri, rj) = calcD(i, j, merge, dist, ok)
#4
						if ok[j] and ((theMin == None) or (D < theMin)):
							theMin = D
							ij = (i, j)
#5						
		(i, j) = ij
#6
		ok[i] = ok[j] = False
		k = len(merge)
		sizek = size[i] + size[j]
		newDistRow = []
#7
		for z in range(0, k):
			if ok[z]:
				diz = height[i]
				djz = height[j]
				if i > z: diz = dist[i][z]
				else: diz = dist[z][i]
				if j > z: djz = dist[j][z]
				else: djz = dist[z][j]
				newDistRow.append((diz + djz - dist[i][j]) / 2)
			else :
				newDistRow.append(None)
		
		dist.append(newDistRow)
		size.append(sizek)
#8		
		ei = (dist[i][j] + ri - rj) / 2
		ej = (dist[i][j] + rj - ri) / 2
		newEdge = ( ei, ej )
		edge.append(newEdge)
#9
		h = 10000000;
		if height[i] < h : h = height[i]
		if height[j] < h : h = height[j]
		height.append((dist[i][j] / 2) + h)
#10
		ok.append(True)
		merge.append(ij)
#11^
#12	
	for z in range(0, len(merge)):
		if ok[z] : 
			j = z
			ok[j] = False;
			break;
	for z in range(0, len(merge)):
		if ok[z] : 
			i = z
			ok[i] = False;
			break;
	ij = (i, j)
#	print(ij)
		
	dist.append(newDistRow)
#	print(dist[i][j])
	merge.append(ij)
	edge.append(dist[i][j])
	
	print(merge)
	print(size)
	print(edge)
main()