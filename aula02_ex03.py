time1 = input("Digite o nome do seu time 1: ")
pontos1 = int(input(f"Digite o número de gols  {time1} "))
time2 = input("Digite o nome do time 2: ")
pontos2 = int(input(f"Digite o número de gols {time2} "))

if pontos1 == pontos2:
    print(" os times", time1,"e", time2, "empataram")
elif pontos1 > pontos2:
    print("O", time1, " é o vencedor" )
else:
    print("o", time2, "é o vencedor")
