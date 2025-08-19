found = False
for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2:
                print(f"{a}  {b}  {c}")
                if a + b + c == 1000:
                    found = True
                    print("FOUND")
                    print(f"{a} * {b} * {c} = {a*b*c}")

    if found == True:
        break


