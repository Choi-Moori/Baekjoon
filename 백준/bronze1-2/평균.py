n = int(input())

list1 = list(map(int, input().split()))
maxn = max(list1)
num = []

for socre in list1:
    num.append((socre/maxn)*100)

print(sum(num)/n)

