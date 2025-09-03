#pentagon = i * (3 * i - 1) // 2
def is_pent(target,a,b):
    for i in range(a,b):
        pentagon = i * (3 * i - 1) // 2
        if target < pentagon:
            return False
        elif target == pentagon:
            return True

min_dif = None
is_found = False
for a in range(1,10000):
    pent_1 = a * (3 * a - 1) // 2
    for b in range(a+1,10000):
        pent_2 = b * (3 * b - 1) // 2
        if is_pent(pent_1 + pent_2,b,10000):
            if is_pent(pent_2 - pent_1,1,b):
                print("Differencce: ",pent_2 - pent_1)
                is_found = True
                break
    if is_found:
        break



                


        
