import sys
input = sys.stdin.readline
n = int(input().rstrip())
num = list(map(int, input().split()))
res = 0

for i in range(0, n , 2):
    res += num[i]
##
##ans = res
##res1 = res
##
##for i in range(n-1, 0, -2):
##    res1 += num[i]
##    res1 -= num[i-1]
##    ans = max(ans, res1)
##
##print(ans)
##
##for i in range(n-2, 1, -2):
##    res -= num[i]
##    res += num[i-1]
##    ans = max(ans,res)
##print(ans)
res1 = res
ans = res

for i in range(n-1, 0, -2):
    res1 -= num[i-1]
    res1 += num[i]
    ans = max(res1, ans)
    print(ans, res1)
print(ans)
