import sys
input = sys.stdin.readline
n = int(input().rstrip())
num_list = list(map(int, input().split()))
k = int(input().rstrip())
num_list.sort(reverse=True)

count = 0
low = 0
high = n-1

while low <= high :
    if num_list[low] > k:
        low += 1
    elif low == high:
        if num_list[low] == k and num_list[low] != num_list[-1]:
            count += 1
        else:
            break
    elif num_list[low]+num_list[high] == k:
        count += 1
        high -= 1
        
    elif num_list[low]+num_list[high] > k:
        low += 1
        
    elif num_list[low]+num_list[high] < k:
        high -= 1        

print(count)
