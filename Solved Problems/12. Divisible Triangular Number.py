import time
start_time = time.time()
def triangle_number(number):
    triangle = (number * (number+1)) // 2
    return int(triangle)

import math
def number_of_divisors(number):
    divisors_number = 0
    sqrt_n = int(math.isqrt(number))
    for i in range(1, sqrt_n + 1):
        if number % i == 0:
            if i * i == number:
                divisors_number += 1
            else:
                divisors_number += 2
    return divisors_number

while True:
    found = False
    for i in range(1,100000000):
        number = triangle_number(i)
        divisors = number_of_divisors(number)
        if divisors >= 500:
            print(f"{i}th triangular number is {number}")
            print(f"Number of divisors: {divisors}")
            found = True
            break
    if found:
        break
            

end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")