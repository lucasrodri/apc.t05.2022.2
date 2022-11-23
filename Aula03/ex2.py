#MDC(x, y) = MDC(x − y, y), se x > y
#MDC(x,y) = MDC(y,x)
#MDC(x,x) = x

def mdc(x,y):
    if x == y:
        return x
    if x < y:#garantir que x > y
        aux = x
        x = y
        y = aux
        #ou
        #x,y = y,x
    if x > y:
        return mdc(x-y,y)
    else:#não vai entrar nunca por causa da linha 8
        return mdc(y,x)

print(mdc(12,36))