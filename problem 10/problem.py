def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


total = 2
for i in range(3, int(2e6), 2):
    if is_prime(i):
        total += i

print(total)
