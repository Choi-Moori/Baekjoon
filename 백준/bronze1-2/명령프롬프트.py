n = int(input())

str1 = []
str2 = ''
state = 0
if(n==1):
    print(input())
else:
    for i in range(n):
        str1.append(input())

    for i in range(len(str1[0])):
        for j in range(n):
            if(str1[0][i] == str1[j][i]):
                state = 1
            else:
                state = 0
                break
        if(state == 1):
            str2 += str1[1][i]
        else:
            str2 += '?'

    print(str2)
           
