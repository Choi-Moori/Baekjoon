import sys
input = sys.stdin.readline
t = int(input().rstrip())


def fibo(n):
    global cz, co
    if n == 0:
        cz += 1
        return 0
    elif n == 1:
        co += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


for i in range(t):
    num = int(input().rstrip())
    cz = co = 0
    fibo(num)

    print(cz, co)
