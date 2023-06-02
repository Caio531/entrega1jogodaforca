
arquivo = open("frase.txt", "a+")
novo_texto = "\nUMA VEZ FLAMENGO SEMPRE FLAMENGOOOO, somos uma naçãaao sempre estarei contigooooo, dale dale dale ooooohhhhhhhh"
arquivo.write(novo_texto)
arquivo.seek(0)
novo_conteudo = arquivo.read()
print("Novo conteúdo:")
print(novo_conteudo)
arquivo.close()
