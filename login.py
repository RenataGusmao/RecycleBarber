import server

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

def verificar_cpf(cpf = str):
    try:
        cpf = cpf.replace(".","")
        cpf = cpf.replace("-","")
        if len(cpf) != 11: raise Exception
        if not cpf.isdigit(): raise Exception
    except:
        print("CPF inválido, tente novamente.")
    else:
        return cpf

def login():
    while True:
        cpf = verificar_cpf(input("Insira seu CPF: "))
        if cpf in server.usuarios_cadastrados:
            usuario = server.usuarios_cadastrados[cpf]
            senha = input("Insira sua senha.")
            if senha == usuario.password: return usuario
            else: print("Senha incorreta, tente novamente.")
        else: 
            print("O CPF não está cadastrado.")
            break

def cadastrar():
    while True:
        cpf = verificar_cpf(input("Insira seu CPF: "))
        if cpf == None:
            pass
        else:
            break
    if cpf in server.usuarios_cadastrados:
        print("CPF já cadastrado. Retornando...")
        return None
    
    nome_empresa = input("Nome da empresa: ")
    username = input("Nome do empresário: ")
    email = input("E-mail da empresa: ").lower()
    password = input("Insira a sua senha: ")
    
    confirm_password = ""
    while confirm_password != password:
        confirm_password = input("Confirme sua senha: ")
        if confirm_password != password: print("A senha entrada foi diferente.")
    
    endereco = {}
    endereco["UF"] = input("Estado: ")
    endereco["cidade"] = input("Cidade: ")
    endereco["bairro"] = input("Bairro: ")
    
    while True:
        try:
            endereco["CEP"] = input("CEP: ")
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
    
    while True:
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

    new_user = User(cpf, nome_empresa, username, usertype, email, password, endereco)
    server.usuarios_cadastrados[cpf] = new_user 
        
    print("Cadastro efetuado com sucesso! Efetuando login...\n")
    
    return new_user


def mostrar_perfil(usuario):
    print("-----------")
    print(f"CPF cadastrado:\n{usuario.cpf}")
    print(f"Nome da empresa:\n{usuario.nome_empresa}")
    print(f"Nome do usuário:\n{usuario.username}")
    print(f"E-mail:\n{usuario.email}")
    print(f"Endereço:\n{usuario.endereco['rua']}, {usuario.endereco['numero']} {usuario.endereco['complemento']}")
    print(f"{usuario.endereco['CEP']}")
    print(f"{usuario.endereco['bairro']}, {usuario.endereco['cidade']}, {usuario.endereco['UF']}")