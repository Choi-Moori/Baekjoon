import sys
input = sys.stdin.readline
t = int(input().rstrip())

n = [0]*101
n[0] = n[1] = n[2] = 1

for i in range(3, 100):    
    n[i] = n[i-2] + n[i-3]
    
for _ in range(t):
    num = int(input().rstrip())
    print(n[num-1])
