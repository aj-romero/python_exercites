def isPair(number):
    return number % 2 == 0

a = int(input('set the integer number: '))

result = isPair(a)

print('The number is pair '+ str(a) if result else 'the number is odd')
