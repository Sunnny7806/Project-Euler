def binary(x):
    code = ""
    while x // 2 >= 1:
        if x % 2 == 0:
            code += "0"
            x = x // 2
        elif x % 2 == 1:
            code += "1"
            x = x // 2
        if x == 1:
            code += "1"
            break
    return code
print(binary(103564))
    





    
        