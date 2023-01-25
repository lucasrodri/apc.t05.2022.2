n = int(input())

dd = {}

for i in range(n):
    arquivo,t1,t2,t3,t4 = input().split()
    dd[arquivo] = t1,t2,t3,t4

tags = input().split() #list
saida = []

for key,value in dd.items():
    for tag in tags:
        if tag in value:
            if key not in saida:
                saida.append(key)
                
print("\n".join(saida))

