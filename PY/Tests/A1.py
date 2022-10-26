def range(x, k):
    r = x - k
    if r < 0:
        r = -r
    else:
        r = r
    return r

Xa, Ya = map(int, input().split())
Xb, Yb = map(int, input().split())
Xk, Yk = map(int, input().split())

Adil = range(Xa, Xk) + range(Ya,Yk)
Bayel = range(Xb, Xk) + range(Yb,Yk)

if Adil > Bayel:
    print('Bayel')
elif Adil < Bayel:
    print('Adil')
else:
    print('Adil and Bayel')