def prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if not x % i:
            return False
    return True


grid = 3
count_p = 0
number_c = 1
while True:
    b_right = grid ** 2
    b_left = b_right - grid + 1
    t_left = b_left - grid + 1
    t_right = t_left - grid + 1
    number_c += 4
    if prime(b_left):count_p += 1
    if prime(b_right):count_p += 1
    if prime(t_left):count_p += 1
    if prime(t_right):count_p += 1
    ratio = count_p / number_c
    if ratio < 0.1:
        print("Last Grid: ",grid,ratio)
        break
    grid += 2










