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
    
prime_numbers = []
for i in range(1001,10000,2):
    if prime(i):
        prime_numbers.append(i)
        for j in prime_numbers[:prime_numbers.index(i)]:
            if set(str(i)) == set(str(j)):
                for g in prime_numbers[:prime_numbers.index(j)]:
                    if set(str(g)) == set(str(j)):
                        if i - j == j - g:
                            print(g,j,i)
                

        
