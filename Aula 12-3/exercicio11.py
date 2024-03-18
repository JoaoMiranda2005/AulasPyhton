def ler_lista():
    lista = []
    while True:
        valor = input("Digite um valor (ou digite 'fim' para encerrar): ")
        if valor.lower() == 'fim':
            break
        lista.append(float(valor))
    return lista

def dobrar_valores(lista):
    return [valor * 2 for valor in lista]

lista_original = ler_lista()


lista_dobro = dobrar_valores(lista_original)

print("Lista com o dobro dos valores:")
print(lista_dobro)
