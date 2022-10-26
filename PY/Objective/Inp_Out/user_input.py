#Palindrome
def reverse(text):
    return text[::-1]

def is_pal(text):
    return text == reverse(text)

smth = input('Write: ')
new_smth = ''

#Deleting register
for symbol in smth:
    if symbol.isupper():
        new_smth += symbol.lower()
    else:
        new_smth += symbol
#Make into list to delete forbidden symbols
l = list(new_smth)

forbidden = [',', '.', '?', ';', '/', '[', ']', '!', ':', '-', '(', ')', ' ']
for item in l:
    if item in forbidden:
        p = l.index(item)
        del(l[p])

#Return to str
new_smth = "".join(l)

if (is_pal(new_smth)):
    print("Yes! It's palindrome")
else:
    print("No, it's not palindrome")