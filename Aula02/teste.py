"""
O retorno feito na própria função e não.
Função com entrada e sem entrada
Questão da indentação
Como vai funcionar no CodeRunner: Em muitos exercícios basta enviar a função
def nome_função(entradas)
<código>
"""

def f1(a,b=4):
    print(a+b)
    return a+b

def lucas():
    pass
      

a = f1(6)
print(a)
a = f1(6,90)
print(a)
