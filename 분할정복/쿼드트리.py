## leng = 배열의 길이
## mat = 배열
def conqu(mat, leng, x, y):
    count = 0
    for i in range(x, x+leng):
        for j in range(y, y+leng):
            if mat[i][j] != mat[x][y]:
                count = 1
                break
        if count == 1:
            break
    if count == 1:
        print("(",end='')
        leng = leng//2
        conqu(mat, leng, x,y)
        conqu(mat, leng, x, y + leng)
        conqu(mat, leng, x+leng, y)
        conqu(mat, leng, x+leng, y+leng)
        print(")",end='')
    elif count == 0:
        print(mat[x][y], end='')
        
from pprint import pprint

n = int(input())
x,y = 0,0

mat = [[0 for i in range(n)] for j in range(n)]

mat = [list(map(int, input())) for _ in range(n)]

conqu(mat, n, x, y)
            

## 쪼개지면 time complexty => n/2 -> 4개이므로 (n/2)^2*4
## n = 64에서 n=1 까지 줄이는 time complexty는 log2n
## => n^2 * log2n

##2차원 누적합을 이용할 시 O(n^2) 으로 줄일 수 있다.


