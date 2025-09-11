def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

max_count = 0
product = 0

for a in range(-999, 1000,2):
    for b in range(2, 1001):
        n = 0
        while True:
            val = n * n + a * n + b
            if not is_prime(val):
                break
            n += 1
        if n > max_count:
            max_count = n
            product = a * b

print("Maksimum ardışık asal sayılar:", max_count)
print("a * b =", product)














