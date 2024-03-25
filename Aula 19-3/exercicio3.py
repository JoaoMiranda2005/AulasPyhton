class Fracao:
    def __init__(self, num_den):
        num, den = map(int, num_den.split('/'))
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"


minha_fracao = Fracao("3/4")
print(minha_fracao)
