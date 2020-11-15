import math

def isPP(n):
	for base in range(2,n+1):
		k = math.log(n,base)
		k = round(k)
		if base*base > n:
			return None
		if base**k == n:
			return [base,k]
			
print(isPP(164130859375))