class Fracao:
    def __init__(self, num_den):
        num, den = map(int, num_den.split('/'))
        self.num = num
        self.den = den

    def __repr__(self):
        return f"{self.num}/{self.den}"

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


fracao1 = Fracao("1/2")
fracao2 = Fracao("3/4")

# Adição
resultado_adicao = fracao1 + fracao2
print("Adição:", resultado_adicao)

# Subtração
resultado_subtracao = fracao1 - fracao2
print("Subtração:", resultado_subtracao)

# Multiplicação
resultado_multiplicacao = fracao1 * fracao2
print("Multiplicação:", resultado_multiplicacao)

# Divisão
resultado_divisao = fracao1 / fracao2
print("Divisão:", resultado_divisao)
