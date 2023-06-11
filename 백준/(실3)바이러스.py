import sys
input = sys.stdin.readline
n = int(input().rstrip())
v = int(input().rstrip())

gra = [[] for _ in range(n+1)]
vis = [0] * (n+1)
count = 0
for _ in range(v):
    a, b = map(int, input().split())
    gra[a] += [b]
    gra[b] += [a]
def dfs(v):
    global count
    vis[v] = 1
    for i in gra[v]:
        if vis[i] == 0:
            dfs(i)
            count += 1
dfs(1)
print(count)
