import sys
input = sys.stdin.readline

n, q = map(int, input().split())
num = []
res = []

for _ in range(n):
    num.append(int(input().rstrip()))

for _ in range(q):
    a,b = map(int, input().split())
    res = num[a:b]
    print(res)
    
print(n,q)
print(res)
