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
                    #Permite o usuario modificar suas informações de cadastro
                    case "3":
                        print("\n")
                        if LOGIN_OK:
                            PAGINA,LOGIN_OK = atualizar_dados(USUARIO_LOGADO)
                        else:
                            print("\nNecessario fazer Login!")
                            PAGINA = 6
                    #sair da pagina
                    case "4":
                        PAGINA = 0
                    #caso o usuario digite errado
                    case _:
                        print("\n")
                        print("Opção invalida!")
                        print("Escolha um das opções: 1, 2, 3 ou 4.")
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