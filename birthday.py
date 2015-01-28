#!/usr/bin/env python3

def P(n) :
	if n <= 1 :
		return 1
	else :
		return P(n - 1) * ((365 - (n - 1)) / 365.0)
		
def main() :
	for x in range(1, 101) :
		match = P(x)
		result = round(1 - match, 4)
		print(x, result)
		
main()
