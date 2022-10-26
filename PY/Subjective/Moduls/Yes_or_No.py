import keyboard


def Yes():
    print('YES!')
def No():
    print('NO!')
keyboard.add_hotkey('y', Yes)
keyboard.add_hotkey('n', No)


keyboard.wait('Esc')
