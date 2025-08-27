def non_repeat(x,y):
    for i in range(x,y):
        digit_set = set()
        for j in str(i):
            if j == "0":
                break
            digit_set.add(j)
        if len(digit_set) == len(str(i)):
            yield i

def compare_non_repeat(x,y):
    for i in str(x):
        for j in str(y):
            if j == i:
                return False
    return True
    
list_of_product = []        
total = 0
for a in non_repeat(2,100):
    for b in non_repeat(100,5000):
        if compare_non_repeat(a,b):
            product = a * b
            digit = set()
            for i in str(product):
                if i == "0":
                    break
                digit.add(i) 
            if len(digit) == len(str(product)):
                if compare_non_repeat(product,a):
                    if compare_non_repeat(product,b):
                        if len(str(product)) + len(str(a)) + len(str(b)) == 9:
                            if product in list_of_product:
                                pass
                            else:
                                list_of_product.append(product)
                                print(f"Multiplicant: {a}\nMultiplier: {b}\nProduct: {product}\n")
                                total += product
                                print("Total:",total)