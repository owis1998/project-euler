import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def multiplyList(myList) :
    result = 1
    for x in myList:
         result *= x 
    return result

def largest_prime_factor(n):
	i = 1
	l = []
	while True:
		if multiplyList(l) >= n:
			return l[-1]

		if is_prime(i) and n % i == 0:
			l.append(i)

		i += 2
