#!/usr/bin/env python3

plist = [-1 for x in range(101)]
def P(n) :
	if plist[n] != -1 :
		return plist[n]
	if n <= 1 :
		plist[n] = 1
		return 1
	else :
		plist[n] = P(n - 1) * ((365 - (n - 1)) / 365.0)
		return P(n - 1) * ((365 - (n - 1)) / 365.0)	

def main() :
	for x in range(1, 101) :
		match = P(x)
		result = round(1 - match, 4)
		print(x, result)
		
main()
