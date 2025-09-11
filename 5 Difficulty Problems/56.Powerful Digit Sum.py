a = 2
max_res = 0
max_pro = 0
while a < 100:
    for b in range(1,100):
        total = 0
        product = a**b
        for i in str(product):
            total += int(i)
        if max_res < total:
            max_res = total
            max_pro = product
    a += 1
print(f"Max Digit Sum: {max_res}\nThe Product: {max_pro}")
