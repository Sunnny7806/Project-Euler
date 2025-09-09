def prime(x):
    if int(x) < 2:
        return False
    is_prime = True
    for i in range(2, int((int(x) ** 0.5) + 1)):
        if int(x) % i == 0:
            is_prime = False
            break
    if is_prime:
        return True
    else:
        return False 
    
number = 9
while True:
    found = False
    if not prime(number):
        for i in reversed(range(1,number,2)):
            if prime(i):
                result = ((number - i)//2)**0.5
                if result == int(result):
                    break
                elif i == 3:
                    found = True
                    print(number)
                    break

    number += 2
    if found:break