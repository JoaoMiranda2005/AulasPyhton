def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b


def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    escolha = input("Digite o número da operação desejada: ")
    return escolha


def main():
    escolha = menu()

    if escolha in ['1', '2', '3', '4']:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if escolha == '1':
            resultado = soma(valor1, valor2)
        elif escolha == '2':
            resultado = subtracao(valor1, valor2)
        elif escolha == '3':
            resultado = multiplicacao(valor1, valor2)
        elif escolha == '4':
            resultado = divisao(valor1, valor2)

        print("O resultado da operação é:", resultado)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
