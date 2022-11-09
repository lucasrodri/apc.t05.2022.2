"""
Se eu sair da minha casa às 6:52 e correr 1
quilômetro a um certo passo (8min15s por
quilômetro), então 3 quilômetros a um passo
mais rápido (7min12s por quilômetro) e 1
quilômetro no mesmo passo usado em primeiro
lugar, que horas chego em casa para o café
da manhã?
"""
horas_inicial = int(input("Informe a hora inicial: "))
minuto_inicial = int(input("Informe o minuto inicial: "))
#etapa1
km_1 = int(input("Quantos km na etapa 1: "))
mvel_1 = int(input("Em quantos minutos na etapa 1: "))
svel_1 = int(input("Em quantos segundos na etapa 1: "))
tempo1 = km_1 * ((60*mvel_1) + svel_1)
#etapa2
km_2 = int(input("Quantos km na etapa 2: "))
mvel_2 = int(input("Em quantos minutos na etapa 2: "))
svel_2 = int(input("Em quantos segundos na etapa 2: "))
tempo2 = km_2 * ((60*mvel_2) + svel_2)
#etapa3
km_3 = int(input("Quantos km na etapa 3: "))
mvel_3 = int(input("Em quantos minutos na etapa 3: "))
svel_3 = int(input("Em quantos segundos na etapa 3: "))
tempo3 = km_3 * ((60*mvel_3) + svel_3)

tempo_total = tempo1+tempo2+tempo3#segundos
seg = horas_inicial * 3600
seg += (minuto_inicial * 60)
total_seg = seg + tempo_total#segundos
hora_final = total_seg//3600
resto = total_seg%3600
minuto_final = resto//60
segundo_final = resto%60

print(f"Você irá chegar as {hora_final}:{minuto_final}:{segundo_final} h")
