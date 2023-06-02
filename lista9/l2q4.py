# Lista de idades e alturas dos alunos
idades = []
alturas = []

# Obtendo as idades e alturas dos alunos
for i in range(30):
    idade = int(input(f"Informe a idade do aluno {i+1}: "))
    altura = float(input(f"Informe a altura do aluno {i+1}: "))

    idades.append(idade)
    alturas.append(altura)

# Calculando a média de altura dos alunos com mais de 13 anos
soma_alturas = sum(alturas)
media_alturas = soma_alturas / len(alturas)

# Contando quantos alunos com mais de 13 anos possuem altura inferior à média
contador = 0
for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media_alturas:
        contador += 1

print("Número de alunos com mais de 13 anos e altura inferior à média:", contador)
51
