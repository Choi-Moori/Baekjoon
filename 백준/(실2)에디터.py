import sys
input = sys.stdin.readline
from collections import deque

left_st = deque(list(input().rstrip()))
right_st = deque()

n = int(input())

for i in range(n):
    s = input().split()
    if s[0] == 'P':
        left_st.append(s[1])
    elif s[0] == 'L':
        if len(left_st) != 0:
            right_st.appendleft(left_st.pop())
    elif s[0] == 'D':
        if len(right_st) != 0:
            left_st.append(right_st.popleft())
    elif s[0] == 'B':
        if len(left_st) != 0:
            left_st.pop()

st = left_st + right_st
st = ''.join(s for s in st)
print(st)
