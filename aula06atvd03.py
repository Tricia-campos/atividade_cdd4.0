#1=1x 2=2x 3=3x ...

nmr = int(input("Digite um numero: "))
for i in range(1,nmr+1):
    for z in range(1, i+1):
        print(i, end="")