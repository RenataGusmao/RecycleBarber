import random
import string

usuarios_cadastrados = {} # lista de usuários cadastrados

# objeto do usuário
class User:
    def __init__(self, cpf, nome_empresa, username, email, password, endereco):
        self.cpf = cpf
        self.nome_empresa = nome_empresa
        self.username = username
        self.email = email
        self.password = password
        self.endereco = endereco
        self.coletas = []

def verificar_cpf(cpf = str):
    cpf = cpf.replace(".","") # retira pontos da string, caso o usuário colocar
    cpf = cpf.replace("-","") # retira traços da string, caso o usuário colocar
    if len(cpf) != 11: raise Exception # um CPF tem 11 digitos, se não tiver, levanta uma exceção
    cpf = int(cpf)
    return cpf

# login
def login(): # a fazer
    efetuado = False
    while not efetuado:
        cpf = verificar_cpf(input("Insira seu CPF: "))
        if str(cpf) in usuarios_cadastrados:
            usuario = usuarios_cadastrados[cpf]
            senha = input("Insira sua senha.")
            if senha == usuario.password:
                efetuado = True
            else:
                pass

# cadastro
def cadastrar():
    while True:
        try:
            cpf = verificar_cpf(input("Insira seu CPF: "))
        except:
            print("Erro: CPF inválido. Por favor, tente novamente.")
        else:
            if str(cpf) in usuarios_cadastrados: # transforma o CPF em string temporariamente para 
                print("CPF já cadastrado. Retornando...")
                break # se o CPF já estiver cadastrado, quebra o loop e cancela o cadastro
            
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
            
            while True:
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
            
            new_user = User(cpf, nome_empresa, username, email, password, endereco) # cria objeto de usuário
            usuarios_cadastrados[str(cpf)] = new_user
            
            print("Cadastro efetuado com sucesso! Efetuando login...\n")
            
            return new_user # retorna valor booleano para já funcionar com a lógica do main

def mostrar_perfil(usuario):
    print("-----------")
    print(f"CPF cadastrado:\n{usuario.cpf}")
    print(f"Nome da empresa:\n{usuario.nome_empresa}")
    print(f"Nome do usuário:\n{usuario.username}")
    print(f"E-mail:\n{usuario.email}")
    print(f"Endereço:\n{usuario.endereco["rua"]}, {usuario.endereco["numero"]} {usuario.endereco["complemento"]}")
    print(f"{usuario.endereco["CEP"]}")
    print(f"{usuario.endereco["bairro"]}, {usuario.endereco["cidade"]}, {usuario.endereco["UF"]}")