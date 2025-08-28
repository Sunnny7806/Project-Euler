def binary(x):
    if x // 2 < 1:
        return str(1)
    else:
        return str(x % 2) + str(binary(x//2))
    
def palindrome(x):
    x = str(x)
    reverse_x = x[::-1]
    if x == reverse_x:
        return True
    else:
        return False
    
total = 0
for i in range(1,1000000):
     if palindrome(i):
        if palindrome(binary(i)):
            total += i
            print(i)

print("Total: ",total)
    
        