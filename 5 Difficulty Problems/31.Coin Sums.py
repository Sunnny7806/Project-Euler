"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
target = int(input("Target: "))
alternative_ways = 0
for a in range(0,target // 200 + 1):                
    for b in range(0, target // 100 + 1):                        
        total = (200 * a) + (100 * b)
        if total > target:
            break
        for c in range(0,target // 50 + 1):                   
            total = (200 * a) + (100 * b) + (50 * c)
            if total > target:
                break
            for d in range(0,target // 20 + 1):               
                total = (200 * a) + (100 * b) + (50 * c) + (20 * d)
                if total > target:
                    break
                for e in range(0, target // 10 + 1):
                    total = (200 * a) + (100 * b) + (50 * c) + (20 * d) + (10 * e)
                    if total > target:
                        break
                    for f in range(0,target // 5 + 1):
                        total = (200 * a) + (100 * b) + (50 * c) + (20 * d) + (10 * e) + (5 * f)
                        if total > target:
                            break 
                        for g in range(0,target // 2 + 1):
                            total = (200 * a) + (100 * b) + (50 * c) + (20 * d) + (10 * e) + (5 * f) + (2 * g)
                            if total > target:
                                break
                            else:
                                alternative_ways += 1

print(alternative_ways)