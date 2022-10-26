jobs = ['Python', 'PHP', 'HTML', 'CSS']


class Animal:
    def __init__(self, name, diet, safe):
        self.name = name
        self.d = diet
        self.s = safe

    def __str__(self):
        return f'{self.name}. They eat {self.d}. It is {self.s} to stay near to them'

    def say(self):
        print(self.name)

class Mamm(Animal):
    def __init__(self, name, diet, safe, feathers):
        super().__init__(name, diet, safe)
        self.f = feathers

    def __str__(self):
         return super().__str__() + f'\n {self.name} is mammal and {self.f} have feathers\n\n'


ani1 = Mamm('Zebra', 'grasses', 'safe', "don't")



class Rept(Animal):
    def __init__(self, name, diet, safe, aquatic):
        super().__init__(name, diet, safe)
        self.ac = aquatic

    def __str__(self):
        return super().__str__() + f'\n {self.name} is reptile and {self.ac} swim'


ani2 = Rept('Crocodile', 'fish', 'dangerous', 'can')


Zoo = [ani1, ani2]
print('В нашем ассартименте есть:')
ani1.say(), ani2.say()
var = int(input('Билет к 1му будет стоить 10$, ко 2му 15$. Какой вы хотите? 1 / 2 '))
if var == 1:
    print(ani1)

else:
    print(ani2)
