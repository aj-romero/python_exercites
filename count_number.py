number_list = []
print('Set the numbers and for exit write "stop"')

while True:
    number = input('set the number: ')
    if number == 'stop':
        break
    else:
        try:
            number = int(number)
            number_list.append(number)
        except:
            print('input number is not correct')
            exit()

result = 0

for x in number_list:
    result += x

print('the sum of the numbers entered is: ',result)
