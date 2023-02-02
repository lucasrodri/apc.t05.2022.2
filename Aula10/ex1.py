#{n:{"Nome":nome,"Notas":[notas]}}
alunos = {}

with open("alunos.txt", 'r') as file:
    linha = file.readline()
    while linha:
        n,nome = linha.split()
        alunos[n] = {"Nome":nome}
        linha = file.readline()

with open("notas.txt", 'r') as file:
    linha = file.readline()
    while linha:
        n,p1,p2,p3,p4 = linha.split()
        p1,p2,p3,p4 = map(float,[p1,p2,p3,p4])
        alunos[n]["Notas"] = [p1,p2,p3,p4]
        alunos[n]["Media"] = (p1 + p2 + p3 + p4)/4
        linha = file.readline()

#print(alunos)
entrada = input()
if entrada.isnumeric():
    if entrada in alunos:
        print(f"O aluno chamado {alunos[entrada]['Nome']} tem as notas:",*alunos[entrada]["Notas"])
        print(f"A media do {alunos[entrada]['Nome']} é {alunos[entrada]['Media']:.2f}")
    else:
        print("Aluno não encontrado")
else:
    #Quico -> n
    numero = -1
    for n,d in alunos.items():
        if d["Nome"] == entrada:
            numero = n
            break
            
    if numero in alunos:
        print(f"O aluno chamado {alunos[numero]['Nome']} tem as notas:",*alunos[numero]["Notas"])
        print(f"A media do {alunos[numero]['Nome']} é {alunos[numero]['Media']:.2f}")
    else:
        print("Aluno não encontrado")

