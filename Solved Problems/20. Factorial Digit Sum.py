def factorial(x):
    a = 1
    for i in range(1,x+1):
        a *= i
    return a

def digit_Sum(x):
    x = str(x)
    a = 0
    for i in x:
        a += int(i)
    return a

print(digit_Sum(factorial(100)))