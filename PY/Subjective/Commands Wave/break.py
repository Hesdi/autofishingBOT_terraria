while True:
	s = input('Enter: ')
	if s == "exit" :
		break
	if len(s) < 3:
		print('Слишком мало')
		continue
	print('Введённая строка достаточной длины')
print('end')