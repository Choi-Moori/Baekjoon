word = list(map(str, input().lower()))

word1 = set(word)
c = 0
d = 0
max = 0
a = ''
for i in word1:
    for j in word:
        if i == j:
            c += 1
            if c > max:
                max = c
                a = i
                d = 0
            elif c == max:
                d = 1
    c = 0    
            

if d==1:
    print("?")
else:
    print(a.upper())
