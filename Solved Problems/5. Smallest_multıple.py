def ebob(x,y):
    number = min(x,y)
    while number >= 1:
        if x % number == 0 and y % number == 0:
            ebob = number
            return ebob
        number -= 1

def ekok(x,y):
    return x*y // ebob(x,y)

total = 1

for i in range(2,21):
    total = ekok(total,i)

print(total)