units = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:""}
just_tens = {0:"ten", 1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}
ten_digits = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety", 0:""}
hundreds =  { 1:"onehundred", 2:"twohundred", 3:"threehundred", 4:"fourhundred", 5:"fivehundred", 6:"sixhundred", 7:"sevenhundred", 8:"eighthundred", 9:"ninehundred"}

x = 0
numbers_2_digits = []
numbers_3_digits = []
for number in range(1,1000):
    number = str(number)
    if len(number) == 1:
        letter_form1 = len(units.get(int(number)))
        x += letter_form1

    elif len(number) == 2:
        for figures in number:
            numbers_2_digits.append(figures)  # Figures append to list as string
        if numbers_2_digits[0] == "1":
            letter_form2 = len(just_tens.get(int(numbers_2_digits[1])))
            x += letter_form2
            numbers_2_digits.clear()
        else:
            letter_form3 = len(ten_digits.get(int(numbers_2_digits[0])))
            letter_form4 = len(units.get(int(numbers_2_digits[1])))
            numbers_2_digits.clear()
            x += letter_form3 + letter_form4

    elif len(number) == 3:
        for figures in number:
            numbers_3_digits.append(figures)
        letter_form5 = len(hundreds.get(int(numbers_3_digits[0])))
        x += letter_form5
        if numbers_3_digits[1] == "1":
            letter_form6 = len(just_tens.get(int(numbers_3_digits[2])))
            x += letter_form6
        else:
            letter_form7 = len(ten_digits.get(int(numbers_3_digits[1])))
            x += letter_form7
            letter_form8 = len(units.get(int(numbers_3_digits[2])))
            x += letter_form8
        if int(number[1:]) != 0:
            x += 3
        numbers_3_digits.clear()
        
print(x + len("onethousand"))




