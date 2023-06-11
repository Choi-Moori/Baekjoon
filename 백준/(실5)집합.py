import sys
input = sys.stdin.readline
n = int(input().rstrip())
num_list = set()


for _ in range(n):
    s = input().split()
    
    if s[0] == 'all':
        num_list = set([i for i in range(1,21)])
    elif s[0] == 'add':
        num_list.add(int(s[1]))
    elif s[0] == 'remove':
        num_list.discard(int(s[1]))
    elif s[0] == 'check':
        if int(s[1]) in num_list:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if int(s[1]) in num_list:
            num_list.discard(int(s[1]))
        else:
            num_list.add(int(s[1]))
    elif s[0] == 'empty':
        num_list -= num_list
