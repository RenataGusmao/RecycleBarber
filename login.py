import server

# objeto do usuário
class User:
    def __init__(self, cpf, nome_empresa, username, usertype, email, password, endereco):
        self.cpf = cpf
        self.nome_empresa = nome_empresa
        self.username = username
        self.usertype = usertype
        self.email = email
        self.password = password
        self.endereco = endereco
        self.coletas = []
        self.coletas_realizadas = []

# func para verificar o CPF
def verificar_cpf(cpf = str):
    try:
        cpf = cpf.replace(".","") # retira pontos da string, caso o usuário colocar
        cpf = cpf.replace("-","") # retira traços da string, caso o usuário colocar
        if len(cpf) != 11: raise Exception # um CPF tem 11 digitos, se não tiver, levanta uma exceção
        if not cpf.isdigit(): raise Exception # verifica se todos os caracters são digitos
    except:
        print("CPF inválido, tente novamente.")
    else:
        return cpf # retorna cpf como string

# login
def login(): # a fazer
    while True:
        cpf = verificar_cpf(input("Insira seu CPF: "))
        if cpf in server.usuarios_cadastrados: # se o CPF tiver cadastrado:
            usuario = server.usuarios_cadastrados[cpf] # procura o obj do usuario pela chave (CPF) 
            senha = input("Insira sua senha.")
            if senha == usuario.password: return usuario # se a senha for correta, retorna o obj de usuário
            else: print("Senha incorreta, tente novamente.")
        else: 
            print("O CPF não está cadastrado.")
            break

# cadastro
def cadastrar():
    while True: # loop para verificar se o CPF é válido
        cpf = verificar_cpf(input("Insira seu CPF: "))
        if cpf == None:
            pass
        else:
            break
    # se já estiver cadastrado, abortar cadastro
    if cpf in server.usuarios_cadastrados:
        print("CPF já cadastrado. Retornando...")
        return None
    
    nome_empresa = input("Nome da empresa: ")
    username = input("Nome do empresário: ")
    email = input("E-mail da empresa: ").lower() # converte o e-mail em letras minúsculas
    password = input("Insira a sua senha: ")
    
    confirm_password = "" # confirmação de senha
    while confirm_password != password:
        confirm_password = input("Confirme sua senha: ")
        if confirm_password != password: print("A senha entrada foi diferente.")
    
    endereco = {} # cria um dicionário vazio para guardar todas as informações do endereço
    endereco["UF"] = input("Estado: ")
    endereco["cidade"] = input("Cidade: ")
    endereco["bairro"] = input("Bairro: ")
    
    while True: # loop para verificar se o CEP é válido
        try:
            endereco["CEP"] = input("CEP: ") # mesma lógica de verificação do CPF
            endereco["CEP"] = endereco["CEP"].replace("-","")
            if len(endereco["CEP"]) != 8: raise Exception
            endereco["CEP"] = int(endereco["CEP"])
        except: 
            print("CEP inválido.")
        else: 
            break
    
    endereco["rua"] = input("Rua: ")
    endereco["numero"] = input("Número: ")
    endereco["complemento"] = input("(Opcional) Complemento: ")
    
    while True: # loop para assegurar que o usuario entre opção válida
        print("Você é...")
        print("1 - Usuário (Profissional de estética)")
        print("2 - Parceiro de coleta.")
        
        opt = input()
        if opt == "1":
            usertype = "usuario"
            break
        elif opt == "2":
            usertype = "coleta"
            break
        else:
            print("Entre uma opção valida.")

    # cria objeto de usuario
    new_user = User(cpf, nome_empresa, username, usertype, email, password, endereco) # cria objeto de usuário
    # cadastra o usuário no dicionário de usuarios cadastrados do servidor, usando CPF como chave
    server.usuarios_cadastrados[cpf] = new_user 
        
    print("Cadastro efetuado com sucesso! Efetuando login...\n")
    
    return new_user # retorna objeto de usuúario

def mostrar_perfil(usuario): # printa informações do usuário
    print("-----------")
    print(f"CPF cadastrado:\n{usuario.cpf}")
    print(f"Nome da empresa:\n{usuario.nome_empresa}")
    print(f"Nome do usuário:\n{usuario.username}")
    print(f"E-mail:\n{usuario.email}")
    print(f"Endereço:\n{usuario.endereco['rua']}, {usuario.endereco['numero']} {usuario.endereco['complemento']}")
    print(f"{usuario.endereco['CEP']}")
    print(f"{usuario.endereco['bairro']}, {usuario.endereco['cidade']}, {usuario.endereco['UF']}")