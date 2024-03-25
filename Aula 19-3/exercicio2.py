class Fracao:
    def __init__(self, num_den):
        num, den = map(int, num_den.split('/'))
        self.num = num
        self.den = den

minha_fracao = Fracao("3/4")
print("Numerador:", minha_fracao.num)
print("Denominador:", minha_fracao.den)
