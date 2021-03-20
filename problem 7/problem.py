import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

n = 1
index = 1
while index != 10001:
	n += 2
	if is_prime(n):
		index += 1
	
print(n)
