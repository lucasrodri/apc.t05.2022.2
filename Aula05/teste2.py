a = int(input())
b = int(input())

if b > 0:
    r = 1
    for n in range(b):
        r = r * a
    print(r)
else:
    r = 1
    for n in range(b*-1):
        r = r / a
    print(r)
