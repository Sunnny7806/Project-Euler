def prime(x):
    is_prime = True
    for i in range(2, int((x ** 0.5) + 1)):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        return True
    else:
        return False         
        
count_prime = 2   #2 and 5
for i in range(3,1000000,2):
    is_double = False
    for j in str(i):
        if int(j) % 2 == 0 or int(j) % 5 == 0:
            is_double = True
            break
    if is_double:
        continue
    if prime(i):
        i = str(i)
        circular = True
        if len(i) > 1:
            digit = []
            for k in i:
                digit.append(k)
            for l in range(len(i)-1):
                digit.append(digit[0])
                digit.pop(0)
                number = ""
                for m in digit:
                    number += m
                if not prime(int(number)):
                    circular = False
                    break            
            if circular:
                count_prime += 1
                print(i)   
        else:
            count_prime += 1
            print(i)

print("Total: ",count_prime)