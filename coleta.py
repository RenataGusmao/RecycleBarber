# A FAZER:

# funções para solicitação:
#- solicitar coleta (cria um novo objeto de solicitação de coleta)
#- acompanhar coleta
#- finalizar coleta
#- cancelar coleta
import string
import random
import datetime 

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
    status = "Agendado"
    coleta = Coleta(id,barbeiro,data_solicitacao,data_prevista, residuos, status)    
    return coleta

def mostrar_coleta(coleta):
    print("------")
    print(f"ID da coleta: {coleta.id}")
    print(f"Data agendada: {coleta.data_solicitacao}")
    print(f"Data prevista: {coleta.data_prevista}")
    print(f"Tipos de resíduos: {coleta.residuos}")
    print(f"Status: {coleta.status}")
    input("Pressione Enter para voltar.\n")