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

    def __int__(self):
        return self.num // self.den

    def __float__(self):
        return self.num / self.den

    def __bool__(self):
        return bool(self.num)


fracao = Fracao("3/4")

# Conversão para inteiro
print("Inteiro:", int(fracao))

# Conversão para float
print("Float:", float(fracao))

# Conversão para booleano
print("Booleano:", bool(fracao))
