n = int(input())
for i in range(n):
    palavras = input().split()
    resultado = ""
    for palavra in palavras:
        resultado += palavra[0]
    print(resultado)