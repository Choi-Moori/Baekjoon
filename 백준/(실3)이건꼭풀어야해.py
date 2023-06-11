import sys
input = sys.stdin.readline

n, q = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
res = [0] * (n+1)

for i in range(1, n+1):
    res[i] = res[i-1] + num[i-1]
for _ in range(q):
    L, R = map(int , input().split())

    print(res[R] - res[L-1])
