def tempo(t,p,tfixo):
    if t == 0:
        print("Cabum!!!! Explodiu")
    elif t == 5:
        print("Seu tempo está acabando!")
        return tempo(t-1,p,tfixo)
    elif t == 1:
        if p >= tfixo:
            print("Bomba desativada automaticamente!")
        else:
            print("Seja rápido. Falta 1 segundo")
            return tempo(t-1,p,tfixo)
    else:
        print(f"Atenção faltam {t} segundos...")
        return tempo(t-1,p,tfixo)
    
t = int(input())
p = int(input())
tempo(t,p,t)