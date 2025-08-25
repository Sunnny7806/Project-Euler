
target = int(input("Target: "))

coins = [200, 100, 50, 20, 10, 5, 2, 1]  # 1 TL de eklendi
ways = [0] * (target + 1)
ways[0] = 1  # 0’a ulaşmanın 1 yolu vardır

for coin in coins:
    for value in range(coin, target + 1):
        ways[value] += ways[value - coin]

print(ways[target])
