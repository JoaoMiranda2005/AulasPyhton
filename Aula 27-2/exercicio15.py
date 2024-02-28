def main():
    try:
        N = int(input("Digite o número de elementos que deseja inserir na lista: "))
        lista_numeros = []

        for i in range(N):
            numero = float(input(f"Digite o {i+1}º número: "))
            lista_numeros.append(numero)

        print("Lista de números inseridos:", lista_numeros)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
