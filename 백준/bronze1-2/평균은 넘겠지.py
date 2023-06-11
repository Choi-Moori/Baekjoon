n = int(input())
num = []
for i in range(n):
    num = list(map(int, input().split()))
    avg = (sum(num[1:])/num[0])
    a = 100/num[0]
    c = 0
    for i in num[1:]:
        if(i > avg):
            c += 1
    print("{0:.3f}%".format(a*c))


