import sys
from collections import Counter
n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
##cm = [0] * m
##nl.sort()
##
##low = 0
##high = len(nl)-1
##        
##
##for i in range(len(ml)):
##    while ml[i] in nl:
##        mid = (low+high)//2
##
##        if nl[mid] == ml[i]:
##            low = 0
##            high = len(nl)-1
##            cm[i] += 1
##            del nl[mid]
##        elif nl[mid] > ml[i]:
##            high = mid - 1
##        else:
##            low = mid + 1
##            
##    print(cm[i],'',end='')

count = Counter(nl)

for i in range(len(ml)):
    if ml[i] in count:
        print(count[ml[i]],'', end='')
    else:
        print(0,'' , end='')
