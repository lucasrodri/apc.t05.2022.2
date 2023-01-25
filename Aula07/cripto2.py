def encript1(frase,n,m):
    frase = frase[::-1]
    cript = ""
    for c in frase:
        if c.isalpha() and c.islower():
            cod = ord(c)
            cod += n
            cript += chr(cod)
        elif c.isalpha() and c.isupper():
            cod = ord(c)
            cod -= m
            cript += chr(cod)
        else:
            cript += c
    return cript

frase = input()
n,m = map(int, input().split())
print(encript1(frase,n,m))

