def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        a,b = b,a+b

        yield b
total = 0
for sayı in fibonacci():
    
    if sayı % 2 == 0:
        total += sayı
    if sayı >= 4000000:
        break
    else:
        print(sayı)

print(f"Total: {total}")