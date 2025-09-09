def sum_of_squre(x):
    total_sum = 0
    for i in range(1,x+1):
        total_sum += i ** 2
    return total_sum

def square_of_sum(y):
    total_squre = 0
    a = 0
    for i in range(1,y+1):
        total_squre += i
    return total_squre ** 2

print(square_of_sum(100)-sum_of_squre(100))