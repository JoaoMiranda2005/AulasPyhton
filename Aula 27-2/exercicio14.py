def produto_escalar(vetor1, vetor2):
    resultado = sum(x * y for x, y in zip(vetor1, vetor2))
    return resultado

def produto_vetorial(vetor1, vetor2):
    resultado = [vetor1[1]*vetor2[2] - vetor1[2]*vetor2[1],
                 vetor1[2]*vetor2[0] - vetor1[0]*vetor2[2],
                 vetor1[0]*vetor2[1] - vetor1[1]*vetor2[0]]
    return resultado

def main():
    vetor1 = []
    vetor2 = []

    print("Digite os valores do primeiro vetor:")
    for i in range(3):
        valor = float(input(f"Digite o {i+1}º valor: "))
        vetor1.append(valor)

    print("\nDigite os valores do segundo vetor:")
    for i in range(3):
        valor = float(input(f"Digite o {i+1}º valor: "))
        vetor2.append(valor)

    print("\nVetor 1:", vetor1)
    print("Vetor 2:", vetor2)

    produto_esc = produto_escalar(vetor1, vetor2)
    print("\nProduto Escalar:", produto_esc)

    produto_vet = produto_vetorial(vetor1, vetor2)
    print("Produto Vetorial:", produto_vet)

if __name__ == "__main__":
    main()
