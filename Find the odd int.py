from collections import Counter

def findOdd(seq):
	return [x for x in seq if seq.count(x) % 2][0]

print(findOdd([1,1,1,1,1,1,10,1,1,1,1] ))