def tempoJogo(hi, mi, hf, mf):
    t1 = hi * 60 + mi
    t2 = hf * 60 + mf
    t = t2 - t1
    if t == 0:
        h = 24
        m = 0
    else:
        if t < 0:
            t = t + 24*60
        h = t//60
        m = t%60
    print(f"O jogo durou {h} horas(s) e {m} minuto(s).")


hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
tempoJogo(hi, mi, hf, mf)