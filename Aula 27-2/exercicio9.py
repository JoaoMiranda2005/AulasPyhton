def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def main():
    try:
        numero = int(input("Digite um número inteiro para calcular o fatorial: "))
        if numero < 0:
            print("O fatorial não está definido para números negativos.")
        else:
            resultado = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {resultado}")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
