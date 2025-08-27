import random

# Lista para armazenar o nome dos alunos
alunos = []

# Pede para o usuário digitar o nome dos 4 alunos
for i in range(4):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    alunos.append(nome)

# Embaralha a lista de alunos
random.shuffle(alunos)

# Mostra a ordem de apresentação
print("\nA ordem de apresentação é:")
for i, aluno in enumerate(alunos):
    print(f"{i+1}º - {aluno}")