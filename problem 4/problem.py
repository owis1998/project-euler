def has_factor(n, m):
	i = m
	while i > m - 100:
		if n % i == 0 and n / i < m:
			return True

		i -= 1

	return False


m = 1000
n = (m - 1) ** 2

while m >= 100 and n > 100:
	if n == int(str(n)[::-1]):
		if has_factor(n, m):
			break			

	if n < (m - 100) ** 2:
		m -= 100

	n -= 1

print(n)
