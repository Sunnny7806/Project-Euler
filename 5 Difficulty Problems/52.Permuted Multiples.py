number = 1
while True:
    digits = set()
    is_found = False
    for i in str(number):
        digits.add(i)
    length = len(digits)
    for a in str(number*2):
        digits.add(a)
    if length == len(digits):
        for b in str(number*3):
            digits.add(b)
        if length == len(digits):
            for c in str(number*4):
                digits.add(c)
            if length == len(digits):
                for d in str(number*5):
                    digits.add(d)
                if length == len(digits):
                    for e in str(number*6):
                        digits.add(e)
                    if length == len(digits):
                        print(number)
                        is_found = True
    if is_found:
        break
    number += 1