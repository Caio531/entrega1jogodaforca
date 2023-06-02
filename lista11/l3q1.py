
arquivo = open("frase.txt", "w")

frase = "UMA VEZ FLAMENGO SEMPRE FLAMENGOOOO"
arquivo.write(frase)

arquivo.close()

arquivo = open("frase.txt", "r")
frase_lida = arquivo.read()
print(frase_lida)

arquivo.close()
