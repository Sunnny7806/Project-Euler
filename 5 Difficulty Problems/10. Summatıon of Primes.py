number = 1
total = 0
for i in range(2,2000000):
    number += 1
    is_prime = True
    for divider in range(2, int(number**0.5)+1):
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        total += number
        
print(f"Total: {total}")


