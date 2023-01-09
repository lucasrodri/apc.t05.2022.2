nome,salario = input().split(",")
salario = float(salario)
soma = 0
cont = 1
while nome != "Fim":
    soma = soma + salario
    nome,salario = input().split(",")
    salario = float(salario)
    if nome != "Fim":
        cont = cont + 1

media = soma/cont
print(f"{media:.2f}")