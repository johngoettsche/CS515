#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser
from random import *

def calcD(i, j, size, dist) :
	di = dj = 0.0
	for z in range(0, size) :
		if z != i :
			if i > z :
				if dist[i][z] != None :
					di += float(str(dist[i][z]))
			else : 
				if dist[z][i] != None :
					di += dist[z][i]
		if z != j :
			if j > z : 
				if dist[j][z] != None :
					dj += dist[j][z]
			else : 
				if dist[z][j] != None :
					dj += dist[z][j]

	ri = (1 / (size - 2)) * di 
	rj = (1 / (size - 2)) * dj
	if ri == None : ri = 0
	if rj == None : rj = 0
	if dist[i][j] == None : dist[i][j] = 0
	D = (dist[i][j] - (ri + rj))
	return (D, ri, rj)
			
def main():
	names = readListStr()
	dist = [[]]
	for i in range(0, len(names) - 1):
		dist.append(readListNum())
	size = len(names) * [1]
	ok = len(names) * [True]
	#height = len(names) * [0]
	edge = len(names) * [0]
	length = len(names) * [0]
	merge = list(range(0, len(names)))
	
	print(names)
	print("dist: ", dist)
	
	for joins in range(1, len(names)):
		theMin = None
		for i in range(0, len(dist)):
			if ok[i]:
				for j in range(0, i):
					(D, ri, rj) = calcD(i, j, len(dist), dist)
					if ok[j] and ((theMin == None) or (D < theMin)):
						theMin = D
						ij = (i, j)
						
		(i, j) = ij
		ok[i] = ok[j] = False
	
		#for i in range(1, len(dist)) :
			#if ok[i] :
				#d = (ri + rj - dist(i, j)) / 2
			
		k = len(dist)
		sizek = size[i] + size[j]
		newDistRow = []
		for z in range(0, k):
			if ok[z]:
				if i > z: diz = dist[i][z]
				else: diz = dist[z][i]
				if j > z: djz = dist[j][z]
				else: djz = dist[z][j]
				newDistRow.append((diz + djz - dist[i][j]) / 2)
			else :
				newDistRow.append(None)
		
		newEdge = ( abs(dist[i][j] + ri - rj) / 2, abs(dist[i][j] + rj - ri) / 2 )
		edge.append(newEdge)
		#height.append(dist[i][j] / 2)
		
		#newDistRow = []
		#for z in range(0, k):
			#if ok[z]:
				#if i > z: diz = dist[i][z]
				#else: diz = dist[z][i]
				#if j > z: djz = dist[j][z]
				#else: djz = dist[z][j]
				#newDistRow.append((size[i] * diz + size[j] * djz) / sizek)
			#else :
				#newDistRow.append(None)
		
		dist.append(newDistRow)
		merge.append(ij)
		size.append(sizek)
		ok.append(True)
	
#	print("height: ", height)
	print("merge: ", merge)
	print("size: ", size)
	print("ok: ", ok)
	print("dist: ", dist)
	print("edge: ", edge)
main()