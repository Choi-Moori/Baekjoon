import sys
input = sys.stdin.readline
n,m = list(map(int, input().split()))
##s = []
##for _ in range(n):
##    s.append(input().rstrip())
##
##check = [input().rstrip() for _ in range(m)]
##
##for i in check:
##    for j in s:
##        if j[0:len(i)] == i:
##            print(j[len(i)+1:].strip())

add = {}
for _ in range(n):
    site, ps = input().split()

    add[site] = ps

for _ in range(m):
    print(add[input().rstrip()])
