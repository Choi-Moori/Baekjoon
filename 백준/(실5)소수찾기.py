import sys
input = sys.stdin.readline

n = int(input().rstrip())
numl = list(map(int ,input().split()))
count = 0

for num in numl:
    check = False

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check = True
        if not check:
            count += 1

print(count)
