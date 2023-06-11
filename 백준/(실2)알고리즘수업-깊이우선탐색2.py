import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())

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
    gra[nv].sort(reverse=True)
    for i in gra[nv]:
        if vis[i] == 0:
            count += 1
            dfs(i)

dfs(r)

for i in range(1, n+1):
    print(vis[i])
