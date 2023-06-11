import sys
input = sys.stdin.readline

n = int(input().rstrip())
num (= list(map(int, input().split()))

res = -1001
tmp = 0

for i in num:
    
    tmp += i
    if tmp <= 0:
        tmp = i
    if res <= tmp:
        res = tmp
    if tmp <= 0:
        tmp = 0
        
print(res)
