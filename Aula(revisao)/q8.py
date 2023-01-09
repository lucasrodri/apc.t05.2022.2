n = int(input())

while n > 0:
    num = ""
    letra = ""
    final = ""
    flag = False
    msg = input()
    for c in msg:
        if not c.isnumeric():
            if flag:
                final += letra * int(num)
                num = ""
            
            letra = c
            flag = True
            
        else:
            num += c
    final += letra * int(num)
    print(final)
    n -= 1
    
    