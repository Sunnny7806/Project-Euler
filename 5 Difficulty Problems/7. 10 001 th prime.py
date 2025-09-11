prime_count = 0
number = 1

while prime_count < 10001:
    number += 1
    is_prime = True
    for divider in range(2, int(number ** 0.5) + 1): #Eğer bir sayı asal değilse, mutlaka iki böleni vardır ve en az biri o sayının karekökünden küçük ya da eşittir.
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
        if prime_count == 10001:
            pass
print(f"The 10001st prime number is: {number}")
            

