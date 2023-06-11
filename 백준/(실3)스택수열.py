import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

stack = deque()

for i in range(n):
    num = int(input())
    for j in range(num):
        if not stack:
            stack.append(j+1)
        else:
            
            
    print(stack, num)

