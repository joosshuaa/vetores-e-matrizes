quantity = int(input())
for i in range(quantity):
    words = input()
    quantity = int(input())
    jupyter = ''
    for l in words:
        position = ord(l)-quantity
        if(position < 65):
            jupyter += chr(91-(65-position))
        else:
            jupyter += chr(ord(l)-quantity)
    print(jupyter)