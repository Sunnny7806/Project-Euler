def pandigital(x):
    set_digit = set(str(x))
    if "0" not in set_digit and len(set_digit) == 9 and len(str(x)) == 9:
        return True
    return False

number = 1
max_number = 1
while len(str(number)) < 5:
    product = ""
    for i in range(1,10):
        product += str(number * i)
        if len(product) == 9:
            if pandigital(int(product)):
                if int(product) >= int(max_number):
                    max_number = product
                    print(max_number)
                    print("Number: ",number)
                    number += 1
                    break
        elif len(product) > 9:
            number += 1
            break

             


