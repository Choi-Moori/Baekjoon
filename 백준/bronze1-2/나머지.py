import sys

a = [int(input()) for _ in range(10)]
count = 1
for i in range(10):
    a[i] = a[i] % 42

a.sort()
for i in range(1, 10):
    for j in range(i-1, i):
        if a[i] != a[j]:
            count += 1
            break
print(count)
