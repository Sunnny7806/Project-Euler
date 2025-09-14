def combinatoric(x,y):
    if x == y:
        return 1
    return x * combinatoric(x-1,y)

def fact(x):
    if x== 1 or x == 0:
        return 1
    return x * fact(x-1)

count = 0
for i in range(1,101):
    for j in range(1,i):
        prod = combinatoric(i,i-j) // fact(j)
        if prod > 1000000:
            count += 1
print(count)