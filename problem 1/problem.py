sum_3 = int((1000 - 1) / 3)
sum_3 = (sum_3 * (1 + sum_3)) / 2

sum_5 = int((1000 - 1) / 5)
sum_5 = (sum_5 * (1 + sum_5)) / 2

sum_15 = int((1000 - 1) / 15)
sum_15 = (sum_15 * (1 + sum_15)) / 2

sum = (sum_3 * 3) + (sum_5 * 5) - (sum_15 * 15)

print(int(sum))
