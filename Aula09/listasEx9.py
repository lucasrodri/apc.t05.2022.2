def ler(linhas,colunas):
    sala = []
    for _ in range(linhas):
        sala.append(input().split())
    return sala

def contaEsquerda(index,fileira):
    cont = 0
    if index == 0:
        return float("inf")
    else:
        for i in range(index-1,-1,-1):
            cont += 1
            if fileira[i] == "1":  
                return cont
        return cont

def contaDireita(index,fileira):
    cont = 0
    if index == len(fileira)-1:
        return float("inf")
    else:
        for i in range(index+1,len(fileira)):
            cont += 1
            if fileira[i] == "1":  
                return cont
        return cont


linhas,colunas = map(int,input().split())
sala = ler(linhas,colunas)
maior = 0
for fileira in sala:
    for i in range(colunas):
        if fileira[i] == "0":
            e = contaEsquerda(i,fileira)
            d = contaDireita(i,fileira)
            if min(e,d) > maior:
                maior = min(e,d)
print(maior)
    
