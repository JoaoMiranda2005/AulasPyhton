class Fracao:
    def __init__(self, num_den):
        num, den = map(int, num_den.split('/'))
        num, den = self.desimplificar_fracao(num, den)
        self.num = num
        self.den = den

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
fracao = Fracao("6/9")
print(fracao)
