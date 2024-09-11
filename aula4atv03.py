numero = int(input(f"Digite qual tabuada você quer ver:"))

for i in range(1,11):
    tabuada = i * numero
    print(f"{i} x {numero} = {tabuada}")