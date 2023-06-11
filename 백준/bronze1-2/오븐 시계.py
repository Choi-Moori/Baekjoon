h, m = list(map(int, input().split()))
cm = int(input())

if m+cm < 60:
    print(h, m+cm)
else:
    print((h+((m+cm)//60))%24, (m+cm)%60)
