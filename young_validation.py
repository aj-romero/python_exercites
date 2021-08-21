def isYoung(usuario):
    return usuario.edad < 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

young = Usuario(15)
older = Usuario (21)

result_young = isYoung(young)
result_older = isYoung(older)

print(result_young, result_older)
