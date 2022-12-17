vet = []
l = input()
for i in range(12):
    vet.append([])
    for j in range(12):
        x = float(input())
        vet[i].append(x)
xj6 = 0
terminal = 0
jupyter = 11
for i in range(1,11):
    for j in range(jupyter,12):
        xj6 += vet[i][j]
        terminal += 1
    if i < 5:
        jupyter -= 1
    if i > 5:
        jupyter += 1
media = xj6 / terminal
if l == "S":
    print('{:.1f}'.format(xj6))
else:
    print('{:.1f}'.format(media))