a = True
print('Загадайте число!')
n0 = int(input('От: '))
n10 = int(input('До: '))
n = (n10 - n0)//2 + n0

def more(n):
    n = n + round((n10 - n0)/2)
    return n


def less(n):
    n = n - round((n10 - n0)/2)
    return n


while a:
    res = input(f"Ваше число больше - >, меньше - <, равно - = {n}?")
    M = ['.', 'ю', '>']
    L = [',', '<', 'б']
    if n in range(n0, n10):
        if res in L:
            n10 = n
            n = less(n)


        elif res in M:
            n0 = n
            n = more(n)


        else:
            print('Ваше число: ', n)
            a = False

