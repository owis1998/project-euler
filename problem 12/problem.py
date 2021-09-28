def fun(x):
	dic = {1:0}
	for i in range(2, int(x / 2)):
		if x % i == 0:
			if i not in dic:
				dic[i] = 0

			if int(x / i) not in dic:
				dic[int(x / i)] = 0

			else:
				return len(dic)
	else:
		return 1
n = 50

while True:
	Sum = int( (n**2 + n) / 2 )

	temp = fun(Sum)
	# print(n, Sum, temp)
	if temp > 500:
		print(Sum)
		break

	n +=1
