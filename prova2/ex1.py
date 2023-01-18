i,f = map(int,input().split(","))
if i > f:
    i,f = f,i
qt = f-i
for step in range(1,qt+1): 
    for n in range(i,f+1,step):
        print(n,end=" ")
    print()