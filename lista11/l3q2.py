
arquivo = open("frase.txt", "r")

conteudo = arquivo.read()

num_caracteres = len(conteudo)

print("Número de caracteres:", num_caracteres)

arquivo.close()
