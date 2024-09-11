#import de bibliotecas
import random
from datetime import date, timedelta
from settings import *  

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
    
# Função verifica marca e modelo
def verifica_marca_modelo():
    marca = input("\tDigite a marca do seu carro: ").lower()
    if marca not in MARCA_CARROS:
        print("\t\nMarca não encontrada.")
        return "","",False
    
    indice_marca = MARCA_CARROS.index(marca)
    modelo = input(f"\tDigite o modelo do seu carro ({', '.join(MODELOS_CARROS[indice_marca])}): ").lower()
    if modelo not in MODELOS_CARROS[indice_marca]:
        print("\t\nModelo não encontrado.")
        return "","", False
    
    return marca, modelo, True

# Função gera oficina aleatoria
def escolhe_oficina_aleatoria():
    return random.choice(OFICINAS_MECANICAS)

# Função para desenhar um quadrado com o tamanho especificado, para utilizar como foto
def foto(SIZE):
    print("\n\tTire uma foto do problema do carro")
    for i in range(10):
        print("\t\t\t\t\t\t\t\t",'*' * SIZE)
    print("\n\tObrigado!")

# Função para agendar e forncer o codigo de agendamento
def agendamento(tipo_problema):
    while True:
        inf = input("\n\t Gostaria de agendar com nossos mecanicos?(sim ou não):")
        if inf == "sim":
            ramdom = random.randint(1,100)
            N_AGENDAMENTO = int(ramdom) 
            print(f"\n\tOK foi agendado! Seu numero de agendamento é {N_AGENDAMENTO}")
            print(f"\tAgora vá/ou retorne a pagina de agendamento e digite seu numero de\n\t agendamento para informações")
            return N_AGENDAMENTO
        elif inf == "não":
            print("\tOK, até a proxima!")
            break
        else:
            print("\tDigite sim ou não.")
            
        
# Função para definir o problema e o codigo
def tipo_problema_():
    while True:
        tipo = input("\nEscolha 0 - Nenhum dos problemas | 1 - Poblema Motor | 2 - Problema Transmissão | 3 - Falha Elétrica | 4 - Problemas freios: ")
        match tipo:
            case '0':
                print("\n\t Ok até a proxima!")
                return "", ""
            case '1':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é de superaquecimento do carro,\n\t pode ser um problema sério, pois pode danificar o motor e outros \n\tcomponentes importantes do veículo...")
                PROBLEMA = "Poblema Motor"
                N_AGENDAMENTO = agendamento(PROBLEMA)
                return str(N_AGENDAMENTO), PROBLEMA
            case '2':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é de dificuldade de troca de marcha,\n\t será necessário uma troca dos sincronizadores desgastados...")
                PROBLEMA = "Problema Transmissão"
                N_AGENDAMENTO = agendamento(PROBLEMA)
                return str(N_AGENDAMENTO), PROBLEMA
            case '3':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é da bateria do carro\n\t será necesserio troca...")
                PROBLEMA = "Falha Elétrica"
                N_AGENDAMENTO = agendamento(PROBLEMA)
                return str(N_AGENDAMENTO), PROBLEMA

            case '4':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema está no desgaste das pastilhas,\n\t será necesserio troca...")
                PROBLEMA = "Problemas freios"
                N_AGENDAMENTO = agendamento(PROBLEMA)
                return str(N_AGENDAMENTO), PROBLEMA
            case _:
                print("Escolha entre 1, 2, 3 ou 4")
            

# Função para cancelar agendamento
def cancelar_agendamento(n_agendameto):
    confirm = input("\tGostaria de cancelar seu agendamento?(sim ou não):")
    if confirm == "sim":
        print("\tCancelamento realizado com sucesso!")
        separador()
        return 0
    elif confirm == "não":
        print("OK, até!")
        separador()
        return n_agendameto
    else:
        input("Informação inválida ")
        return n_agendameto

# Função para mudar data de agendamento
def mudar_data(data,dataop1,dataop2,problema,marca_carro,modelo_carro,mecanica):
    while True:
        print(f"\n\tInformações do agendamento:\n\t\t -Data: {data}\n\t\t -Marca do carro: {marca_carro}\n\t\t -Modelo do carro: {modelo_carro}\n\t\t -Problema: {problema} \n\t\t -Mecânica: {mecanica}")
        confirm_data = input("\n\tGostaria de mudar a data?(sim ou não):")
        if confirm_data == "sim":
            print(f"\tOK, temos essas datas disponiveis: \n\t1 -{dataop1} \n\t2 -{dataop2}")
            ok = input("\tEscolha entre uma das novas datas(1 ou 2) ou digite 0 para manter a data: ")
            match ok:
                case "0":
                    return data
                case "1":
                    if data == DATA0:
                        data = DATA1
                        dataop1 = DATA0
                        dataop2 = DATA2
                    elif data == DATA1:
                         data = DATA0
                         dataop1 = DATA1
                         dataop2 = DATA2
                    else:
                         data = DATA0
                         dataop1 = DATA1
                         dataop2 = DATA2
                    continue
                case "2":
                    if data == DATA0:
                        data = DATA2
                        dataop1 = DATA0
                        dataop2 = DATA1
                    elif data == DATA1:
                         data = DATA2
                         dataop1 = DATA0
                         dataop2 = DATA1
                    else:
                         data = DATA1
                         dataop1 = DATA0
                         dataop2 = DATA2
                    continue
                case _:
                    print("\tEscolha entre 0, 1 ou 2")
                    continue
                    
        elif confirm_data == "não": 
            print(f"\tOK!")
            return data
        else:
            print(f"\tEscreva sim ou não")
            continue
                        
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
                confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
                if confirm == "sim":
                        separador()
                        return 4
                elif confirm == "não":
                        print("OK, até!")
                        separador()
                        return 0
                else:
                        input("Informação inválida ")
                        return 0
            case '2':
                print("\n\tCerto!É possivel cancelar seu agendamento na pagina AGENDAMENTO.")
                confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
                if confirm == "sim":
                        separador()
                        return 4
                elif confirm == "não":
                        print("OK, até!")
                        separador()
                        return 0
                else:
                        input("Informação inválida ")
                        return 0
            case '3':
                print("\n\tCerto!Entre na pagina de AGENDAMENTO, coloque seu numero de agendamento \n\te escolha a opção CANCELAR AGENDAMENTO escrevendo cancelar no indicado;")
                confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
                if confirm == "sim":
                        separador()
                        return 4
                elif confirm == "não":
                        print("OK, até!")
                        separador()
                        return 0
                else:
                        input("Informação inválida ")
                        return 0
            case '4':
                print("\n\tCerto!É apenas possivel realizar 1 agendamento por vez e então \n\tvizualizalo na pagina de AGENDAMENTO.")
                confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
                if confirm == "sim":
                        separador()
                        return 4
                elif confirm == "não":
                        print("OK, até!")
                        separador()
                        return 0
                else:
                        input("Informação inválida ")
                        return 0
            case _:
                continue
