number = 4
total = 0
while number < (10**17)**0.5:
    product = number ** 2
    lenght = len(str(product))
    str_product = str(product)
    if lenght == 17:
        break
    if not lenght % 2:
        a = product // 10 ** (lenght//2)
        b = product % 10 ** (lenght//2)
        if len(str(b)) == lenght // 2:
            if product == (a+b)**2:
                total += product
                print(product)
    else:
        for x in range(lenght//2, lenght//2 + 2):
            a = str_product[:x]
            b = str_product[x:]
            if b[0] != "0":
                if product == (int(a) + int(b)) ** 2:
                    print(product)
                    total += product
                    break
    number += 1 
print("Total: ",total)

#slow