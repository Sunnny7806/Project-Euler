prime_numbers = [2]
for sayı in range(3,60000):
    i = 2
    if sayı > i:
        if sayı % i == 0:
            i += 1
        while sayı % i != 0:
            i += 1
            if sayı == i:
                prime_numbers.append(i)
                print(i)
        
                

x = int(input("Enter a number: "))
x_prime_number = []
for i in prime_numbers:
    if x % i == 0:
        x_prime_number.append(i)
        x = x / i

print(x_prime_number)