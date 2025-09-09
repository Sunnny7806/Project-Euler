def pisagor_triangle(x,y,z):
    if abs(y - z) < x < (y + z):
        if pow(x,2) == pow(y,2) + pow(z,2):
            return True
    return False

max_posibility = 0
for perimeter in range(10,1000):
    posibility = 0
    for a in range(2,perimeter):
        for b in range(1,a):
            if (a + b) >= perimeter:
                break
            c = perimeter - (a + b)
            if a > b > c:
                if pisagor_triangle(a,b,c):
                    posibility += 1
    if posibility > max_posibility:
        max_posibility = posibility
        print(perimeter)
        print("Max Posiblity: ",max_posibility)







