def fibonacci_sequence(n):
	sum = 0
	x1 = 0
	x2 = 1

	while sum <= n:
		x3 = x2
		x2 += x1
		x1 = x3

		if x2 % 2 == 0:
			sum += x2

	return sum
