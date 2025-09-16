exp = 1
a = 3
b = 2
count = 0
while exp <= 1000:
    a,b = 2*b + a,a+b
    if len(str(a)) > len(str(b)):
        count += 1
    exp += 1
print(count)