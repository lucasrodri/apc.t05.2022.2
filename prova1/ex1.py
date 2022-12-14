def loja(valorTotal,qtParcelas):
    if qtParcelas == 1:
        valor = valorTotal * 0.95
        valorParcela = valor/qtParcelas
        print(f"{valor:.2f} {valorParcela:.2f}")
    elif qtParcelas == 2:
        valor = valorTotal
        valorParcela = valor/qtParcelas
        print(f"{valor:.2f} {valorParcela:.2f}")
    elif qtParcelas == 3:
        valor = valorTotal * 1.05
        valorParcela = valor/qtParcelas
        print(f"{valor:.2f} {valorParcela:.2f}")
    elif qtParcelas == 4:
        valor = valorTotal * 1.1
        valorParcela = valor/qtParcelas
        print(f"{valor:.2f} {valorParcela:.2f}")


loja(150,4)
loja(200,3)
loja(45.60,1)