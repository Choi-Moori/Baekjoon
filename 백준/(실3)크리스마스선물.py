import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    n = list(map(int, input().split()))

    if n[0] == 0:
        if not heap:
            print(-1)
        else:
            print(heapq.heappop(heap)[1])
    else:
        for i in n[1:]:
           heapq.heappush(heap, [-i, i])
