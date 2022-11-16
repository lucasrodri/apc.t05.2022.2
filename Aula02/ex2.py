def desconto(nome,valor,desc):
    valorDesconto = (valor*desc)/100
    novoValor = valor - valorDesconto
    print(f"O valor do {nome} com desconto é: {novoValor:.2f} R$")

produto = input()
valor = float(input())
desc = float(input())
desconto(produto,valor,desc)
