soma = 0
for numero in range(10):
    numero = int(input(f"Digite o {numero+1} numero: "))
    if numero % 2 != 0:
        soma = soma + numero
print(soma)