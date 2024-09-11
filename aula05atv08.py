
dnv=1
while dnv !=2:
    negativo = 0
    for i in range (10):
        valor =int(input("Digite um valor: "))
        if valor <0:
            negativo += 1
    print(f"Os numero negativos são {negativo}: ")

    dnv = int(input("Você quer tentar denovo? (1- sim//2- não): "))
print("finalizado!")
