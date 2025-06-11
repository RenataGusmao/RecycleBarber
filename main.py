import login
import coleta
import server

usuario = None
rodando = True

def voltar():
    input("Pressione Enter para voltar.\n")

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
            usuario = login.login()
        elif opt == "2":
            usuario = login.cadastrar()
        else:
            print("Saindo...")
            rodando = False
            break
            
    while usuario:
        if usuario.usertype == "usuario":
            print(f"Olá, {usuario.username}!")
            print("Você está logado como um barbeiro.")
            print()
            print("------------------")
            print("Selecione uma opção:")
            print("1 - Agendar uma nova coleta.")
            print("2 - Ver histórico de coletas.")
            print("3 - Mostrar perfil.")
            print("4 - Sair.")
            print("------------------")
            
            opt = input("")

            if opt == "1":
                try:
                    usuario.coletas.append(coleta.solicitar_coleta(usuario.cpf))
                except:
                    print("Ocorreu um erro inesperado, tente novamente.")
                else:
                    print("Coleta agendada com sucesso!")
                    voltar()
            elif opt == "2":
                if len(usuario.coletas) > 0 or len(usuario.coletas_realizadas) > 0:
                    for i in usuario.coletas:
                        coleta.mostrar_coleta(i,"usuario")
                    for i in usuario.coletas_realizadas:
                        coleta.mostrar_coleta(i,"usuario")
                else:
                    print("Você ainda não agendou nenhuma coleta!")
                voltar()
            elif opt == "3":
                login.mostrar_perfil(usuario)
                voltar()
            else:
                usuario = None
                break
        
        else:
            print(f"Olá, {usuario.username}!")
            print("Você está logado como parceiro de coleta.")
            print()
            print("------------------")
            print("Selecione uma opção:")
            print("1 - Ver pedidos de coleta por usuários.")
            print("2 - Consultar coletas aceitas.")
            print("3 - Ver histórico de coletas.")
            print("4 - Mostrar perfil.")
            print("5 - Sair.")
            print("------------------")
            
            opt = input("")
            
            if opt == "1":
                if len(server.coletas) > 0:
                    for i in server.coletas: 
                        print(f"- Coleta #{server.coletas.index(i) + 1}:")
                        coleta.mostrar_coleta(i,"coleta")   
                    coleta_selecionada = input("\nSelecionar uma coleta?\n(Digite o índice da coleta para selecionar. Digite qualquer coisa além do índice para sair.)")
                    
                    if coleta_selecionada.isdigit():
                        try:
                            usuario.coletas.append(server.coletas[int(coleta_selecionada) - 1])
                        except:
                            print("Não foi possível achar esse pedido de coleta.\nPor favor, tente novamente.")
                        else:
                            server.coletas.pop(int(coleta_selecionada) - 1)
                            print(f"Coleta #{coleta_selecionada} selecionada!")
                else:
                    print("Não há coletas pendentes agora!")
                voltar()
            elif opt == "2":
                if len(usuario.coletas) > 0:
                    for i in usuario.coletas:
                        print(f"- Coleta #{usuario.coletas.index(i) + 1}:")
                        coleta.mostrar_coleta(i,"coleta")
                    coleta_selecionada = input("\nSelecionar uma coleta?\n(Digite o índice da coleta para selecionar. Digite qualquer coisa além do índice para sair.)")
                    if coleta_selecionada.isdigit():
                        try:
                            coleta.mostrar_coleta(usuario.coletas[int(coleta_selecionada) - 1],"coleta")
                        except:
                            print("Não foi possível achar essa coleta.\nPor favor, tente novamente.")
                        else:
                            realizar = input("Deseja realizar essa coleta? (S/N)")
                            if realizar.lower() == "s":
                                coleta.realizar_coleta(usuario.coletas[int(coleta_selecionada) - 1],usuario)
                else:
                    print("Você ainda não aceitou nenhuma coleta!")
                    voltar()
            elif opt == "3":
                if len(usuario.coletas) > 0 or len(usuario.coletas_realizadas) > 0:
                    for i in usuario.coletas:
                        coleta.mostrar_coleta(i,"coleta")
                    for i in usuario.coletas_realizadas:
                        coleta.mostrar_coleta(i,"coleta")
                else:
                    print("Você ainda não finalizou nenhuma coleta!")
                voltar()
            elif opt == "4":
                login.mostrar_perfil(usuario)
                voltar()
            else:
                usuario = None
                break