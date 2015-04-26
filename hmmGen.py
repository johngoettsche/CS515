#!/usr/bin/env python3
from lib515 import *
from optparse import OptionParser
from random import *

def readPList(file) :
	pList = []
	items = int(file.readline().rstrip())
	for i in range(items) :
		l = file.readline().rstrip().split()
		prob = float(l[0])
		label = l[1]
		pList.append(tuple((prob, label)))
	return pList

def readState(hmm, file) :
	stateTrans = readPList(file)
	probabilities = readPList(file)
	state = tuple((stateTrans, probabilities))
	return state

def readHMM(file) :
	HMM = {}
	states = int(file.readline().rstrip())
	for s in range(states) :
		stateName = file.readline().rstrip()
		HMM[stateName] = readState(HMM, file) 
	return HMM	
	
def pickState(hmm, current) :
	ran = random()
	if current != None :
		(stateOdds, itemOdds) = hmm[current]
		sum = 0.0
		for s in stateOdds :
			(p, state) = s
			sum += p
			if sum > ran :
				return (p, state)
		print("Pick State Error")
	else :
		keys = list(hmm.keys())
		return (1.0 / len(keys), choice(keys))
	
def pickItem(hmm, current) :
	ran = random()
	(stateOdds, itemOdds) = hmm[current]
	sum = 0.0
	for i in itemOdds :
		(p, item) = i
		sum += p
		if sum > ran :
			return i
	print("Pick Item Error")

def makeStrings(hmm, init, num) :
	current = init
	states = ""
	items = ""
	P = 1.0
	pState = 1.0
	for x in range(num) :
		if current != None : 
			i = pickItem(hmm, current)
		else : #in the event that the initial state is not defined
			(pState, current) = pickState(hmm, current)
			i = pickItem(hmm, current)
		states += current
		(p, item) = i
		items += item
		#P *= p * pState this is where it should go logically for the odds to get to this state and select this item
		(pState, current) = pickState(hmm, current)
		P *= p * pState #this is where it matches the calculations on the submission page
	return (states, items, P)

def main() :
	parser = OptionParser(usage="usage: %prog [options] file")
	parser.add_option("-n", "--number", dest="num", default="20", help="number of chars to generate")
	parser.add_option("-i", "--init", dest="init", default=None, help="initial state for string")
	(options, args) = parser.parse_args()
		
	if len(args) != 1 :
		parser.print_help()
		exit(1)
	init = options.init
	num = int(options.num)
	filename = args[0]
	file = open(filename, "r")
	HMM = readHMM(file)
	print(HMM)
	(states, items, P) = makeStrings(HMM, init, num)
	print(states)
	print(items)
	print(P)
	
main()
