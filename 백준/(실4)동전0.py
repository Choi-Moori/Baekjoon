import sys
input= sys.stdin.readline
n, k = list(map(int, input().split()))
nlist = [int(input().rstrip()) for _ in range(n)]


nlist.sort(reverse=True)
count = 0

for i in nlist:
    while i <= k:
        kc = k // i
        k %= i
        count += kc

print(count)
