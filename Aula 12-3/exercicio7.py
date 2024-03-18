def calcular_media(notas):
    return sum(notas) / len(notas)

def ler_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    return notas

def mostrar_notas_e_media(notas):
    print("Notas inseridas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    media = calcular_media(notas)
    print(f"Média das notas: {media:.2f}")

notas = ler_notas()

mostrar_notas_e_media(notas)
