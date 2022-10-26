def counter(word):
    num1 = 0
    num2 = 0
    num3 = False

    array = ['а', 'и', 'е', 'ё', 'ы', 'ю', 'я', 'о', 'у', 'э', 'a', 'e', 'u', 'i', 'o']
    array1 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
              'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

    l = list(word.lower())

    for i in l:
        if i in array:
            num1 += 1
        elif i in " '":
            continue
        elif i in array1:
            num2 += 1
        else:
            num3 = True

    sum = num1 + num2
    prop = num1 * 100 / sum
    prop2 = num2 * 100 / sum

    print('Кол-во букв: ', sum)
    print('Согласных: ', num2)
    print('Гласных: ', num1)
    print(f'Гласные/Согласные: {round(prop, 2)}% / {round(prop2, 2)}%')

    if num3:
        print('В вашем имени есть странные символы!')

word = input('Слово: ')
counter(word)