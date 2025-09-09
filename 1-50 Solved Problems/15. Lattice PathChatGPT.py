import time
start_time = time.time()

grid = int(input("Grid: "))

# Başlangıç satırı [1] * (grid + 1)
paths = [1] * (grid + 1)

# Her satırda güncelleme yap
for i in range(grid):
    for j in range(1, grid + 1):
        paths[j] += paths[j - 1]
    print(paths)



#ChatGPT çözümü


end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")
