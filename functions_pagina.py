from functions import *

# Função separador
def separador():
    print("-" * 88)
    print("\n")
    
# Função para o header
def header():
    separador()
    print("-" * 88)
    print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
    separador()
    print("\t","-" * 65)
    
# Função para Duvidas
def duvidas():
     while True:
        duv = input("Escolha 1, 2, 3, 4 ou 0 caso não queira tirar nenhuma duvida:")
        match duv:
            case '0':
                print("OK, até!")
                separador()
                return 0
            case '1':
                print("\n\tCerto!Entre na pagina Mecânico Virtual, faça um diagnostico de seu \n\tproblema. Marque uma consulta e grave seu numero de agendameto para poder \n\tver suas informações.")
                perguntar_saida_pag_duvidas()
            case '2':
                print("\n\tCerto!É possivel cancelar seu agendamento na pagina AGENDAMENTO.")
                perguntar_saida_pag_duvidas()
            case '3':
                print("\n\tCerto!Entre na pagina de AGENDAMENTO, coloque seu numero de agendamento \n\te escolha a opção CANCELAR AGENDAMENTO escrevendo cancelar no indicado;")
                perguntar_saida_pag_duvidas()
            case '4':
                print("\n\tCerto!É apenas possivel realizar 1 agendamento por vez e então \n\tvizualizalo na pagina de AGENDAMENTO.")
                perguntar_saida_pag_duvidas()
            case _:
                continue