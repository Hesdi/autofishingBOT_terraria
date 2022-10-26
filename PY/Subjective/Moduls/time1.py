import time

deter = '_'
a = time.strftime('%Y_%m:%S')
b = deter.join(a)

example = ('example' + time.strftime(a))
print(example)