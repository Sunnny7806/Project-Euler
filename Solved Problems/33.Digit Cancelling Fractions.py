def compare_repeat(x,y):
    for i in str(x):
        for j in str(y):
            if j == i:
                if j == 0:
                    return False
                return True
    return False

def repeat_number(x,y):
    for i in str(x):
        for j in str(y):
            if j == i:
                return j

def delete_digit(x,y):
    a = list(str(x))
    a.pop(a.index(y))
    return int(a[0])

total = 1
for a in range(10,99):
    for b in range(a+1,100):
        if compare_repeat(a,b):
            common_number = repeat_number(a,b)
            product = a / b
            if int(common_number) == 0:
                continue
            if delete_digit(b,common_number) == 0:
                continue
            second_product = delete_digit(a,common_number) / delete_digit(b,common_number)
            if product == second_product:
                print(f"{a} / {b} = {product}")
                total *= product * 10
print(total)


