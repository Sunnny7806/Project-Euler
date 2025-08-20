def digit_fifth_power(number):
    total = 0
    for i in str(number):
        total += int(i) ** 5
    if total == number:
        return True
    else:
        return False
    
total = 0
for i in range(2,1000000):
    x = digit_fifth_power(i)
    if  x:
        total += i
        print("Numbers: ",i)

print(total)
    