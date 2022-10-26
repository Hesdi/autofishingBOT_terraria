num = 12
guess = int(input('Enter a number: '))

if guess == num:
	print('Congritulations!? You won nothing)')
elif guess > num:
	print('The number is a bit less')
else:
	print('The number is a bit more')
print('End')
