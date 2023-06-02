
medias = []

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    medias.append(media)

contador = 0
for media in medias:
    if media >= 7.0:
        contador += 1

print("Número de alunos com média maior ou igual a 7.0:", contador)
