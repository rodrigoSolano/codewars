from itertools import permutations
from collections import Counter
def listPosition(word):
	listCar = list(word)
	per = list(permutations(listCar,len(listCar)))
	per.sort()
	per = ["".join(x) for x in per]
	print(per)
	diccionario = dict()
	j = 1
	for word in per:
		diccionario[word] = j
		j = j + 1
	return diccionario["".join(listCar)]

print(listPosition("BAAA"))
