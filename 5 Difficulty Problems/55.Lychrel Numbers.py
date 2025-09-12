def palindrome(x):
    x = str(x)
    reverse_x = x[::-1]
    if x == reverse_x:
        return True
    else:
        return False
    
number = 195
count = 0
while number < 10000:
    test_number = number 
    test_count = 0
    while test_count <= 50:
        test_number += int(str(test_number)[::-1])
        test_count += 1
        if palindrome(test_number):
            break
        if  test_count == 51:
            if not palindrome(test_number):
                count += 1         
    number += 1   
    
print(f"There are {count} Lychrel Numbers below 10000")      



