from collections import deque
import sys


## 실패(시간초과)
##n, k = list(map(int ,input().split()))
##
##que = deque()
##reque = deque()
##for i in range(1, n+1):
##    que.append(i)
##
##count = 0
##while len(que) != len(reque):
##    if que[0] != 0:
##        count += 1
##    if count == k:
##        reque.append(que.popleft())
##        que.append(0)
##        count = 0
##    else:
##        a = que.popleft()
##        que.append(a)
##
##res = []
##
##for i in reque:
##    res.append(str(i))
##
##
##print('<' + ', '.join(res) + '>')

n,k = map(int, input().split())

result= []

que = [i + 1 for i in range(n)]
idx = 0

while que:
    idx += k - 1
    if idx >= len(que):
        idx %= len(que)
    print(idx, que, result)
    result.append(str(que.pop(idx)))

print('<' + ', '.join(result)[:] + '>')
