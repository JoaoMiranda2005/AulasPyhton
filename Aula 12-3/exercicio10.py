# Função para calcular a média de uma lista de números
def calcular_media(lista):
    return sum(lista) / len(lista)

# Função para obter o nome do mês com base no número
def obter_nome_mes(numero_mes):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[numero_mes - 1]

# Recebendo as temperaturas médias de cada mês
temperaturas = []
for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média de {obter_nome_mes(mes)}: "))
    temperaturas.append(temperatura)

# Calculando a média anual das temperaturas
media_anual = calcular_media(temperaturas)

# Encontrando as temperaturas acima da média anual e em quais meses elas ocorreram
temperaturas_acima_media = [(mes, temperatura) for mes, temperatura in enumerate(temperaturas, start=1) if temperatura > media_anual]

# Imprimindo a média anual e as temperaturas acima da média com os meses correspondentes
print(f"A média anual das temperaturas é: {media_anual:.2f}°C")
print("Temperaturas acima da média anual:")
for mes, temperatura in temperaturas_acima_media:
    print(f"{obter_nome_mes(mes)}: {temperatura}°C")
