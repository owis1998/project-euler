for n in range(1, 50):
	for m in range(n + 1, 51):
		a = m*m - n*n
		b = 2 * m * n
		c = m**2 + n**2
		if a + b + c == 1000:
			print("a = {}, b = {}, c = {}".format(a, b, c))
			print("a * b * c = {}".format(a*b*c))
			quit()
