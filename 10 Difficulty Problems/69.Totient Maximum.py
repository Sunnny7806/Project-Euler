def prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x % i:
            return False
    return True

primoral_num = 2
num = 3
while primoral_num < 1000000:
    if prime(num):
        primoral_num *= num
        print(primoral_num)
    num += 2    