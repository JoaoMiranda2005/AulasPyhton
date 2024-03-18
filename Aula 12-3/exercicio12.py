import random


def criar_matriz_aleatoria(num_linhas, num_colunas):
    matriz = []
    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            linha.append(random.randint(0, 100))  # Números inteiros aleatórios de 0 a 100
        matriz.append(linha)
    return matriz

num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))


matriz_aleatoria = criar_matriz_aleatoria(num_linhas, num_colunas)

print("Matriz Aleatória:")
for linha in matriz_aleatoria:
    print(linha)
