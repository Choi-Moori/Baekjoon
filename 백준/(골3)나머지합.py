import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))

res = [0] * (m)
res[0] = 1
total, count = 0, 0

for i in range(n):
    total = (total+num[i])%m
    res[total] += 1
    
for i in res:
    count += i*(i-1)//2

print(count)
