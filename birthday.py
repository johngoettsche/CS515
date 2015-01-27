#!/usr/bin/env python3
from cs515lib import *

def P(n) :
	return P(n - 1) * ((365 - n) / 365)

def main() :
	x = readInt()
	print(x)
