dnv= 1
while dnv != 2:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    if a == b:
        c = a + b
        print(f"A soma de A e B é: {c}")
    else:
        c = a * b
        print(f"a multiplicação de A e B é: {c}")
    dnv = int(input("Deseja tentar mais uma vez? (1-sim/2-não)"))

print("até logo!")