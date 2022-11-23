valor, parcelas = input().split()
valor = float(valor)
parcelas = int(parcelas)

if parcelas == 1:
    valorFinal = valor * 0.95
    valorParcela = valorFinal/parcelas
    print(f"{valorFinal:.2f} {valorParcela:.2f}")
elif parcelas == 2:
    valorFinal = valor * 1
    valorParcela = valorFinal/parcelas
    print(f"{valorFinal:.2f} {valorParcela:.2f}")
elif parcelas == 3:
    valorFinal = valor * 1.05
    valorParcela = valorFinal/parcelas
    print(f"{valorFinal:.2f} {valorParcela:.2f}")
elif parcelas == 4:
    valorFinal = valor * 1.1
    valorParcela = valorFinal/parcelas
    print(f"{valorFinal:.2f} {valorParcela:.2f}")