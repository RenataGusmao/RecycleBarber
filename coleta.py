import string
import random
import datetime
import server

class Coleta:
    def __init__(self,id,solicitante,data_solicitacao,data_prevista,residuos,status):
        self.id = id
        self.solicitante = solicitante
        self.data_solicitacao = data_solicitacao
        self.data_prevista = data_prevista
        self.residuos = residuos
        self.status = status
        

def gerador_id(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def solicitar_coleta(solicitante):
    id = gerador_id()
    barbeiro = solicitante 
    data_solicitacao = datetime.datetime.now()
    data_prevista = data_solicitacao + datetime.timedelta(
        days=random.randint(1, 7),
        hours=random.randint(8,16),
        minutes=random.randint(0,59)
        )
    residuos = input("Qual o tipo de resíduo que sera coletado?")
    status = "Agendada"
    coleta = Coleta(id,barbeiro,data_solicitacao,data_prevista, residuos, status)    
    server.coletas.append(coleta)
    return coleta

def mostrar_coleta(coleta,usertype):
    if usertype == "usuario":
        print("--------")
        print(f"ID da coleta: {coleta.id}")
        print(f"Data agendada: {coleta.data_solicitacao}")
        print(f"Data prevista: {coleta.data_prevista}")
        print(f"Tipos de resíduos: {coleta.residuos}")
        print(f"Status: {coleta.status}")
    else:
        usuario_info = server.usuarios_cadastrados[coleta.solicitante]
        print("--------")
        print(f"Solicitação {coleta.id}")
        print(f"Solicitante: {usuario_info.username} | Data solicitada: {coleta.data_solicitacao}")
        print(f"Tipos de resíduos: {coleta.residuos}")
        print("Endereço:")
        print(f"{usuario_info.endereco["rua"]}, {usuario_info.endereco["numero"]}, {usuario_info.endereco["complemento"]}")
        print(f"{usuario_info.endereco["bairro"]}, {usuario_info.endereco["cidade"]}, {usuario_info.endereco["UF"]}")
        print(f"CEP: {usuario_info.endereco["CEP"]}")

def realizar_coleta(coleta):
    server.usuarios_cadastrados[coleta.solicitante].status = "Finalizada"
    server.coletas.pop(coleta)