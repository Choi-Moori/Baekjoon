import sys
input = sys.stdin.readline

n = int(input().rstrip())
num = list(map(int , input().split()))
m = int(input().rstrip())
res = [0] * (n+1)

for i in range(1, n+1):
    res[i] = res[i-1] + num[i-1]

for _ in range(m):
    i, j = map(int, input().split())

    print(res[j] - res[i-1])
