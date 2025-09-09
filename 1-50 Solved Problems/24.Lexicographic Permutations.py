figures_list = [0,1,2,3,4,5,6,7,8,9]

def factorial(x):
    for i in range(1,x):
        x *= i
    return x
def stage(x):
    return factorial(lenght_of_list-x)

lenght_of_list = 10
target = 1000000
number_of_stage = 1
counter = 0
index = 0
output = ""

while number_of_stage < lenght_of_list:
    counter += stage(number_of_stage)
    if counter < target:
        index += 1
    elif counter >= target:
        counter -= stage(number_of_stage)
        output += str(figures_list[index])
        figures_list.remove(figures_list[index])
        if len(figures_list) == 1:
            output += str(figures_list[0])        
        number_of_stage += 1
        index = 0
    if len(output) > lenght_of_list:
        break
print("Last Output: {}".format(output))