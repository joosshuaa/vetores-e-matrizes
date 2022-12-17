N = int(input())
M = int(input())
figurines = [0] * N
while M:
    M -= 1
    figurines[int(input()) - 1] = 1

lack = figurines.count(0)
print(lack)