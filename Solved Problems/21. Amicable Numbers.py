def divisors(x):
    main_number = x
    second_number = x
    numbers = [1]
    for i in range(2,second_number):
        if main_number % i == 0:
            numbers.append(i)
            second_number = main_number // i
    numbers.sort()
    return sum(numbers)

numbers_amicable = []
for i in range(1,10000):
    a = divisors(i)
    for j in range(1,i):
        if j == a:
            b = divisors(j)
            if b == i:
                numbers_amicable.append(i)
                numbers_amicable.append(j)

print(sum(numbers_amicable))


 





