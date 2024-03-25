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

    def __add__(self, other):
        if isinstance(other, Fracao):
            novo_num = self.num * other.den + other.num * self.den
            novo_den = self.den * other.den
            return Fracao(f"{novo_num}/{novo_den}")
        elif isinstance(other, int):
            novo_num = self.num + other * self.den
            return Fracao(f"{novo_num}/{self.den}")
        else:
            raise TypeError("Operação não suportada: adição entre Fracao e tipo diferente")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fracao):
            novo_num = self.num * other.den - other.num * self.den
            novo_den = self.den * other.den
            return Fracao(f"{novo_num}/{novo_den}")
        elif isinstance(other, int):
            novo_num = self.num - other * self.den
            return Fracao(f"{novo_num}/{self.den}")
        else:
            raise TypeError("Operação não suportada: subtração entre Fracao e tipo diferente")

    def __rsub__(self, other):
        return Fracao(f"{other * self.den - self.num}/{self.den}")

    def __mul__(self, other):
        if isinstance(other, Fracao):
            novo_num = self.num * other.num
            novo_den = self.den * other.den
            return Fracao(f"{novo_num}/{novo_den}")
        elif isinstance(other, int):
            novo_num = self.num * other
            return Fracao(f"{novo_num}/{self.den}")
        else:
            raise TypeError("Operação não suportada: multiplicação entre Fracao e tipo diferente")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fracao):
            novo_num = self.num * other.den
            novo_den = self.den * other.num
            return Fracao(f"{novo_num}/{novo_den}")
        elif isinstance(other, int):
            novo_den = self.den * other
            return Fracao(f"{self.num}/{novo_den}")
        else:
            raise TypeError("Operação não suportada: divisão entre Fracao e tipo diferente")

    def __rtruediv__(self, other):
        return Fracao(f"{other * self.den}/{self.num}")


# Exemplo de uso
fracao1 = Fracao("3/4")
resultado1 = fracao1 + 2
print(resultado1)

resultado2 = 5 - fracao1
print(resultado2)

resultado3 = fracao1 * 3
print(resultado3)

resultado4 = 10 / fracao1
print(resultado4)

