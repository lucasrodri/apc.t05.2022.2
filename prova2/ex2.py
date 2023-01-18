def brilha(branco,preto):
    print("☆" * branco + "★" * preto)
    if branco != 0:
        brilha(branco-1,preto+1)
        print("☆" * branco + "★" * preto)
