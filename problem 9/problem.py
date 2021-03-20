isDone = False
for a in range(10, 401):
	for b in range(10, 401):
		c = (a**2 + b**2)**0.5 
		if c - int(c) == 0 and (a + b + c) == 1000:
			print(int(a * b * c))
			isDone = True

	if isDone:
		break
