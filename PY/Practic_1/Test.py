lesson = ("N", "O", "H", "T", "Y", "P", "E", "V", "O", "L", "I", True, False, 2, 1, 3, 5, 4, 11, 13, 12.12, 33.222, True, False)
word = []
number = []
bollean = []
llesson = list(lesson)
for i in llesson:
    if type(i) == str:
        word.append(i)
    elif type(i) == int:
        number.append(i)
    elif type(i) == bool:
        bollean.append(i)
    else:
        continue

word.insert(6, ' ')
word.insert(11, ' ')
word = ('').join(word[::-1])
number.sort()
number = tuple(number)

print(word, '\n', number)

inai= {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del inai['bag']
inai['instagram'] = '@inai'
inai['number'] = '996999000404'
inai['address'] = 'Maldybaeva 34b'
courses = []
new = input('What are new courses? ')
courses.append(new.capitalize())
inai['courses'] += courses

print(inai)
asdgf