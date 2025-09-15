def number_square(x):
    x = str(x)
    total = 0
    for i in x:
        total += int(i)**2
    if total == 1:
        return False
    elif total == 89:
        return True
    else:
        return number_square(total)

count = 0
for i in range(1,10000000):
    if number_square(i):
        count += 1

print("Count: ",count)