from settings import *
from  functions_pagina import *

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
               print(f"\n\t {DUVIDAS[0]} - {DUVIDAS[1]} ")
               print(f"\n\t {DUVIDAS[1]} - {DUVIDAS[2]} ")
               print(f"\n\t {DUVIDAS[2]} - {DUVIDAS[3]}  ")
               print(f"\n\t {DUVIDAS[3]} - {DUVIDAS[4]}  ")
               print("\n")
               PAGINA = duvidas()