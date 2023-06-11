t = int(input())

for i in range(t):
    a = input()
    p = 0
    count = 0
    for i in range(len(a)):
        if a[i] == 'O':
            count += 1
            p += count
        else:
            count = 0
    print(p)
        
