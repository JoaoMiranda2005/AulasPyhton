# Função para ler uma lista de valores do usuário
def ler_lista():
    lista = []
    while True:
        valor = input("Digite um valor (ou digite 'fim' para encerrar): ")
        if valor.lower() == 'fim':
            break
        lista.append(float(valor))
    return lista

# Função para gerar uma nova lista com o dobro dos valores da lista original
def dobrar_valores(lista):
    return [valor * 2 for valor in lista]

# Ler uma lista de valores do usuário
lista_original = ler_lista()

# Gerar uma nova lista com o dobro dos valores da lista original
lista_dobro = dobrar_valores(lista_original)

# Imprimir a nova lista
print("Lista com o dobro dos valores:")
print(lista_dobro)
