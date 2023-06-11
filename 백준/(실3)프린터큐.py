from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    count = 0
    
    cnt, num = list(map(int, input().split()))
    que = deque(list(map(int, input().split())))
    od = deque(i for i in range(cnt))

    maxq = max(que)

    while que:
        if que[0] == maxq:
            if od[0] == num:
                count += 1
                print(count)
                break
            od.popleft()
            count +=1
            que.popleft()
            maxq = max(que)
        else:
            que.append(que.popleft())
            od.append(od.popleft())
    
