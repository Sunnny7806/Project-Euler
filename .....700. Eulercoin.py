def eulercoin(x):
    return (1504170715041707 * x) % 4503599627370517

number = 2
total = 0
min_number = eulercoin(1)
max_number = eulercoin(4503599627370517) 
while True:
    x = eulercoin(number)
    y = eulercoin(4503599627370517-number)
    if x < min_number:
        min_number = x
        total += min_number
        print("Min Number: {}\tNumber: {}\tTotal: {}".format(min_number,number,total))
    if x == 0:
        break
    number += 1 



