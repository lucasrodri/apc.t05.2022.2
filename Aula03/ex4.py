def ordena(a,b,c):
    #retornar a,b,c de forma decrescente
    if a > b and a > c:#a é o maior
        if b > c:#b segundo maior
            return a,b,c
        else:#c > b
            return(a,c,b)
    else:#a não é o maior
        if b > c:#b é maior de todos
            if a > c:#c é o menor de todos
                return(b,a,c)
            else:#a é o menor de todos
                return(b,c,a)
        else:#c é o maior de todos
            if a > b:#b é o menor de todos
                return(c,a,b)
            else:#a é menor de todos
                return(c,b,a)
    
a = float(input())
b = float(input())
c = float(input())

a,b,c = ordena(a,b,c)

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif a**2 == (b**2) + (c**2):
    print("TRIANGULO RETANGULO")
elif a == b and b == c and a == c:# a == b == c
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")