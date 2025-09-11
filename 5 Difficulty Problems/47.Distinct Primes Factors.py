import time
start_time = time.time()
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
    
def prime_factor(x):
    factor_counter = set()
    while not x % 2:
        x //= 2
        factor_counter.add(2)
    for i in range(3,int(x**0.5)+1,2):
        if prime(i):
            while not x % i:
                x //= i
                factor_counter.add(i)
            if x == 1:
                break
            if prime(x):
                factor_counter.add(x)
                return len(factor_counter)
    return len(factor_counter)    
    
number = 150
while True:
    if prime(number):
        number += 1
    if prime_factor(number) == 4:
        if prime_factor(number+1) == 4:
            if prime_factor(number+2) == 4:
                print(number,number+1,number+2)
                if prime_factor(number+3) == 4:    
                    print(number,number+1,number+2,number+3)
                    break
                else:number+=4
            else:number+=3 
        else:number+=2 
    else:number += 1


    
    

end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")
