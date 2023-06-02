
numeros_favoritos = {}

for i in range(5):
    nome = input("Informe o nome da pessoa: ")
    numero_favorito = input("Informe o número favorito dessa pessoa: ")
    numeros_favoritos[nome] = numero_favorito

for pessoa, numero in numeros_favoritos.items():
    print(pessoa, ":", numero)
