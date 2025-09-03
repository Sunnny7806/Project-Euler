def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return

        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()

    backtrack()
    return ans

# Kodu kullanma:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
permutations = permute(nums)
total = 0
for i in permutations:
    if i[5] == 5:
        if i[0] != 0:
            if i[3] % 2 == 0:
                if int(str(i[2]) + str(i[3]) + str(i[4])) % 3 == 0:
                    if int(str(i[4]) + str(i[5]) + str(i[6])) % 7 == 0:
                        if int(str(i[5]) + str(i[6]) + str(i[7])) % 11 == 0:
                            if int(str(i[6]) + str(i[7]) + str(i[8])) % 13 == 0:
                                if int(str(i[7]) + str(i[8]) + str(i[9])) % 17 == 0:
                                    number = ""
                                    for j in i:
                                        number += str(j)
                                    total += int(number)

print(total)
