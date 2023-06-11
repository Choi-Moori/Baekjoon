import sys
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i == 0:
        for j in range(1, n):
            mat[i][j] += mat[i][j-1]
            mat[j][i] += mat[j-1][i]
    else:
        for j in range(1,n):
            mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

for _ in range(m):
    x1,y1, x2,y2 = map(int, input().split())
    x1,y1, x2,y2 = x1-1, y1-1, x2-1,y2-1
    res = 0
    if x1 == 0 and y1 == 0:
        res = mat[x2][y2]
    elif x1 == 0:
        res = mat[x2][y2] - mat[x2][y1-1]
    elif y1 == 0:
        res = mat[x2][y2] - mat[x1-1][y2]
    else:
        res = mat[x2][y2] - mat[x2][y1-1] - mat[x1-1][y2] + mat[x1-1][y1-1]
    print(res)
    
