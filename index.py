import funcoes

sair = 0

while sair != 6:
    print("\033[35m-=-=-=-=-=-=-=-=-=-  MENU USUÁRIOS  -=-=-=-=-=-=-=-=-=-\n\033[m")
    menu = int(input("1 - Adicionar usuário "
                     "\n2 - Localizar usuário "
                     "\n3 - Atualizar cadastro já existente "
                     "\n4 - Deletar cadastro "
                     "\n5 - Imprimir relação de cadastros "
                     "\n6 - Sair "
                     "\nDigite a sua opção: "))
    print("-=-" * 20)

    if menu == 1:
        with open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios") as arquivo:
            funcoes.addJSON(arquivo)
    elif menu == 2:
        nome = input("Digite o nome do usuário que deseja buscar: ")
        with open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios") as arquivo:
            funcoes.lerEspecifico(arquivo, nome)
    elif menu == 3:
        nome = input("Digite o nome do usuário que deseja atualizar o cadastro: ")
        with open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios") as arquivo:
            funcoes.updateJSON(arquivo, nome)
    elif menu == 4:
        nome = input("Digite o nome do usuário que deseja deleter o cadastro: ")
        with open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios") as arquivo:
            funcoes.deletarJSON(arquivo, nome)
    elif menu == 5:
        with open(r"C:\Users\admin\Desktop\PROJETOS\CRUD_python\json_usuarios") as arquivo:
            funcoes.lerJSON(arquivo)
    elif menu == 6:
        break
