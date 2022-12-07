#str -> ""
#int -> 2
#float -> 2.
#bool -> True or False

#x = 3
#x = 3.7
#x "L"
#x = True
"""
input() -> str
print() -> n argumentos, 2 argumentos ocultos importantes 'sep' e o 'end'

+
-
*
/
%
//
**
Raiz-> **(1/2)
"""
#int()
#float()
#str()
#bool()
#fstr -> f""


#b = int(input())
#h = (b**2 + b**2)**(1/2)
#area = (b*h)/2
#area = f"{area:.2f}"
#print(f"{area:.2f}")

#>
#<
#>=
#<=
#==
#!=
#b = 4<=5
#c = 5 != 6
#print(b, c)

#and or not
#print((b),(not c), (c and b), (c or b), (c or not b), (c and not b))

"""
if <cond>:
    <blk>
elif <cond>:
    <blk>
elif <cond>:
    <blk>
else:
    <blk>
print()
"""
"""
IMC = peso / (altura x altura).
Magreza
Normal
Sobrepeso
Obesidade grau I
Obesidade grau II
Obesidade grau III
"""
#peso = input("Qual é o seu peso: ")
#altura = input("Qual é o seu altura: ")
"""
peso, altura = input().split()#str
peso = float(peso)
altura = float(altura)
imc = peso / (altura**2)
#print(imc)
imc = 29.99
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Magreza'")
elif imc >= 18.5 and imc < 25:# 18.5 <= imc <= 24.9:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Normal'")
elif imc >= 25 and imc < 30:# 18.5 <= imc <= 24.9:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Sobrepeso'")
elif imc >= 30 and imc < 35:# 18.5 <= imc <= 24.9:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Obesidade grau I'")
elif imc >= 35 and imc < 40:# 18.5 <= imc <= 24.9:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Obesidade grau II'")
else:
    print(f"Seu IMC é {imc:.2f} e sua classificação é 'Obesidade grau III'")
"""
def func():
    #<blk>
    pass

def func2(a,b,c):
    print(a,b,c)

def func3(a,b,c):
    return a,b,c

#x = 3
#func2(x,x,x)
#print(func3(6,5,6))

def batata(base,altura=45):
    area = (base * altura) / 2
    area = f"{area:.2f}"
    return area
    
print(batata(7,3.54545353))
print(batata(7))
print(batata(7,altura=5))
    
    
    
    










