def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x-1)

main_total = 0
for i in range(3,1000000):
    total = 0
    for j in str(i):
        j = int(j)
        total += factorial(int(j))
    if total == i:
        main_total += total

print(main_total)

