P, Q, S = map(int, input().split())
if P == 0:
    if Q == 0:
        if S > 0:
            x = - S**(1/3)
            xi = int(x)
            if x - xi == 0:
                print(3)
        elif S == 0:
            print(1)
        else:
            print(0)
    else:
        print(0)
elif Q == 0:
    if S == 0:
        if P > 0:
            x = -P
            print(2)
        else:
            print(0)
    else:
        print(0)
elif S == 0:
    if P == 0:
        if Q < 0:
            x = - Q
            print(3)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)