import sys
from collections import Counter

input = sys.stdin.readline
n = int(input().rstrip())
num_list = [int(input().rstrip()) for _ in range(n)]

num_list.sort()
cnt = Counter(num_list)
cntb = cnt.most_common()

print(round(sum(num_list)/n))
print(num_list[n//2])

if n > 1:
    if cntb[0][1] == cntb[1][1]:
        print(cntb[1][0])
    else:
        print(cntb[0][0])
else:
    print(num_list[0])

print(max(num_list) - min(num_list))
