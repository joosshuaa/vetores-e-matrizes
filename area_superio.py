m = []
t = input()
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
a = 0
inferior = 1
superior = 11
jupyter = 0
for i in range(0,5):
    for j in range(inferior,superior):
        a += m[i][j]
        jupyter += 1
    inferior += 1
    superior -= 1
media = a / jupyter
if t == "S":
    print('{:.1f}'.format(a))
else:
    print('{:.1f}'.format(media))