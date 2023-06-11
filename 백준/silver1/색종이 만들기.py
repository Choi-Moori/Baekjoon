def divide(x,y,mat,n):
    state = -1
    global count0
    global count1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[i][j] == mat[x][y] and mat[x][y] == 0:
                
                
            


from pprint import pprint

n = int(input())
count0, count1 = 0,0
x,y = 0, 0

mat = [[0 for i in range(n)] for j in range(n)]

mat = [list(map(int, input().split())) for _ in range(n)]

divide(x,y,mat,n)

pprint(mat)
