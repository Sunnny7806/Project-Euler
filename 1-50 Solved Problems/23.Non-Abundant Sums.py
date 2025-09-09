import time
start_time = time.time()
def divisors(x):
    main_number = x
    second_number = x
    total = 0
    for i in range(2,second_number):
        if main_number % i == 0:
            total += i
            second_number = main_number // i
    return total + 1
def abundant(x):
    if divisors(x) <= x:
        return False
    else:
        return True

list_of_abundant = []
abundant_sum_list = []
number_range = 28123
total_sum = (number_range * (number_range + 1))//2

for i in range(1,number_range+1):
    if abundant(i):
        list_of_abundant.append(i)

for j in list_of_abundant:
    for k in list_of_abundant:
        if j <= k:
            abundant_number_sum = j+k
            if abundant_number_sum < number_range:
                if abundant_sum_list.count(abundant_number_sum) == 0:
                    abundant_sum_list.append(abundant_number_sum)
            else:
                break
        else:
            continue
total_sum -= sum(abundant_sum_list)
            
abundant_sum_list.sort()

print(sum(abundant_sum_list))

print(total_sum)

end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")