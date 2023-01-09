import random # módulo random
numero = random.randrange(1, 101) # número entre 1 e 100
palpites = 1
flag = True
meu_palpite = int(input("Adivinhe meu número entre 1 e 100: "))
while meu_palpite != numero:
    palpites = palpites + 1
    if meu_palpite > numero:
        print(meu_palpite, "está acima.")
    elif meu_palpite < numero:
        print(meu_palpite, "está abaixo.")
    meu_palpite = int(input("tente novamente: "))
    if meu_palpite == 0:
        flag = False
        palpites = palpites -1
        break 
if flag:
    print("\nÓtimo, você acertou em", palpites, "tentativas!")
else:
    print("\nVocê desistiu em", palpites, "tentativas!")
    
    
    