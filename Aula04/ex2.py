def minimo(a,b):
    if a < b:
        return a
    else:
        return b

p1,p2,p3,t1 = map(float,input().split())

mp = (p1 + (2*p2) + (3*p3)) / 6
mt = t1

mf = (0.6 * mp) + (0.4 * mt)

if mp < 5 or mt < 5:
    #mf = min(mf,4.9)
    mf = minimo(mf,4.9)

if mf == 0:
    print("SR")
elif mf < 3:
    print("II")
elif mf < 5:
    print("MI")
elif mf < 7:
    print("MM")
elif mf < 9:
    print("MS")
else:
    print("SS")

