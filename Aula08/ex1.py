n = int(input())
        #x,y 
plano = (0,0)

for i in range(n):
    direcao,quadras = input().split()
    quadras = int(quadras)
    if direcao == "N":
        plano = plano[0], plano[1]+quadras
    elif direcao == "S":
        plano = plano[0], plano[1]-quadras
    elif direcao == "L":
        plano = plano[0]+quadras, plano[1]
    elif direcao == "O":
        plano = plano[0]-quadras, plano[1]

n,s = 0,0
l,o = 0,0
#plano = (-2, 3)
if plano[1] > 0:
    n = 0
    s = plano[1]
else:
    n = plano[1] * -1
    s = 0

if plano[0] > 0:
    l = 0
    o = plano[0]
else:
    l = plano[0] * -1
    o = 0
    

print(n,s,l,o)