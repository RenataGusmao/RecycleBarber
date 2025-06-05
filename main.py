import login
import coleta

usuario = None
rodando = True

while rodando:
    while usuario == None:
        print("Seja bem-vindo ao Recycle Barber.")
        print("------------------")
        print("Selecione uma opção:")
        print("1 - Entrar com sua conta.")
        print("2 - Não tem conta? Cadastre-se.")
        print("3 - Sair.")
        print("------------------")
        
        opt = input("")

        if opt == "1":
            pass
        elif opt == "2":
            try:
                usuario = login.cadastrar()
            except:
                print("Ocorreu um erro inesperado, tente se cadastrar novamente.")
        else:
            print(rodando)
            rodando = False
            break
            
            
    # loop principal, após fazer login
    while usuario:
        print(f"Olá, {usuario.username}!")
        print()
        print("------------------")
        print("Selecione uma opção:")
        print("1 - Agendar uma nova coleta.")
        print("2 - Ver histórico de coletas.")
        print("3 - Trocar pontos.")
        print("4 - Mostrar perfil.")
        print("5 - Sair.")
        print("------------------")
        
        opt = input("")

        if opt == "1":
            try:
                usuario.coletas.append(coleta.solicitar_coleta(usuario))
            except:
                print("Ocorreu um erro inesperado, tente novamente.")
            else:
                print("Coleta agendada com sucesso!")
                input("Pressione para voltar.\n")
        elif opt == "2":
            if len(usuario.coletas) > 0:
                for i in usuario.coletas:
                    coleta.mostrar_coleta(i)
            else:
                print("Você ainda não agendou nenhuma coleta!")
            input("Pressione Enter para voltar.\n")
        elif opt == "3":
            pass
        elif opt == "4":
            login.mostrar_perfil(usuario)
            input("Pressione Enter para voltar.\n")
        else:
            usuario = None
            break