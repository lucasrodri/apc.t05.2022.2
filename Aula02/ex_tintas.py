def calcula(area,valor,volume):
    #1 litro para cada 6 metros quadrados
    litros = (area*1.1)/6
    qt = litros//volume
    restoQt = litros%volume
    if restoQt != 0:
        qt = qt + 1
    #print(f"O valor total é: {qt*valor:.2f} R$")
    return qt*valor

def melhorcusto(area):
    volumeLata = 18
    valorLata = 80
    volumeGalao = 3.6
    valorGalao = 25
    litros = (area*1.1)/6
    latas = litros//volumeLata
    restoLitros = litros%volumeLata
    galao = restoLitros//volumeGalao
    resto = restoLitros%volumeGalao
    if resto != 0:
        galao += 1
    if galao == 4:
        galao = 0
        latas += 1
    return latas*valorLata + galao*valorGalao

area = float(input("Informe o valor da area: "))
print(f"Comprando apenas Latas o valor será {calcula(area,80,18):.2f} R$")
print(f"Comprando apenas Galões o valor será {calcula(area,25,3.6):.2f} R$")
print(f"Comprando no melhor custo o valor será {melhorcusto(area):.2f} R$")



