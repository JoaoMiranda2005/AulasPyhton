def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Exemplo de uso:
n = int(input("Digite o valor de n: "))
resultado = fibonacci_recursivo(n)
print(f"O {n}º número da sequência de Fibonacci é:", resultado)
