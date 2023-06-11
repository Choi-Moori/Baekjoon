import sys
input = sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())

total = 0
res = 10001

for i in range(m, n+1):
    check = False

    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                check = True

        if not check:
            total += i
            res = min(res, i)

if total:
    print(total)
    print(res)
else:
    print(-1)
