months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1901
index_day = 2  
total = 0
while year <= 2000:
    if year % 400 == 0:
        months[1] = 29
    elif year % 100 == 0:
        months[1] = 28
    elif year % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28
    for days in months:
        if index_day == 7:
            total += 1
        index_day += days
        index_day %= 7
        if index_day == 0:
            index_day = 7
    year += 1
print("Total:", total)
