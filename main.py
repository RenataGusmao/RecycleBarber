import login
import coleta
import server

usuario = None # usuario cadastrado no momento
rodando = True

def voltar(): # função para deixar a mensagem de voltar consistente
    input("Pressione Enter para voltar.\n")

while rodando: # loop principal
    while usuario == None: # enquanto não tiver usuario (deslogado), executar esse loop
        print("Seja bem-vindo ao Recycle Barber.")
        print("------------------")
        print("Selecione uma opção:")
        print("1 - Entrar com sua conta.")
        print("2 - Não tem conta? Cadastre-se.")
        print("3 - Sair.")
        print("------------------")
        
        opt = input("") # escolha do usuário

        if opt == "1":
            usuario = login.login()
        elif opt == "2":
            usuario = login.cadastrar()
        else:
            print("Saindo...")
            rodando = False # setar o rodando para false quebra o loop principal
            break
            
    # loop principal, após fazer login
    while usuario: # enquanto tiver um usuario logado, executar esse loop
        if usuario.usertype == "usuario": # loop para usuários (barbeiros e profissionais de beleza)
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
            
            opt = input("") # escolha do usuário

            if opt == "1":
                try: # tenta agendar uma coleta
                    usuario.coletas.append(coleta.solicitar_coleta(usuario.cpf))
                except: # se em algum lugar houver um erro, executa isso
                    print("Ocorreu um erro inesperado, tente novamente.")
                else: # se não, exceuta isso
                    print("Coleta agendada com sucesso!")
                    voltar()
            elif opt == "2":
                # se qualquer uma dessas duas listas não estiver vazia, rodar:
                if len(usuario.coletas) > 0 or len(usuario.coletas_realizadas) > 0:
                    for i in usuario.coletas:
                        coleta.mostrar_coleta(i,"usuario")
                    for i in usuario.coletas_realizadas:
                        coleta.mostrar_coleta(i,"usuario")
                else: # se não:
                    print("Você ainda não agendou nenhuma coleta!")
                voltar()
            elif opt == "3":
                login.mostrar_perfil(usuario)
                voltar()
            else:
                usuario = None
                break
        
        else: # loop para parceiros de coleta
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
            
            opt = input("") # escolha do usuário
            
            if opt == "1":
                if len(server.coletas) > 0: # se tiver pedidos de coleta no servidor
                    for i in server.coletas: 
                        print(f"- Coleta #{server.coletas.index(i) + 1}:") # printa os pedidos acompanhados de um índice
                        coleta.mostrar_coleta(i,"coleta")
                    # entrada do usuário:    
                    coleta_selecionada = input("\nSelecionar uma coleta?\n(Digite o índice da coleta para selecionar. Digite qualquer coisa além do índice para sair.)")
                    
                    if coleta_selecionada.isdigit(): # verifica se o usuário entrou um número
                        try: # tenta adicionar a coleta na lista do servidor ao perfil do coletador
                            usuario.coletas.append(server.coletas[int(coleta_selecionada) - 1])
                        except: # caso o coletador erre o índice
                            print("Não foi possível achar esse pedido de coleta.\nPor favor, tente novamente.")
                        else:
                            server.coletas.pop(int(coleta_selecionada) - 1) # retira a coleta do servidor
                            print(f"Coleta #{coleta_selecionada} selecionada!")
                    # se o coletador não entra um índice, automaticamente pula
                else: # se não
                    print("Não há coletas pendentes agora!")
                voltar()
            elif opt == "2":
                if len(usuario.coletas) > 0: # verificar apenas se há itens na lista de coletas ativas
                    for i in usuario.coletas:
                        print(f"- Coleta #{usuario.coletas.index(i) + 1}:") # printa os pedidos acompanhados de um índice
                        coleta.mostrar_coleta(i,"coleta")
                    # entrada do usuário:
                    coleta_selecionada = input("\nSelecionar uma coleta?\n(Digite o índice da coleta para selecionar. Digite qualquer coisa além do índice para sair.)")
                    if coleta_selecionada.isdigit(): # verifica se o usuário entrou um número
                        try: # tenta selecionar uma coleta
                            coleta.mostrar_coleta(usuario.coletas[int(coleta_selecionada) - 1],"coleta")
                        except: # caso o índice esteja fora de alcance
                            print("Não foi possível achar essa coleta.\nPor favor, tente novamente.")
                        else:
                            realizar = input("Deseja realizar essa coleta? (S/N)")
                            if realizar.lower() == "s": # se sim, finaliza a coleta
                                coleta.realizar_coleta(usuario.coletas[int(coleta_selecionada) - 1],usuario)
                else:
                    print("Você ainda não aceitou nenhuma coleta!")
                    voltar()
            elif opt == "3":
                # mostra tanto coletas ativas quanto as que foram realizadas, nessa ordem
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