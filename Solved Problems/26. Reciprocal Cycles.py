def period_lenght(x):
    div_check = x
    while not div_check % 2:
        div_check //= 2
        if div_check == 1:
            return 0
    while not div_check % 5:
        div_check //= 5
        if div_check == 1:
            return 0
    rem = set()
    first_rem = 1 % x
    rem.add(first_rem)
    remainder = (first_rem*10)%x
    rem.add(remainder)
    n = 0
    while n != len(rem):
        remainder = (remainder*10)%x 
        rem.add(remainder)
        n += 1
    return n   

max_result = 0 
max_number = None
for i in range(2,1000):
    result = period_lenght(i)
    if result >  max_result:
        max_result = result
        max_number = i
print(max_number,max_result)