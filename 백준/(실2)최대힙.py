import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
heap = []

for _ in range(n):
    num = int(input().rstrip())

    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-num, num))
