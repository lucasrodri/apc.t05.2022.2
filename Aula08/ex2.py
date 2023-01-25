n = int(input())

dd = {}

for i in range(n):
    problema,solucao,dificuldade = input().split()
    dd[problema] = solucao,dificuldade
    
#print(dd)

def ordenaEx(elem):
    #print(elem[0])# voldemort_imortal
    #print(elem[1])# ('reliquias_da_morte', '8')
    return int(elem[1][1])

string = ''
#print(sorted(dd.items(),key=ordenaEx,reverse=True))
for chave,valor in sorted(dd.items(),key=ordenaEx,reverse=True):
    #print(chave,valor, sep=' ')
    string += valor[0]

print(string)