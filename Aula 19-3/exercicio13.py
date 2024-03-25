class Automovel:
    def __init__(self, capacidade_deposito, quantidade_combustivel, consumo_litros_por_100km):
        self.capacidade_deposito = capacidade_deposito
        self.quantidade_combustivel = quantidade_combustivel
        self.consumo_litros_por_100km = consumo_litros_por_100km

    def combustivel(self):
        return self.quantidade_combustivel

    def autonomia(self):
        return int((self.quantidade_combustivel / self.consumo_litros_por_100km) * 100)

    def abastece(self, n_litros):
        if self.quantidade_combustivel + n_litros <= self.capacidade_deposito:
            self.quantidade_combustivel += n_litros
            return f"{self.autonomia()} Km até abastecimento"
        else:
            raise ValueError("Capacidade máxima do depósito excedida")

    def percorre(self, n_km):
        combustivel_necessario = (self.consumo_litros_por_100km * n_km) / 100
        if combustivel_necessario <= self.quantidade_combustivel:
            self.quantidade_combustivel -= combustivel_necessario
            return f"{self.autonomia()} Km até abastecimento"
        else:
            raise ValueError("Não tem autonomia para esta viagem")


a1 = Automovel(60, 10, 15)
print(a1.combustivel())
print(a1.autonomia())
print(a1.abastece(45))
print(a1.percorre(150))
try:
    print(a1.percorre(250))
except ValueError as e:
    print(e)
