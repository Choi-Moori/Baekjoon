import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
res = []

res.append(sum(num[:m]))

for i in range(n-m):
    res.append(res[i] - num[i] + num[m+i])

print(max(res))
