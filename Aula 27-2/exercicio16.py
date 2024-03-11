def main():
    try:
        N = int(input("Digite o número de elementos que deseja inserir na lista: "))
        lista_numeros = []
        for i in range(N):
            numero = float(input(f"Digite o {i + 1}º número: "))
            lista_numeros.append(numero)
        print("Lista de números inseridos:", lista_numeros)
        soma = sum(lista_numeros)
        print("Soma dos itens:", soma)
        media = soma / N
        print("Média dos valores:", media)
        maior_valor = max(lista_numeros)
        menor_valor = min(lista_numeros)
        print("Maior valor na lista:", maior_valor)
        print("Menor valor na lista:", menor_valor)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
if __name__ == "__main__":
    main()
