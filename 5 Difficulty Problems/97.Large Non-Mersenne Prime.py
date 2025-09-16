count = 1
number = 1
while count <= 7830457:
    number *= 2
    if len(str(number)) > 10:
        number = number%(10**10)
    count += 1
print(str(28433*number + 1)[-10:])
