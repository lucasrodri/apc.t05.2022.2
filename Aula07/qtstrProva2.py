#i,f = map(int,input().split(","))
#if i > f:
#    i,f = f,i
#qt = f-i
#for step in range(1,qt+1): 
#    for n in range(i,f+1,step):
#        print(n,end=" ")
#    print()

i,f = map(int,input().split(","))
print("\n".join( [" ".join([str(n) for n in range(min(f,i),max(f,i)+1,step)])
                  for step in range(1,max(f,i)-min(f,i)+1)]))

