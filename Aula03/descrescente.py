#Escreva um programa que leia três números distintos e os imprima em
#ordem decrescente.

a,b,c = map(int,input().split())

if a > b and a > c:#a é o maior
    if b > c:#b segundo maior
        print(a,b,c)
    else:#c > b
        print(a,c,b)
else:#a não é o maior
    if b > c:#b é maior de todos
        if a > c:#c é o menor de todos
            print(b,a,c)
        else:#a é o menor de todos
            print(b,c,a)
    else:#c é o maior de todos
        if a > b:#b é o menor de todos
            print(c,a,b)
        else:#a é menor de todos
            print(c,b,a)

    