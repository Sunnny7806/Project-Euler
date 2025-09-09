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
    
prime_list = [2]    
for i in range(3,1000000,2):
    if prime(i):
        prime_list.append(i)

max_chain = 0
for a in prime_list:
    total = a
    chain = 1
    for b in prime_list[prime_list.index(a)+1:]:
        total += b
        chain += 1
        if  total > 1000000:
            break
        if prime(total):
            if max_chain < chain:
                max_chain = chain
                print(total,chain)