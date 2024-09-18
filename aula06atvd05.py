#1=1x 2=2x 3=3x ...#quebrar linhas #add 0

nmr = int(input("Digite um numero: "))
for i in range(0,nmr+1):
    for z in range(0,i+1):
        print(z,end=" ")
    print()