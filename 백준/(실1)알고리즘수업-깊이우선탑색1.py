import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,v = map(int, input().split())

gra = [[] for _ in range(n+1)]
vis = [0] * (n+1)
count = 1
for _ in range(m):
    a,b = map(int, input().split())
    gra[a] += [b]
    gra[b] += [a]

def dfs(nv):
    global count
    vis[nv] = count
    gra[nv].sort()
    for i in gra[nv]:
        if vis[i] == 0:
            count += 1
            dfs(i)
dfs(v)

for i in range(1, len(vis)):
    print(vis[i])
