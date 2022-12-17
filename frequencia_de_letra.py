testes = int(input())
for teste in range(testes):
    words = input().lower()
    char = {}
    for c in words:
        if c.isalpha() and c not in char:
            char[c] = words.count(c)
    char_ordered = sorted(char.items(), key = lambda x: (-x[1],x[0]))
    larger = char_ordered[0][1]
    result = ''
    for c in char_ordered:
        if c[1] == larger:
            result += c[0]
        else:
            break
    print(result)