s = input()

tam = len(s)
cont = 0
par = False
if tam % 2 == 0:#par
    par = True
    a = s[:tam//2]
    b = s[tam//2:]
    b = b[::-1]
    for i in range(tam//2):
        if a[i] != b[i]:
            cont += 1

else:#impar
    a = s[:tam//2]
    b = s[(tam//2)+1:]
    b = b[::-1]
    for i in range(tam//2):
        if a[i] != b[i]:
            cont += 1
            
if par and cont == 1:
    print("ON")
elif not par and cont < 2:
    print("ON")
else:
    print("OFF")
