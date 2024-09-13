import pandas as pd
from datetime import date, timedelta

#Variaveis Globais
PAGINA = 0
LOGIN_OK = False
USER_NAME = ""
SIZE = 20

#Listas Globais
DATAS = [(date.today() + timedelta(days=3)).strftime("%d/%m/%y"), (date.today() + timedelta(days=17)).strftime("%d/%m/%y"), (date.today() + timedelta(days=24)).strftime("%d/%m/%y")]
OFICINAS_MECANICAS = [
    "Auto Mecânica Silva",
    "Oficina do João",
    "ReparAuto",
    "Mecânica Rápida",
    "Oficina São José",
    "Auto Center Elite",
    "Oficina Bom Carro",
    "Mecânica da Vila",
    "Oficina dos Amigos",
    "Mecânica Qualicar"
]

#Listas de dicionarios globais
USUARIO_LOGADO = []
DUVIDAS =  {"1":"Como agendar um serviço?: ", 
            "2":"Quais são as políticas de cancelamento e reembolso?: ", 
            "3":"Como faço para alterar ou cancelar um agendamento existente?: ", 
            "4":"Como posso visualizar ou gerenciar meus agendamentos futuros?: "
        }
PROBLEMAS =  {"1":"Problemas de Motor: \n\t\t - Falhas de ignição, superaquecimento, problemas com a \n\t\tbateria ou falhas no sistema de injeção de combustível.", 
            "2":"Problemas de Transmissão: \n\t\t - Dificuldades para engatar as marchas ou ruídos \n\t\testranhos durante as mudanças.", 
            "3":"Falhas no Sistema Elétrico: \n\t\t - Falhas na bateria, alternador ou arranque.\n\t\tProblemas com sistemas de iluminação, sensores, \n\t\tsistemas de som e outros componentes eletrônicos.", 
            "4":"Problemas no Sistema de Freios: \n\t\t - Desgaste nas pastilhas ou discos de freio,\n\t\t vazamentos no sistema hidráulico, ou falhas \n\t\t no sistema de assistência de frenagem. "
        }

CARROS_AGENDADOS = [
    #{"data": "", "marca_carro": "", "modelo": "", "problema": "","mecanica":"", "id":""}
]

#Banco de Dados
BD_USUARIOS = [
    {"user_id":"1", "nome":"felipe", "user_name":"felipe", "RG":"x", "CPF":"x", "Data_Nasc":"x", "email":"x", "telefone":"x", "adress":"x", "senha":"1234"}
]

df = pd.read_csv("Car_Models.csv")
cols = ['Company', 'Model']
df = df[cols]
df.to_csv("Car_Models_Company.csv", index=False)
df['Company'] = df['Company'].str.lower()
df['Model'] = df['Model'].str.lower()
BD_MARCA_MODELOS = df.groupby('Company')['Model'].apply(list).to_dict()