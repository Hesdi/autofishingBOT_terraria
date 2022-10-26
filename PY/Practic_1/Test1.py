w = input('Integer: ')
n = int(input('Power: '))
max1 = int(input('Max value: '))
wl = list(w)
lw = wl[::-1]
ilw = ''.join(lw)
swl = 0
mwl = 1
num = 0
num1 = 1

Usl = True

for i in wl:
    i1 = int(i)
    mwl *= i1
    swl += i1

while Usl:
    num += 1
    num1 = num**n
    res = (num - 1)**n
    if num1 >= max1:
        Usl = False
        print(res)


print('The Sum ', swl)
print('The opposite ', ilw)
print('The Product ', mwl)
