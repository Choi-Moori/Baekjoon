import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())
b_list = []
for _ in range(n):
    b_list.append(input().rstrip())

b_list.sort()

cnt_b = Counter(b_list).most_common()

print(cnt_b[0][0])
