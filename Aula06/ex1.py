nfatias, premiada = input().split()
nfatias = int(nfatias)
premiada = int(premiada)

def criaBolo(nfatias, premiada):
    lista = []
    for i in range(nfatias):
        if i == premiada:
            lista.append(True)
        else:
            lista.append(False)
    return lista

#bolo = criaBolo(nfatias, premiada)
bolo = [False]*nfatias
bolo[premiada] = True


for i in range(nfatias):
    nome,fatia = input().split()
    fatia = int(fatia)
    if bolo[fatia] == True:
       ganhador = nome
    del bolo[fatia]

print(ganhador)
    
    
    