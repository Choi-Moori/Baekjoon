import sys
import re
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    end, rev = 1, True
    
    s = list(map(str, input().rstrip()))
    n = int(input().rstrip())
    num = input()
    deq= deque(re.findall(r'\d+', num))
    
    for i in s:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if deq:
                if rev:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                end = 0
                break
    if not rev:
        deq.reverse()
    if end == 0:
        print("error")
    else:
        print('[' + ','.join(deq) + ']')
