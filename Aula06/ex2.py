"""
4
X Y Z W
X D 3 # Y Z W X
Y D 1 # Z Y W X
W E 1 # Z W Y X
Z E 0 # Z W Y X
W E 1 # W Z Y X
"""
nbrinquendos = int(input())
prateleira = input().split()

prateleiraInicial = prateleira[:]

for i in range(5):
    brinquedo,direcao,deslocamento = input().split()
    deslocamento = int(deslocamento)
    index = prateleira.index(brinquedo)
    #del prateleira[index]
    prateleira.remove(brinquedo)
    if direcao == "D":
        posicao = index + deslocamento
        prateleira.insert(posicao,brinquedo)
    else:
        posicao = index - deslocamento
        prateleira.insert(posicao,brinquedo)
    
#X Y Z W
#W Z Y X
cont = 0
for i in range(nbrinquendos):
    if prateleira[i] != prateleiraInicial[i]:
        cont += 1

print(cont)


