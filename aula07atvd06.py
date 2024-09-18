peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print(f"seu imc é {imc:.2f} você está abaixo do peso")
elif imc <= 24.9:
    print(f"seu imc é {imc:.2f} você está no peso ideal")
elif imc <= 29.9:
    print(f"seu imc é {imc:.2f} você está levemente acima do peso")
elif imc <= 34.9:
    print(f"seu imc é {imc:.2f} você está com obesidade grau I")
elif imc <= 39.9:
    print(f"seu imc é {imc:.2f} você está com obesidade grau II")
elif imc >= 40.0:
    print(f"seu imc é {imc:.2f} você está obeso")