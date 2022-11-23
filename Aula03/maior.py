#Escreva um programa que leia três números e imprima o maior deles.

a,b,c = map(int,input().split())
"""
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
"""

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)