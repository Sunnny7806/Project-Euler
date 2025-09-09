grid = 1001
double_numbers = []
total = 1
for i in range(3,grid+1,2):
    double_numbers.append(i**2)

first_boost = 6
second_boost = 20

for j in double_numbers:
    total += j + (j+ first_boost)
    first_boost += second_boost
    second_boost += 16

print(total)