class Fracao:
    def __init__(self, num_den=None):
        if num_den is None:
            self.num = 0
            self.den = 1
        elif isinstance(num_den, int):
            self.num = num_den
            self.den = 1
        else:
            num, den = map(int, num_den.split('/'))
            self.num, self.den = self.desimplificar_fracao(num, den)

    def __repr__(self):
        return f"{self.num}/{self.den}"

    @staticmethod
    def simplificar_fracao(a, b):
        def mdc(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        divisor_comum = mdc(a, b)
        return a // divisor_comum, b // divisor_comum

    def desimplificar_fracao(self, a, b):
        if b < 0:  # Ajusta o sinal apenas para o numerador
            a *= -1
            b *= -1
        return self.simplificar_fracao(a, b)

    def __lt__(self, other):
        if isinstance(other, Fracao):
            return self.num * other.den < other.num * self.den
        elif isinstance(other, int):
            return self.num < other * self.den
        else:
            raise TypeError("Operação não suportada: comparação entre Fracao e tipo diferente")

    def __le__(self, other):
        if isinstance(other, Fracao):
            return self.num * other.den <= other.num * self.den
        elif isinstance(other, int):
            return self.num <= other * self.den
        else:
            raise TypeError("Operação não suportada: comparação entre Fracao e tipo diferente")

    def __eq__(self, other):
        if isinstance(other, Fracao):
            return self.num * other.den == other.num * self.den
        elif isinstance(other, int):
            return self.num == other * self.den
        else:
            raise TypeError("Operação não suportada: comparação entre Fracao e tipo diferente")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)


# Exemplo de uso
fracao1 = Fracao("3/4")
fracao2 = Fracao("5/6")

print(fracao1 < fracao2)
print(fracao1 <= fracao2)
print(fracao1 == fracao2)
print(fracao1 != fracao2)
print(fracao1 >= fracao2)
print(fracao1 > fracao2)
