n = int(input())
str = []
revstr = []

for i in range(n):
    str.append(input())

for i in range(n):
    for j in range(len(str[i])-1, -1 , -1):
        revstr.append(str[i][j])
        
for i in range(n):
    print(revstr[i])
                      
