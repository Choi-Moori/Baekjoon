import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
hip = []
for _ in range(n):
    num = int(input().rstrip())
    if num == 0:
        if not hip:
            print(0)
        else:
            print(heapq.heappop(hip))
    else:
        heapq.heappush(hip, num)
