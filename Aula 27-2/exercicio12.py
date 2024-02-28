def contar_nomes(lista_nomes):
    contagem_nomes = {}
    for nome in lista_nomes:
        if nome in contagem_nomes:
            contagem_nomes[nome] += 1
        else:
            contagem_nomes[nome] = 1
    return contagem_nomes


def main():
    lista_nomes = []

    print("Digite os nomes (digite uma string vazia para finalizar):")
    while True:
        nome = input("Nome: ")
        if nome == "":
            break
        lista_nomes.append(nome)

    contagem = contar_nomes(lista_nomes)
    print("\nContagem de nomes:")
    for nome, quantidade in contagem.items():
        print(f"{nome}: {quantidade} vezes")


if __name__ == "__main__":
    main()
