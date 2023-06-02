import random

temas = {
    "times de futebol": ["barcelona", "real madrid", "manchester united"],
    "países": ["brasil", "alemanha", "frança"],
    "comidas": ["pizza", "hambúrguer", "sushi"]
}


def imprimir_forca(erros):
    partes_corpo = [
        """
           |
           |
           |
           |
           |
        --------
        """,
        """
           |      |
           |
           |
           |
           |
        --------
        """,
        """
           |      |
           |      O
           |
           |
           |
        --------
        """,
        """
           |      |
           |      O
           |     /|\\
           |
           |
        --------
        """,
        """
           |      |
           |      O
           |     /|\\
           |      |
           |
        --------
        """,
        """
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
        --------
        """
    ]
    print(partes_corpo[erros])


def imprimir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")


def escolher_tema():
    print("Escolha um tema:")
    for i, tema in enumerate(temas.keys()):
        print(f"{i+1}. {tema}")

    while True:
        escolha = input("Digite o número do tema escolhido: ")
        if escolha.isdigit() and int(escolha) in range(1, len(temas) + 1):
            tema_escolhido = list(temas.keys())[int(escolha) - 1]
            return tema_escolhido
        else:
            print("Opção inválida. Digite o número correspondente ao tema.")


def escolher_palavra(tema):
    palavras_tema = temas[tema]
    return random.choice(palavras_tema)


def jogar_forca():
    while True:
        tema = escolher_tema()
        palavra = escolher_palavra(tema)

        letras_erradas = []
        letras_corretas = []
        tentativas_maximas = 6

        while len(letras_erradas) < tentativas_maximas:
            imprimir_palavra(palavra, letras_corretas)

            if all(letra in letras_corretas for letra in palavra):
                print("Parabéns, você ganhou!")
                break

            if letras_erradas:
                print("Letras erradas:", " ".join(letras_erradas))

            letra = input("Digite uma letra: ").lower()

            if letra in letras_corretas or letra in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            if letra in palavra:
                letras_corretas.append(letra)
            else:
                letras_erradas.append(letra)
                imprimir_forca(len(letras_erradas))

        if len(letras_erradas) == tentativas_maximas:
            print("Você perdeu! A palavra era:", palavra)

        jogar_novamente = input("Deseja jogar novamente? (S/N): ").lower()
        if jogar_novamente == "n":
            break


jogar_forca()
