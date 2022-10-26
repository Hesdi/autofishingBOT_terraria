the_list = ['Bac9', 'Max', 'Ray']
a = True

while a:
    print(the_list, '\nВы хотите изменить список?')
    answ = int(input('1 - добавить ментора, 2 - удалить ментора, 3 - изменить ментора'))

    if answ == 1:
        new = input('Имя нового ментора: ').capitalize()
        the_list.append(new)
    elif answ == 2:
        name = input('Кого увольняем?: ').capitalize()
        fired = the_list.index(name)
        del the_list[fired]
    else:
        who = input('Кого меняем?: ').capitalize()
        ment = the_list.index(who)
        del the_list[ment]
        what = input('На кого?: ').capitalize()
        the_list.insert(ment, what)