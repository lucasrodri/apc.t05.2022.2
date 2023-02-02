#{nome:[Mbytes,percentual]}
dd = {}

with open("usuarios.txt", 'r') as file:
    nome,b = file.readline().split()
    while nome:
        mbytes = int(b)/10**6
        percentual = (mbytes*100)/(500*1000)
        dd[nome] = [mbytes,percentual]
        try:
            nome,b = file.readline().split()
        except:
            break 


with open("relatorio.txt", 'w') as file:
    total = 0
    for key,value in dd.items():
        nome = key
        mbytes = value[0]
        total += mbytes
        percentual = value[1]
        file.write(f"{nome}/{mbytes}/{percentual:.2f}\n")
    percentual = (total*100)/(500*1000)
    file.write(f"Total utilizado do disco (Megabytes): {total}\n")
    file.write(f"Total utilizado do disco (%): {percentual:.2f}")
