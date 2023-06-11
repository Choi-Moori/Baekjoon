import sys
from collections import Counter

n = int(input().rstrip())
stlist = []

for _ in range(n):
    _ , e = map(str, input().split('.'))
    
    stlist.append(e)

stcnt = Counter(stlist)
stlist = list(set(stlist))
stlist.sort()

for i in stlist:
    print(i, stcnt.get(i))

##stcnt = Counter(stlist).most_common()
##stcnt = sorted(stcnt, key = lambda x : x[0])
##
##for i, j in stcnt:
##    print(i, j)
