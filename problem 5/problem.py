my_list = [i for i in range(2, 21)]


def fn(n):
    if n == 0:
        return False
    for i in my_list:
        if n % i != 0:
            return False
    else:
        return True


i = 0
while True:
    if fn(i):
        print(i)
        break
    i += 2520
