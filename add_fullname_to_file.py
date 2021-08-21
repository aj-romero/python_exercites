
def addFullNametoFile(name, surname):
    f = open('fullname_database','a')
    f.write(name + ' ' + surname + '\n')
    f.close()

n = input('set the name: ')
s = input('set the surname: ')

addFullNametoFile(n, s)

