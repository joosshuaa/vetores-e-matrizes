cyberpunk = int(input())
while cyberpunk > 0:
    cyberpunk -= 1
    black = input().split()
    black.sort(key = len, reverse = True)
    for i in range(len(black)):
        print(black[i], end = '')
        if i != len(black)-1:
            print(' ', end = '')
    print()