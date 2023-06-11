import time

n = int(input())

start = time.time()

f = []
f.append(0)
f.append(1)
f.append(1)

if n == 0:
    print(f[0])
elif n == 1:
    print(f[1])
else:
    for i in range (2, n):
        f.append(f[i] + f[i-1])

print(f[n])

print("time :", time.time() - start)
