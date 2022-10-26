def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 4, 5, 6, 8, 9]
number = int(input('What do you wonna find? '))
print('It\'s found on location -', binary_search(my_list, number) + 1)

