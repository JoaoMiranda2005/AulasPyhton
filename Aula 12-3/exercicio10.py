def calcular_media(lista):
    return sum(lista) / len(lista)

def obter_nome_mes(numero_mes):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[numero_mes - 1]

temperaturas = []
for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média de {obter_nome_mes(mes)}: "))
    temperaturas.append(temperatura)

media_anual = calcular_media(temperaturas)

temperaturas_acima_media = [(mes, temperatura) for mes, temperatura in enumerate(temperaturas, start=1) if temperatura > media_anual]

print(f"A média anual das temperaturas é: {media_anual:.2f}°C")
print("Temperaturas acima da média anual:")
for mes, temperatura in temperaturas_acima_media:
    print(f"{obter_nome_mes(mes)}: {temperatura}°C")
