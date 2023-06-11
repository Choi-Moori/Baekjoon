import time

start = time.time()

n = int(input())

for j in range(n):
    a,b = map(int,input().split())
    for i in range(max(a,b), 100000000000 , +max(a,b)):
        if i%a == 0 and i % b == 0:
            print(i)
            break

print("time :", time.time() -start)
