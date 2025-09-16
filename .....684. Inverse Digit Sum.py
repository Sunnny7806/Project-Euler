def func_s(x):
    nine_count = x // 9
    number = str(x - 9*nine_count) + "9" * nine_count
    return int(number)

def fibonacci(x):
    if x == 2:
        return 1
    count = 2
    a = 1
    b = 1
    while count < x:
        a , b = b , a+b
        count += 1
        if count == x:
            return b

total = 0
for i in range(2,11):
    for n in range(1,fibonacci(i)+1):
        total += func_s(n)
print(total)