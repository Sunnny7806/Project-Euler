import time
start_time = time.time()

def collatz(number):
    count = 1
    while number > 1 :
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1    
        count += 1
    return count

max_result  = 0
max_number = 0
for numbers in range(1,1000000):
    result = collatz(numbers)   
    if result > max_result:
        max_result = result
        max_number = numbers
        print(f"{numbers} has {result} chains")
print(f"Max chains: {max_result}")
print(max_number)


end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")