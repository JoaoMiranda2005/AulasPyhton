def multi_multiplicacao(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# Exemplo de uso:
resultado = multi_multiplicacao(2, 3, 4)
print(resultado)
