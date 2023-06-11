x,y,w,h = map(int, input().split())


c = min(w-x, x , h - y, y)

if x == 1 or y == 1:
    c == 1

print(c)
