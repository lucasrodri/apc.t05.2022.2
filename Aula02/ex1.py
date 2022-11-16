def desconto(nome,valor):
    #valorDesconto = (valor*9)/100
    #novoValor = valor - valorDesconto
    novoValor = valor*0.91
    print(f"O valor do {nome} com desconto é: {novoValor:.2f} R$")

produto = input()
valor = float(input())
desconto(produto,valor)