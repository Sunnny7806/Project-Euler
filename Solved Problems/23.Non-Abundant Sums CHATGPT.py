import time
start_time = time.time()

def divisors(n):
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

def abundant(n):
    return divisors(n) > n

limit = 28123
abundants = [i for i in range(1, limit+1) if abundant(i)]

abundant_sums = set()
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s <= limit:
            abundant_sums.add(s)
        else:
            break

total_sum = sum(range(1, limit+1)) - sum(abundant_sums)

print(sum(abundant_sums))
print(total_sum)

end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.4f} seconds")

