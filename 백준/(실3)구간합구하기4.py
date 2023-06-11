import sys
input = sys.stdin.readline
n , m = map(int, input().split())
num_list = list(map(int, input().split()))
l_list = [0] * (n+1)

for i in range(1,n+1):
    l_list[i] = l_list[i-1] + num_list[i-1]

for _ in range(m):
    i, j = map(int , input().split())

    print(l_list[j] - l_list[i-1])
    
