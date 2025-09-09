def slope(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return y / x

def right_angle(x,y,z):
    if x * y == -1 or x * z == -1 or y * z == -1:
        return True
    if x == y != z or y == z != x or x == z != y:
        return True
    return False

grid = 50
total = 0
for x1 in range(0,grid+1):
    for y1 in range(0,grid+1):
        if x1 == y1 and x1 == 0:
            continue
        for x2 in range(0,grid+1):
            for y2 in range(0,grid+1):
                if x2 == y2 and x2 == 0:
                    continue
                slope_1 = slope(x1,y1)
                slope_2 = slope(x2,y2)
                slope_3 = slope((x1 - x2),(y1 - y2))
                if slope_1 == slope_2 and slope_1 != 0:
                    continue
                if right_angle(slope_1,slope_2,slope_3):
                    total += 1

print(total//2)