# My shop list
shoplist = ['apples', 'yogurt', 'pasta']

print('I must make', len(shoplist), "purchases")

print('Purchases', end=': ')
for item in shoplist:
    print(item, end=', ')

print('\nAlso rice')
shoplist.append('rice')
print('Now my shop list is:', shoplist)

print("Let's sort my list")
shoplist.sort()
print("My sorted shop list", shoplist)

print('First i will buy', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I've bought ", olditem)
print("So my shop list remains: ", shoplist)
