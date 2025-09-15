x_number = 1
y_number = 1
count = 0
while True:
    product = y_number ** x_number
    lenght = len(str(product))
    if lenght == x_number:
        count += 1
        print(f"{y_number}^{x_number}     Count: {count}")
        y_number += 1  
    elif lenght >= x_number:
        x_number += 1
        y_number = 1
        continue
    else:
        y_number += 1
    if len(str(9**x_number)) < x_number:
        break