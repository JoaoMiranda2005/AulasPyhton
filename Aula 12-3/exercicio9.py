numeros = [i for i in range(1, 21)]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", impares)
