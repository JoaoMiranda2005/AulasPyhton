def encontrar_maior_menor_idade(idades):
    maior_idade = max(idades)
    menor_idade = min(idades)
    return maior_idade, menor_idade

def ler_idades():
    idades = []
    for i in range(20):
        idade = int(input(f"Digite a idade {i + 1}: "))
        idades.append(idade)
    return idades

idades = ler_idades()


maior_idade, menor_idade = encontrar_maior_menor_idade(idades)


print(f"A maior idade é: {maior_idade} anos")
print(f"A menor idade é: {menor_idade} anos")
