'''Library of simple helpful functions and definitions for 
CS515 class.'''

import sys

# a cheap form of the numpy zeros routine
def zeros(x, y, value=0.0) :
    l = []
    for i in range(0, x) : 
        l.append(y * [value])
    return l

# print out a matrix

#def printMatrix(mat) :
#	for line in mat :
#		for item in line :
#			#sys.stdout.write("%d", item)
#			print(str(item).rjust(6))
#			#print("\b" + str(len(line)))
#		#print()

def printMatrix(mat, symbol=None) :
    for line in mat :
        for item in line :
            if symbol==None :
                print("%6s "%item, end="")
            else :
                print("%6s "%symbol[item], end="")
        print()


# returns tuple (location of maximum, maximum value)
# where location of maximum is the location of the FIRST maximum
# Assumes list is nonempty.
def argmax(s, symbol=None):
    max = s[0];

    if symbol==None : maxa = 0;
    else : maxa = symbol[0]

    for i in range(1, len(s)) :
        if s[i]>max:
            max = s[i]

            if symbol==None : maxa = i
            else : maxa = symbol[i]

    return (maxa, max)

def readStr() :
    return sys.stdin.readline().rstrip()

def readNum() :
    return float(sys.stdin.readline().rstrip())

def readListStr() :
    return sys.stdin.readline().rstrip().split()

def readListNum() :
    return [float(x) for x in sys.stdin.readline().rstrip().split()]
