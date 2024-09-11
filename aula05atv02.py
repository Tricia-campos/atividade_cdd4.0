aluno = 0
soma = 0
while aluno < 10:
    nota =(float(input(f"Digite a nota: ")))
    aluno += 1
    soma = soma + nota
media = soma / aluno

print(f"{media:.2f}")