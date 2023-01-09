n = int(input())
anterior = int(input())
indicadora = False

for i in range(n-1):
    atual = int(input())
    if atual == anterior:
        indicadora = True
    anterior = atual

if indicadora:
    print("sim")
else:
    print("não")
        
    