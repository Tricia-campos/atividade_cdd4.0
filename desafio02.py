#senha, 3 tentativas, senha bloqueada

senha = 3184
x = 0
tent = 3
usuario = int(input("Digite a senha de 4 digitos: "))

while usuario != senha and tent > 1:
    tent -= 1
    if tent > 0:
        print(f"Senha incorreta. Você tem {tent} tentativa(s) restante(s).")
        usuario = int(input("Tente mais uma vez: "))
    else:
        print("Número bloqueado")


if usuario == senha:
    print("aprovado")


