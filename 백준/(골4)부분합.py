import sys
input = sys.stdin.readline

n,s = map(int, input().split())
num = list(map(int, input().split()))
start, end = 0,0
ans = 0
res = 100000
er = False
num.append(0)
while end <= len(num)-1:
    if ans >= s:
        ans -= num[start]
        start += 1
        res = min(res, (end-start) + 1)
        er = True
    elif ans < s:
        ans += num[end]
        end += 1

if er:
    print(res)
else:
    print(0)
