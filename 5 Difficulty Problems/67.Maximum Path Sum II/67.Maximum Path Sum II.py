with open("5 Difficulty Problems/67.Maximum Path Sum II/67.txt","r") as f:
    all_lines = f.readlines()
    number_list = []
    for i in reversed(all_lines):
        number_list.append(i.split())
    for row in range(0,100):
        for column in range(0,len(number_list[row])-1):
            number_list[row+1][column] = int(number_list[row+1][column]) + max(int(number_list[row][column]),int(number_list[row][column+1]))
print(number_list[99])





