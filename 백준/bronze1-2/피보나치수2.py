n = int(input())
num1 = []
num1.append(0)
num1.append(1)
num1.append(1)


if n == 1:
    print(num1[1])
elif n == 2:
    print(num1[2])
else:
    for i in range(2, n):
        num1.append(num1[i] + num1[i-1])
    print(num1[n])
    
