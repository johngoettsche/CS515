'''Library of simple helpful functions and definitions for 
CS515 class.'''

import sys

# a cheap form of the numpy zeros routine
# for index range 0 to x-1 and 0 to y-1
def zeros(x, y, value=0.0) :
    l = []
    for i in range(0, x) : 
        l.append(y * [value])
    return l

# print out a matrix
def printMatrix(mat) :
	for line in mat :
		for item in line :
			#sys.stdout.write("%d", item)
			print(str(item).rjust(6))
			#print("\b" + str(len(line)))
		#print()


# returns tuple (location of maximum, maximum value)
# Assumes list is nonempty.
def maxarg(s):
    max = s[0];
    maxa = 0;
    for i in range(1, len(s)) :
        if s[i]>max:
            max = s[i]
            maxa = i
    return (maxa, max)

def readStr() :
    return sys.stdin.readline().rstrip()

def readFloat() :
    return float(sys.stdin.readline().rstrip())

def readInt() :
    return int(sys.stdin.readline().rstrip())

def readListStr() :
    return sys.stdin.readline().rstrip().split()

def readListFloat() :
    return [float(x) for x in sys.stdin.readline().rstrip().split()]

def readListInt() :
    return [int(x) for x in sys.stdin.readline().rstrip().split()]
