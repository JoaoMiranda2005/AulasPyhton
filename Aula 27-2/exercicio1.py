def calcular_tempo(t):
    horas = t // 3600
    minutos = (t % 3600) // 60
    segundos = t % 60
    return horas, minutos, segundos

def main():
    t = int(input("Digite a quantidade total de segundos: "))
    horas, minutos, segundos = calcular_tempo(t)
    print(f"{t} segundos correspondem a {horas} horas, {minutos} minutos e {segundos} segundos.")

if __name__ == "__main__":
    main()
