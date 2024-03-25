class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"

    def num(self):
        return self.numerador

    def den(self):
        return self.denominador

    def __add__(self, other):
        novo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        novo_denominador = self.denominador * other.denominador
        return Racional(novo_numerador, novo_denominador)

    def __mul__(self, other):
        novo_numerador = self.numerador * other.numerador
        novo_denominador = self.denominador * other.denominador
        return Racional(novo_numerador, novo_denominador)


# Exemplo de uso
r1 = Racional(2, 4)
r2 = Racional(1, 6)

print(r1)
print(r2)
print(r1 + r2)
print(r1 * r2)
