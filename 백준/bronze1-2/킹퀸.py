k,q,l,b,kn,p = list(map(int, input().split()))

kc = qc = lc = bc = knc = pc = 0

while k!=1:
    if k <= 0:
        k += 1
        kc += 1
    elif k >= 2:
        k -= 1
        kc -= 1

while q!=1:
    if q <= 0:
        q += 1
        qc += 1
    elif q >= 2:
        q -= 1
        qc -= 1

while l!=2:
    if l <= 1:
        l += 1
        lc += 1
    elif l >=3:
        l -= 1
        lc -= 1

while b != 2:
    if b <= 1:
        b+=1
        bc += 1
    elif b>=3:
        b -=1
        bc -= 1
while kn != 2:
    if kn <= 1:
        kn+=1
        knc += 1
    elif kn >= 3:
        kn -=1
        knc-=1
while p != 8:
    if p <= 7:
        p+=1
        pc+=1
    elif p >= 9:
        p -= 1
        pc-=1

print(kc, qc, lc, bc, knc,pc)
