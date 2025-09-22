with open("10 Difficulty Problems/81.Path Sum Two Ways/0081_matrix.txt", "r") as f:
    lines = f.readlines()

matrix = []
for line in lines:
    row_of_integers = [int(num) for num in line.strip().split(',')]
    matrix.append(row_of_integers)
    
for row in range(0,80):
    for column in range(0,80):
        if row != 0 and column != 0:
            matrix[row][column] += min(matrix[row-1][column],matrix[row][column-1])
        if row == 0:
            if column != 0:
                matrix[row][column] += matrix[row][column-1]
        if column == 0:
            if row != 0:
                matrix[row][column] += matrix[row-1][column] 

print(matrix[79][79])