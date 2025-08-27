def factoriel(x):
    if x == 1 or x == 0:
        return 1
    return x * factoriel(x-1)

print(factoriel(3)//(factoriel(1)*factoriel(0)*factoriel(0)*factoriel(2)))
