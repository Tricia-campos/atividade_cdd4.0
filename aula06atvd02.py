
dnv = 0
while dnv !=2:
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 <0 or nota1 >10:
        nota1 = float(input("Digite um numero entre 0 e 10: "))
        nota1 > 0 or nota1 < 10

    nota2 = float(input("Digite a segunda nota: "))

    while nota2 <0 or nota2 >10:
        nota2= float(input("Digite um numero entre 0 e 10: "))
        nota2 > 0 or nota2 < 10
    media = (nota1+nota2)/2
    print(f"a media é: {media}")

    dnv = int(input("Quer tentar mais uma vez? (1- sim / 2- não)"))
print("até logo!")