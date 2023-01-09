nome,salario = input().split(",")
salario = float(salario)
menor = salario
nomeMenor = nome

if nome == "Fim":
    print("Não tem")
else:
    while nome != "Fim":
        nome,salario = input().split(",")
        salario = float(salario)
        if nome != "Fim":
            if menor > salario:
                menor = salario
                nomeMenor = nome

    print(f"{nomeMenor}")
