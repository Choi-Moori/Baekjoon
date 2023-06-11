import sys
import heapq
input = sys.stdin.readline

T = int(input().rstrip())


for _ in range(T):
    n = int(input().rstrip())
    count = 0
    maheap = []
    miheap = []
    maheaptmp = []
    miheaptmp = []
    for _ in range(n):
        s, num = input().split()
        num = int(num)
        if s == 'I':
            heapq.heappush(maheap, (-num, num))
            heapq.heappush(miheap, (num))
            count += 1
        else:
            if num == -1 and count != 0:
                heapq.heappop(miheap)
                for _ in range(len(maheap)-1):
                    ls = heapq.heappop(maheap)[1]
                    heapq.heappush(maheaptmp, ls)
                heapq.heappop(maheap)[1]
                while maheaptmp:
                    ls = heapq.heappop(maheaptmp)
                    heapq.heappush(maheap, (-ls, ls))
                count -= 1
            elif num == 1 and count != 0:
                heapq.heappop(maheap)
                for _ in range(len(miheap)-1):
                    ls = heapq.heappop(miheap)
                    heapq.heappush(miheaptmp, ls)
                heapq.heappop(miheap)
                while miheaptmp:
                    ls = heapq.heappop(miheaptmp)
                    heapq.heappush(miheap, ls)
                count -= 1
                    
    if count:
        print(heapq.heappop(maheap)[1], heapq.heappop(miheap))
    else:
        print("EMPTY")
