list = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in list:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('the lowest number is: ',menor)
