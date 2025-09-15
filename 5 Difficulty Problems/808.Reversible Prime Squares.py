def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

def reverse(x):
    x = str(x)
    return int(x[::-1])

def prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x % i:
            return False
    return True

number = 3
count = 0
total = 0
while count<50:
    if prime(number):
        prod = number ** 2
        if not palindrome(prod):
            rev_num = reverse(prod) ** 0.5
            if rev_num == int(rev_num):
                if prime(rev_num):
                    total += prod
                    count += 1
                    print(prod,total,count)
    number += 2

#yavaş çalışıyor