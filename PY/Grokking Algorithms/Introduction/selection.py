def find_smallest(arg):
    smallest = arg[0]
    smallest_ind = 0

    for i in range(1, len(arg)):
        if arg[i] < smallest:
            smallest = arg[i]
            smallest_ind = i
    return smallest_ind

def selsort(arg):
    newarg = []

    for i in range(len(arg)):
        smallest = find_smallest(arg)
        newarg.append(arg.pop(smallest))
    return newarg

print(selsort([5, 6, 1, 2, 3, 4]))