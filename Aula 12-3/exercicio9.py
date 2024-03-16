# Inicializando uma lista de 20 números inteiros
numeros = [i for i in range(1, 21)]

# Usando compreensão de listas para separar números pares e ímpares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# Imprimindo as listas de números pares e ímpares
print("Números pares:", pares)
print("Números ímpares:", impares)
