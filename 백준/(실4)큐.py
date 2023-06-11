import sys

input = sys.stdin.readline

n = int(input())

que = []
def empty():
    if not que:
        return 1
    else:
        return 0


for i in range(n):
    s = input().split()
    
    if s[0] == "push":
        que.append(s[1])

    elif s[0] == "pop":
        emp = empty()
        if emp:
            print("-1")
        else:
            print(que[0])
            del que[0]
    elif s[0] == "size":
        print(len(que))
    elif s[0] == "empty":
        print(empty())
    elif s[0] == "front":
        emp = empty()
        if emp:
            print("-1")
        else:
            print(que[0])
    elif s[0] == "back":
        emp = empty()
        if emp:
            print("-1")
        else:
            print(que[-1])
