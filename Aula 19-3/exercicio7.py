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
        if b < 0:
            a *= -1
            b *= -1
        return self.simplificar_fracao(a, b)

    def __add__(self, other):
        novo_num = self.num * other.den + other.num * self.den
        novo_den = self.den * other.den
        return Fracao(f"{novo_num}/{novo_den}")

    def __sub__(self, other):
        novo_num = self.num * other.den - other.num * self.den
        novo_den = self.den * other.den
        return Fracao(f"{novo_num}/{novo_den}")

    def __mul__(self, other):
        novo_num = self.num * other.num
        novo_den = self.den * other.den
        return Fracao(f"{novo_num}/{novo_den}")

    def __truediv__(self, other):
        novo_num = self.num * other.den
        novo_den = self.den * other.num
        return Fracao(f"{novo_num}/{novo_den}")


# Exemplo de uso
fracao1 = Fracao()
print(fracao1)

fracao2 = Fracao(5)
print(fracao2)

fracao3 = Fracao("-10/5")
print(fracao3)