#lista = []
#for i in range(5):
#    lista.append(i**2)
#print(lista)

#lista = [<exp> for i in <list>]
#lista = [i**2 for i in range(5)]
#print(lista)

lista = []
for i in range(5):
    if i % 2 == 0:
        lista.append(i**2)
    else:
        lista.append(i**3)
print(lista)

#lista = [<exp> for i in <list> if <cond>]
#lista = [i**2 for i in range(5) if i % 2 == 0 if i != 0]
#print(lista)

#lista = [<exp> for i in <list> if <cond> if <cond>]

#lista = [<exp> if <cond> else <exp2> for i in <list>]
lista = [i**2 if i % 2 == 0 else i**3 for i in range(5)]
print(lista)