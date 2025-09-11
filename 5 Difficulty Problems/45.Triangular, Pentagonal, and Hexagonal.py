#triangular = x(x + 1)//2
#pentagonal = x(3x - 1)//2   3x^2 -x -2y = 0  
#hexagonal = x(2x - 1)  2x^2 -x - y = 0
def pentagonal(x):
    result = (1 + (1 + 24*x)**0.5)/6
    if result == int(result):
        return True
    else:
        return False

def hexagonal(x):
    result = (1 +(1 + 8*x)**0.5)/4
    if result == int(result):
        return True
    else:return False

count = 0
x = 2
while count < 2:
    result = (x*(x + 1))//2
    if pentagonal(result):
        if hexagonal(result):
            print(result)
            count += 1
            x+=1
        else:x+=1
    else:x += 1



