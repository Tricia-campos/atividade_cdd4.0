qnt = int(input("Quantos alunos são? "))
aluno = 0
soma = 0
while aluno < qnt:
    nota = (float(input(f"Digite a nota: ")))
    aluno += 1
    soma = soma + nota
media = soma / qnt

print(f"{media: .2f}")