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

def factoriel(x):
    if x == 1 or x == 0:
        return 1
    return x * factoriel(x-1)

codes = []
count_prime = 2   #2 and 5
for i in range(3,1000,2):
    is_double = False
    for j in str(i):
        if int(j) % 2 == 0 or int(j) % 5 == 0:
            is_double = True
            break
    if is_double:
        continue
    if prime(i):
        i = str(i)      
        a_1 = i.count("1")
        b_3 = i.count("3")
        c_7 = i.count("7")
        d_9 = i.count("9")
        tekrarlı_permütasyon_of_i = factoriel(a_1+b_3+c_7+d_9)// (factoriel(a_1) * factoriel(b_3) * factoriel(c_7) * factoriel(d_9)) 
        code_of_i = str(a_1) + str(b_3) + str(c_7) + str(d_9)
        codes.append(code_of_i)
        if codes.count(code_of_i) == tekrarlı_permütasyon_of_i:
            count_prime += tekrarlı_permütasyon_of_i
            print(i)
print("Total: ",count_prime)