alunos = {}
#mat: dict("Nome":"","Provas":[0,0,0])

n = int(input())
for i in range(n):
    mat = input("Informe a matricula: ")
    nome = input("Informe o nome: ")
    p1 = float(input("Informe a nota da p1: "))
    p2 = float(input("Informe a nota da p2: "))
    p3 = float(input("Informe a nota da p3: "))
    if mat not in alunos:
        alunos[mat] = {"Nome": nome, "Provas": [p1,p2,p3]}

print(f"Matricula\tNome\tP1\tP2\tP3\tMédia")
for key, value in alunos.items():
    media = (value['Provas'][0] + value['Provas'][1] + value['Provas'][2]) / 3
    print(f"{key}\t{value['Nome']}\t{value['Provas'][0]}\t{value['Provas'][1]}\t{value['Provas'][2]}\t{media:.2f}")
    

    
