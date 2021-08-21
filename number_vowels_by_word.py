word = input('set the word: ')
vowels = 0
for w in word:
    o = w.lower()
    vowels += 1 if o == 'a' or o == 'e' or o == 'i' or o == 'o' or o == 'u' else 0

print('the number of vowels is: ',vowels)
