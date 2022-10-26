def greet(name):
    print('hello ' + name + '!')
    greet2(name)
    print('getting ready to say bye...')
    bye()

def greet2(name):
    print('How are you, ' + name + '?')

def bye():
    print('ok, bye!')

your_name = 'hesdi'
greet(your_name)