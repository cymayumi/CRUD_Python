import json

# script com um CRUD, bem simples usando toda lógica de programação, para trabalhar com um JSON presente em um arquivo txt.

# Ler todos os valores dentro do json
def lerJSON(arquivo):
    dados = json.load(arquivo)
    for usuario in dados:
        print("Nome: {}".format(usuario["nome"]))
        print("Celular: {}".format(usuario["celular"]))
        print("Email: {}\n".format(usuario["email"]))


# Ler conteúdo específico dentro do json
def lerEspecifico(arquivo, nome):
    dados = json.load(arquivo)
    for usuario in dados:
        if usuario["nome"] == nome:
            print("Olá {}, sua ficha é: ".format(nome))
            print("Nome: {}".format(usuario["nome"]))
            print("Celular: {}".format(usuario["celular"]))
            print("Email: {}\n".format(usuario["email"]))


# Add nova entrada no json
def addJSON(arquivo):
    usuario = {"nome": input("Digite seu nome: "), "celular": input("Digite seu celular: "),
               "email": input("Digite seu email: ")}

    dados = json.load(arquivo)
    dados.append(usuario)
    final = json.dumps(dados)
    arq = open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios", "w")
    arq.write(final)


# Deleta conteúdo específico no json
def deletarJSON(arquivo, nome):
    dados = json.load(arquivo)
    for index, usuario in enumerate(dados):
        if usuario["nome"] == nome:
            dados.pop(index)

    final = json.dumps(dados)
    arq = open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios", "w")
    arq.write(final)


# Update de um determinado elemento no json
def updateJSON(arquivo, nome):
    dados = json.load(arquivo)
    for index, usuario in enumerate(dados):
        if usuario["nome"] == nome:
            dados.pop(index)

    user = {"nome": input("Digite seu nome: "), "celular": input("Digite seu celular: "),
            "email": input("Digite seu email: ")}

    dados.append(user)
    final = json.dumps(dados)
    arq = open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios", "w")
    arq.write(final)
