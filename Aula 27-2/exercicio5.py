def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence[:n]

def main():
    try:
        n = int(input("Digite o número de elementos da sequência de Fibonacci que deseja imprimir: "))
        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
            return
        sequence = fibonacci(n)
        print(f"Os primeiros {n} números da sequência de Fibonacci são: {sequence}")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
