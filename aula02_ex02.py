aluno = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3
print(aluno, "Sua media é: ",media)

if media >= 7:
    print(aluno, ", você esta aprovado!!")
elif media >=4:
    print(aluno, ", você esta de recuperação!")
else:
    print(aluno, ", Você esta reprovado!")
