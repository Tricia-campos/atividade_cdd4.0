
print("RECIBO")
cliente = input("Digite seu nome: ")
produto = input("Com o que você vai abastecer E (etanol) ou G (gasolina)")
litros = (float(input(f"Quantos litros de {produto} você vai abastecer ")))

if produto == "E" or produto == "e":
    resultado1 = litros *  4.10
    print(f"O {cliente} abasteceu com {litros} de etanol o total foi:{resultado1}")
elif produto == "G" or produto == "g":
    resultado2 = litros * 5.8
    print(f"O {cliente} abasteceu com {litros} gasolina o total foi:{resultado2}")
else:
    print("invalido")




