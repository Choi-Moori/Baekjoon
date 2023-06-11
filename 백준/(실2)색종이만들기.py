import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input().rstrip())

mat = [list(map(int, input().split())) for _ in range(n)]
x,y = 0, 0
bcnt = wcnt = 0


def conqu(mat,x,y , leng):
    global bcnt, wcnt
    end = 0
    count = 0
    for i in range(x, x + leng):
        for j in range(y, y +leng):
            if  mat[i][j] != mat[x][y]:
                end = 1
                break
        if end:
            count = 0
            break
    if end:
        leng = leng//2
        conqu(mat, x,y, leng)
        conqu(mat, x, y+leng, leng)
        conqu(mat, x+leng, y, leng)
        conqu(mat, x+leng, y+leng, leng)
    else:
        if mat[x][y]:
            bcnt += 1
        else:
            wcnt += 1
conqu(mat,x,y, n)
print(wcnt)
print(bcnt)
