## time complexty == logn

def matmult(a,b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = (c[i][j]+ a[i][k]*b[k][j])%1000
    return c
## mat1^10 = (mat1^5)^2 = (((mat1^2)^2)*mat)^2
## a^11 = ((mat1^5)^2)*mat = (((mat1^2)^2)*mat)^2
def conqu(b, mat):
    if b == 1:
        return mat
    elif b % 2 == 0:
        mat1 = conqu(b//2, mat)
        return matmult(mat1,mat1)
    elif b % 2 == 1:
        mat1 = conqu(b-1,mat)
        return matmult(mat,mat1)

n , b = map(int, input().split())

mat = [[0] * n for _ in range(n)]
mat = [list(map(int, input().split())) for _ in range(n)]


mat1 = conqu(b, mat)

for i in range(n):
    for j in range(n):
        print(mat1[i][j]%1000, end= ' ')
    print()
