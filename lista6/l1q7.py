class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

usuarios = []

def cadastrar_usuario():
    print("Cadastro de Usuário")
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")

    usuario = Usuario(nome, idade, email)
    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("Lista de Usuários")
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, Idade: {usuario.idade}, Email: {usuario.email}")

while True:
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
