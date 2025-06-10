import string # biblioteca com funções relacionadas a string
import random # biblioteca com funções de geração de numeros aleatorios
import datetime # biblioteca com funções de calendário
import server

# objeto de coleta
class Coleta:
    def __init__(self,id,solicitante,data_solicitacao,data_prevista,residuos,status):
        self.id = id
        self.solicitante = solicitante
        self.data_solicitacao = data_solicitacao
        self.data_prevista = data_prevista
        self.residuos = residuos
        self.status = status
        
# gera uma id aleatoria, com 9 caracteres de letras maiusculas e numeros
def gerador_id(size=9, chars=string.ascii_uppercase + string.digits):
    # "chars" é uma variavel
    # composta por todas as letras maiusculas do alfabeto (string.ascii_uppercase)
    # mais todos os algarismos (string.digits)
    # random.choice seleciona caracteres aleatorios de chars para serem retornados
    # o processo é repetido pela quantidade de vezes especificada no "size" (que é o tamanho da ID a ser gerada)
    return ''.join(random.choice(chars) for _ in range(size)) # retorna como uma string

def solicitar_coleta(solicitante):
    id = gerador_id() # gera uma id para a solicitação
    barbeiro = solicitante 
    # registra a data da solicitação utilizando o calendário do sistema
    data_solicitacao = datetime.datetime.now()
    # registra uma data de previsão
    # a data é gerada aleatoriamente com base na data da solicitação
    data_prevista = data_solicitacao + datetime.timedelta(
        days=random.randint(1, 7), # dia seguinte até a próxima semana
        hours=random.randint(8,16), # entre 8 e 16 horas
        minutes=random.randint(0,59) # entre 0 e 58 minutes
        )
    residuos = input("Qual o tipo de resíduo que sera coletado?")
    status = "Agendada"
    
    # cria obj de coleta
    coleta = Coleta(id,barbeiro,data_solicitacao,data_prevista, residuos, status)    
    server.coletas.append(coleta) # adiciona coleta a lista de coletas do servidor
    return coleta # retorna objeto de coleta

def mostrar_coleta(coleta,usertype):
    if usertype == "usuario": # print especifico para usuarios (barbeiros)
        print(f"ID da coleta: {coleta.id}")
        print(f"Data agendada: {coleta.data_solicitacao}")
        print(f"Data prevista: {coleta.data_prevista}")
        print(f"Tipos de resíduos: {coleta.residuos}")
        print(f"Status: {coleta.status}")
        print("----------")
    else: # print especifico para parceiros de coleta
        # bota numa variavel as informação para não ficar o código com linhas longas
        usuario_info = server.usuarios_cadastrados[coleta.solicitante]
        print(f"Solicitação {coleta.id}")
        print(f"Solicitante: {usuario_info.username} | Data solicitada: {coleta.data_solicitacao}")
        print(f"Tipos de resíduos: {coleta.residuos}")
        print("Endereço:")
        print(f"{usuario_info.endereco['rua']}, {usuario_info.endereco['numero']}, {usuario_info.endereco['complemento']}")
        print(f"{usuario_info.endereco['bairro']}, {usuario_info.endereco['cidade']}, {usuario_info.endereco['UF']}")
        print(f"CEP: {usuario_info.endereco['CEP']}")
        print("----------")

def realizar_coleta(coleta, coletador):
    solicitante = server.usuarios_cadastrados[coleta.solicitante] # busca o solicitante na lista de usuarios cadastrados
    
    clt_index1 = solicitante.coletas.index(coleta) # pega o indice da coleta na lista de coletas ativas do usuario
    solicitante.coletas[clt_index1].status = "Finalizada" # bota o status como finalizada
    solicitante.coletas_realizadas.append(coleta) # bota a coleta para o histórico de coletas
    solicitante.coletas.pop(clt_index1) # retira a coleta da lista de coletas ativas
    
    clt_index2 = coletador.coletas.index(coleta) # mesma lógica, para o coletador
    coletador.coletas[clt_index2].status = "Finalizada"
    coletador.coletas_realizadas.append(coleta)
    coletador.coletas.pop(clt_index2)
    
    print (f"Coleta {coleta.id} finalizada com sucesso!")