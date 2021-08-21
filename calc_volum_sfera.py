def calcVolmSfera(radio):
    return 4 / 3 * 3.14 * radio ** 3

r = float(input('Set the radio of sfera: '))

result = calcVolmSfera(r)
print(result)
