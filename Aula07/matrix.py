N = int(input())
n = N/2
if N % 2 != 0:
    n +=  0.5
n = int(n)
for i in range(N):
    for j in range(N):
        check = 0
        distx1 = j
        disty1 = i
        distx2 = (N - 1) - j
        disty2 = (N - 1) - i
        distance = min(distx1,distx2,disty1,disty2)
        print(n-distance,end=' ')
    print()
