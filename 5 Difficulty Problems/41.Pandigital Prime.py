def pandigital(x):
    if "0" in str(x):
        return False
    for i in str(x):
        if int(i) > len(str(x)):
            return False
    if len(set(str(x))) == len(str(x)):
        return True
    return False
            
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
    
max_pandigital_prime = 0
for i in range(1,987654322,2):
    if pandigital(i):
        if prime(i): 
            print(i)

# Program sonlanmıyor  ama sonucu veren sayıdan sonra çıktı alınamıyor.
