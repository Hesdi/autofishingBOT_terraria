class SchoolMember:
    '''Представление любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('{0} is part of our school!'.format(self.name))
    def tell(self):
        '''Вывести информацию'''
        print('{0} is {1} years old'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''Представляет преподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('{0} is our teacher!'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {0}'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('{0} is our student'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Grades: {0}'.format(self.marks))

t = Teacher('Mrs. Khalida', "15*3", 80000)
s = Student('Hesdi', 16, 99.9)
s1 = SchoolMember('Hesd', 13)

print() # печатает пустую строку

members = [t, s, s1]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента