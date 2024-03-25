class Estacionamento:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.lugares_livres = capacidade

    def entra(self):
        if self.lugares_livres > 0:
            self.lugares_livres -= 1
            print("Carro entrou no estacionamento.")
        else:
            print("O estacionamento está lotado. Não há mais vagas disponíveis.")

    def sai(self):
        if self.lugares_livres < self.capacidade:
            self.lugares_livres += 1
            print("Carro saiu do estacionamento.")
        else:
            print("O estacionamento já está vazio. Não há carros para sair.")

    def lugares(self):
        return self.lugares_livres


# Exemplo de uso
est = Estacionamento(20)
print(est.lugares())
est.entra()
est.entra()
est.entra()
est.entra()
est.sai()
print(est.lugares())
