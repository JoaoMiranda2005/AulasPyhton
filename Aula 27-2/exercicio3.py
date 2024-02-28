t = int(input("Insere o número de segundos:\n"))

horas = t // 3600
minutos = (t % 3600) // 60
segundos = t % 60

print("Horas:",horas)
print("Minutos:",minutos)
print("Segundos:",segundos)