import sys
from collections import Counter
input = sys.stdin.readline
n , m = list(map(int,input().split()))

nlist = [input().rstrip() for _ in range(n)]
mlist = [input().rstrip() for _ in range(m)]

nlist.sort()
mlist.sort()

result = Counter(nlist) & Counter(mlist)

count = 0
for i in result:
    count += 1

print(count)
for i in result:
    print(i)
