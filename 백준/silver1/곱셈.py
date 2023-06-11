a, b, c = map(int, input().split())
tmp = a

def divied(a,b):
    global tmp
    
    if b == 1:
        return a%c
    elif b%2 == 0:
        a = divied(a,b//2)
        return (a * a)%c
    else:
        a = divied(a,b-1)
        return (a*tmp)%c

a = divied(a,b)

print(a)
