class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi, my name is', self.name)

Person('Hesdi').say_hi()
