import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]



def conqu(mat, leng, x, y):
    w = leng//3
    for i in range(w):
        

x,y = 0,0

conqu(mat, n, x, y)
