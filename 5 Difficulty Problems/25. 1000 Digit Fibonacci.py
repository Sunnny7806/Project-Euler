def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        a,b = b,a+b

        yield b

count = 0
for number in fibonacci():
    if len(str(number)) >= 1000:
        count += 1
        print(f"Found: {number}")
        print(f"Count: {count}")
        break
    else:
        print(number)
        count += 1

