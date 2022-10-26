def countdown(i):
    print(i)
    # Basic term
    if i <= 0:
        print('Done')
    # Recursive term
    else:
        countdown(i - 1)


countdown(10)
