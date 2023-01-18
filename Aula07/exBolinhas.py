def lerJogo(n):
    mat = []
    for i in range(n):
        mat.append(input().split())
    return mat
                       
def gravidade(mat):
    tam = len(mat)
    for i in range(tam-2,-1,-1):
        for j in range(tam):
            if mat[i][j] == "o":
                if mat[i+1][j] == ".":
                    mat[i+1][j] = "o"
                    mat[i][j] = "."
                    #mat[i][j],mat[i+1][j] = mat[i+1][j],mat[i][j]

def printMat(mat): 
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j],end=" ")
        print()

def copiaJogo(mat):
    jogo = []
    for linha in mat:
        jogo.append(linha[:])
    return jogo

def mudanca(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m1)):
            if m1[i][j] != m2[i][j]:
                return True
    return False

n = int(input())
mat = lerJogo(n)

cont = 0
mudou = True
while mudou:
    mat2 = copiaJogo(mat)
    gravidade(mat)
    cont += 1
    mudou = mudanca(mat,mat2)
    
#printMat(mat)
print(cont-1)



