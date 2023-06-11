import sys
from collections import Counter
input = sys.stdin.readline

n,x = map(int, input().split())
num = list(map(int , input().split()))
res = []
a = 0
res.append(sum(num[:x]))

for i in range(n-x):
    res.append(res[i] - num[i] + num[x+i])


## 밑에꺼가 빠르고 메모리 더 적게 잡아먹음 
##b = Counter(res).most_common()
##b.sort(key = lambda x : x[0], reverse=True)
##if b[0][0] == 0:
##    print("SAD")
##else:
##    print(b[0][0])
##    print(b[0][1])

a = max(res)
b = Counter(res)

if a == 0:
    print("SAD")
else:
    print(a)
    print(b[a])
