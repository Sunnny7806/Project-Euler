current_number = 1
total = 0
while current_number < 1000:
    if current_number % 3 == 0:
        total += current_number
    elif current_number % 5 == 0:
        total += current_number
    
    current_number += 1
print(total)
