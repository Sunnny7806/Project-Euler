number = "0"
for i in range(1,1000001):
    number += str(i)
    if len(number) > 1000001:
        break
total = int(number[1]) * int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000])
print(total)
