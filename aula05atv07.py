
dnv=1
while dnv !=2:
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))

    while valor2 == 0:
        valor2 = int(input("Tente outro valor: "))

    dividir = valor1 /valor2
    print(f"o valor dividido é {dividir: .2f}: ")

    dnv = int(input("Você quer tentar denovo? (1- sim//2- não): "))


