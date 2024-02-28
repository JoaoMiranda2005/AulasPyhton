def contar_nomes(lista_nomes):
    contagem_nomes = {}
    for nome in lista_nomes:
        if nome in contagem_nomes:
            contagem_nomes[nome] += 1
        else:
            contagem_nomes[nome] = 1
    return contagem_nomes

def main():
    lista_nomes = ['nome1', 'nome2', 'nome1', 'nome3', 'nome2', 'nome1']  # Exemplo de lista de nomes
    contagem = contar_nomes(lista_nomes)
    print("Contagem de nomes:")
    for nome, quantidade in contagem.items():
        print(f"{nome}: {quantidade} vezes")

if __name__ == "__main__":
    main()
