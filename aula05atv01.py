
aluno = int(input("Quantos alunos há na sala? "))
soma = 0
for i in range (aluno):
    nota = float(input("Qual nota dos alunos? "))
    soma = soma + nota
media = soma/ aluno

print(f"{media:.2f}")