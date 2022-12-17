nations = int(input())
while(nations > 0):
    nations -= 1
    budapeste = input()
    newcity = int(len(budapeste)/2) -1
    veneza = budapeste[newcity::-1] + budapeste[len(budapeste)-1:newcity:-1]
    print(veneza)