# Função para encontrar a maior e a menor idade em uma lista
def encontrar_maior_menor_idade(idades):
    maior_idade = max(idades)
    menor_idade = min(idades)
    return maior_idade, menor_idade

# Função para ler as idades do usuário
def ler_idades():
    idades = []
    for i in range(20):
        idade = int(input(f"Digite a idade {i + 1}: "))
        idades.append(idade)
    return idades

# Ler as idades do usuário
idades = ler_idades()

# Encontrar a maior e a menor idade
maior_idade, menor_idade = encontrar_maior_menor_idade(idades)

# Mostrar a maior e a menor idade
print(f"A maior idade é: {maior_idade} anos")
print(f"A menor idade é: {menor_idade} anos")
