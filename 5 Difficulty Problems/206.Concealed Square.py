
def is_target(x):
    x **= 2
    if x % (10**5) < 80900 or x % (10**5) >= 90000:
        return False
    if x % (10**7) < 7080900 or x % (10**7) >= 8000000:
        return False
    if x % (10**9) < 607080900 or x % (10**9) >= 700000000:
        return False
    if x % (10**11) < 50607080900 or x % (10**11) >= 60000000000:
        return False
    if x % (10**13) < 4050607080900 or x % (10**13) >= 5000000000000:
        return False
    if x % (10**15) < 304050607080900 or x % (10**15) >= 400000000000000:
        return False
    if x % (10**17) < 20304050607080900 or x % (10**17) >= 30000000000000000:
        return False
    return True

number = 10**9 + 30 
while True:
    if number % 100 == 30 or number % 100 == 70:
        if is_target(number):
            print("FOUND: ",number)
            break
        number += 40
        continue
    number += 20