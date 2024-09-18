dnv = 1
while dnv != 2:
    nmr = int(input("Digite um numero: "))
    if nmr > 0:
        print(f"{nmr} é positivo!")
    else:
        print(f"{nmr} é negativo!")
    if nmr %2 !=0:
        print(f"{nmr} é impar!")
    else:
        print(f"{nmr} é par!")
    dnv = int(input("Quer tentar mais uma vez? (1- sim / 2- não)"))
print("até logo!")