import sys
from collections import deque

input = sys.stdin.readline
T = int(input().rstrip())


end = 0

for _ in range(T):
    s = input().rstrip()
    sta = deque()
    stmp = deque()
    for i in s:
        if i == '-':
            if sta:
                sta.pop()
        elif i == '<':
            if sta:
                stmp.append(sta.pop())
        elif i == '>':
            if stmp:
                sta.append(stmp.pop())
        
        else:
            sta.append(i)
    while stmp:
        sta.append(stmp.pop())
    print(''.join(sta))
