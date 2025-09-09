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
    
def truncatable(x):
    if int(x) < 10:
        return False
    digit = []
    if prime(x):
        for i in str(x):
            digit.append(i)
        while len(digit) > 0:
            digit.pop(0)
            if len(digit) == 0:
                return True
            new_number = ""
            for j in digit:
                new_number += str(j)
            if not prime(new_number):
                return False

def reverse_truncatable(x): 
    if int(x) < 10:
        return False
    digit = []
    if prime(x):
        for i in str(x):
            digit.append(i)
        while len(digit) > 0:
            digit.pop()
            if len(digit) == 0:
                return True
            new_number = ""
            for j in digit:
                new_number += str(j)
            if not prime(new_number):
                return False
            
counter = 0
number = 8
total = 0
while counter != 11:  
    if truncatable(number):
        if reverse_truncatable(number):
            print(number)
            counter += 1
            total += number
    number += 1
print("Total: ",total)