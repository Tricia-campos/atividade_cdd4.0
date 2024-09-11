###senha, 3 tentativas, SEnha blOqueada

senha = 3184


usuario = int(input("Digite a senha de 4 digitos: "))

for x in range(2):
    if usuario != senha:
        denovo = int(input("Tente mais uma vez:"))
else:
        print("BLOQUEADO!")