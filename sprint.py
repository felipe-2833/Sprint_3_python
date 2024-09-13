from settings import *
from  functions_pagina import *
from time import sleep

while PAGINA == 0:
    header()
    print("\t PROJETO")
    print("\t  O projeto “Mecânico Virtual” é uma solução criada com \n\t  o intuito de facilitar a comunicação entre cliente e profissional, \n\t  como também tornar todo o processo mais simples, \n\t  com ambas as partes tendo suas necessidades atendidas o tempo todo.")
    print("\n")
    print ("Gostaria de entrar em uma das outras paginas?")
    opcao = input("Escolha 1 - MECÂNICO VIRTUAL | 2 - AGENDAR | 3 - SOBRE NÓS | 4 - FAZER PERGUNTA | 5 - LOGIN | 6 - CADASTRO | 7 - ENCERRAR SESSÃO: ")
    
    match opcao:
        #MECÂNICO VIRTUAL 
        case "1":
           PAGINA = 1
           while PAGINA == 1: 
            if LOGIN_OK:
               header()
               print("\t\t\t MECÂNICO VIRTUAL")
               print("\n\tOlá, sou seu mecânico virtual.")
               marca, modelo, eh_valido = verifica_marca_modelo()
               if not eh_valido:
                   PAGINA = 0
                   break
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               for key,value in PROBLEMAS.items():
                print(f"\n\t {key} - {value} ")
               print("\n")
               carro = tipo_problema_(marca,modelo,USUARIO_LOGADO[0]["user_id"])
               CARROS_AGENDADOS.append(carro)
               PAGINA = 0
            else:
                print("\nNecessario fazer Login!")
                PAGINA = 0
                
        #AGENDAR                
        case "2": 
           PAGINA = 2
           while PAGINA == 2: 
            if LOGIN_OK:
                header()
                print("\t\t\t AGENDAMENTO")
                id_cliente = USUARIO_LOGADO[0]["user_id"]
                carros_cliente = {}
                contador = 0
                for carro in CARROS_AGENDADOS:
                    if carro["id"] == id_cliente:
                        contador += 1
                        print(f"\n\tInformações do agendamento:\n\t\t -Numero Agendamento: {contador}\n\t\t -Data: {carro["data"]}\n\t\t -Marca do carro: {carro["marca"]}\n\t\t -Modelo do carro: {carro["modelo"]}\n\t\t -Problema: {carro["problema"]} \n\t\t -Mecânica: {carro["mecanica"]}\n")
                        carros_cliente[contador] = carro
                    else: 
                        print("\n\tNão há agendamentos!Agende com nossos mecânicos na pagina MECANICO VIRTUAL.")
                        PAGINA = 0
                opcao = input("1 - MUDAR DATA | 2 - CANCELAR AGENDAMENTO | 3 - SAIR: ")
                match opcao:
                    #Permite o usuario se cadastrar
                    case "1":
                        print("\n")
                        CARROS_AGENDADOS = mudar_data(carros_cliente,CARROS_AGENDADOS)
                        PAGINA = 2
                    #Permite o usuario ver suas informações de cadastro
                    case "2":
                        print("\n")
                        if LOGIN_OK:
                            PAGINA = info_cadastro(USUARIO_LOGADO)
                        else:
                            print("\nNecessario fazer Login!")
                            PAGINA = 6
                    #sair da pagina
                    case "3":
                        PAGINA = 0
                    #caso o usuario digite errado
                    case _:
                        print("\n")
                        print("Opção invalida!")
                        print("Escolha um das opções: 1, 2, 3 ou 4.")
                        continue
                
            else:
                print("\nNecessario fazer Login!")
                PAGINA = 0
               
        #SOBRE NÓS
        case "3":
            PAGINA = 3
            while PAGINA == 3: 
               header()
               print("\t\t\t SOBRE NÓS")
               print("\n\t|*LOGO*  ANDRÉ GERALDI MARCOLONGO      RM555285|")
               print("\n\t|*LOGO*  SAMIR HAGE NETO               RM557260|")
               print("\n\t|*LOGO*  FELIPE LEVY STEPHENS FIDELIX  RM556426|")
               confirm = input("\nVoltar para HOME? [S/n]: ")
               if confirm.lower() != "s":
                    PAGINA = 3
               else:
                    separador()
                    PAGINA = 0
                    
        #FAZER PERGUNTA
        case "4":
            PAGINA = 4
            while PAGINA == 4: 
               header()
               print("\t\t\t DUVIDAS")
               print("\n\tOlá sou seu assistente virtual, como posso te ajudar?")
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               for key,value in DUVIDAS.items():
                print(f"\n\t {key} - {value} ")
               print("\n")
               PAGINA = duvidas()
               
        #LOGIN                
        case "5": 
           PAGINA = 5
           while PAGINA == 5: 
               header()
               print("\t\t\t LOGIN")
               print("\n")
               PAGINA, LOGIN_OK , USER_NAME, USUARIO_LOGADO = login()
               
        #CADASTRO
        case "6":
            PAGINA = 6
            while PAGINA == 6: 
                header()
                print("\t\t\t CADASTRO")
                print("\n")
                print("Escolha uma das opções:")
                opcao2 = input("1 - CRIAR CADASTRO | 2 - INFORMAÇÔES DE CADASTRO | 3 - MUDAR INFORMAÇÔES | 4 - SAIR: ")
                
                match opcao2:
                    #Permite o usuario se cadastrar
                    case "1":
                        print("\n")
                        PAGINA = cadastro()
                    #Permite o usuario ver suas informações de cadastro
                    case "2":
                        print("\n")
                        if LOGIN_OK:
                            PAGINA = info_cadastro(USUARIO_LOGADO)
                        else:
                            print("\nNecessario fazer Login!")
                            PAGINA = 6
                    #sair da pagina
                    case "3":
                        PAGINA = 0
                    #caso o usuario digite errado
                    case _:
                        print("\n")
                        print("Opção invalida!")
                        print("Escolha um das opções: 1, 2 ou 3.")
                        continue
            
        #ENCERRAR SESSÃO      
        case "7":
            print("Encerrando", end="", flush=True)
            for i in range(3):
                sleep(1)
                print(".", end="", flush=True)
            print()
            break
    
        #Caso opção errada    
        case _:

            print("\n")
            print("Opção invalida!")
            print("Escolha um das opções:(1 a 7).")
            continue
        