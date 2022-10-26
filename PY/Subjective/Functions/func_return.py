def maximum(x, y):
    """Underline the highest number

    They can be equal"""

    if x > y :
        return x
    elif x == y:
        return 'Numbers are equal'
    else:
        return y

x = input('Enter number: ')
y = input('Enter another: ')

print(maximum(x, y))