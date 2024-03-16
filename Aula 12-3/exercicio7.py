# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para ler as notas do usuário
def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    return notas

# Função para mostrar as notas e a média
def mostrar_notas_e_media(notas):
    print("Notas inseridas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    media = calcular_media(notas)
    print(f"Média das notas: {media:.2f}")

# Ler as notas do usuário
notas = ler_notas()

# Mostrar as notas e a média
mostrar_notas_e_media(notas)
