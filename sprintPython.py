#Import das funções
from functions import *
from settings import *
from datetime import date, timedelta
        

#PAGINA PRINCIPAL/ HOME
while PAGINA == 0:
    header()
    print("\t PROJETO")
    print("\t  O projeto “Mecânico Virtual” é uma solução criada com \n\t  o intuito de facilitar a comunicação entre cliente e profissional, \n\t  como também tornar todo o processo mais simples, \n\t  com ambas as partes tendo suas necessidades atendidas o tempo todo.")
    print("\n")
    print ("Gostaria de entrar em uma das outras paginas?")
    opcao = input("Escolha 1 - MECÂNICO VIRTUAL | 2 - AGENDAR | 3 - SOBRE NÓS | 4 - FAZER PERGUNTA | 5 - ENCERRAR SESSÃO: ")
    
    match opcao:
        #MECÂNICO VIRTUAL 
        case "1":
           PAGINA = 1
           while PAGINA == 1: 
               header()
               print("\t\t\t MECÂNICO VIRTUAL")
               print("\n\tOlá, sou seu mecânico virtual.")
               MARCA_CARRO, MODELO_CARRO, eh_valido = verifica_marca_modelo()
               if not eh_valido:
                   PAGINA = 0
                   break
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               print("\n\t 1 - Problemas de Motor: \n\t\t - Falhas de ignição, superaquecimento, problemas com a \n\t\tbateria ou falhas no sistema de injeção de combustível.")
               print("\n\t 2 - Problemas de Transmissão: \n\t\t - Dificuldades para engatar as marchas ou ruídos \n\t\testranhos durante as mudanças.")
               print("\n\t 3 - Falhas no Sistema Elétrico: \n\t\t - Falhas na bateria, alternador ou arranque.\n\t\tProblemas com sistemas de iluminação, sensores, \n\t\tsistemas de som e outros componentes eletrônicos.")
               print("\n\t 4 - Problemas no Sistema de Freios: \n\t\t - Desgaste nas pastilhas ou discos de freio,\n\t\t vazamentos no sistema hidráulico, ou falhas \n\t\t no sistema de assistência de frenagem.")
               print("\n")
               N_AGENDAMENTO, PROBLEMA = tipo_problema_()
               PAGINA = 0
        
        #AGENDAR                
        case "2": 
           PAGINA = 2
           while PAGINA == 2: 
               header()
               print("\t\t\t AGENDAMENTO")
               n = input("\n\t Olá, qual seu numero de agendamento? (se não tiver um, digite 0):")
               if n == "0":
                    print("\n\tVá até a pagina de Mecânico virtual para fazermos um diagnostico \n\tdo seu problema:")
                    PAGINA = 0
               elif n == N_AGENDAMENTO:
                    mecanica = escolhe_oficina_aleatoria()
                    DATA = mudar_data(DATA,DATAOP1,DATAOP2,PROBLEMA,MARCA_CARRO,MODELO_CARRO,mecanica)
                    
                    N_AGENDAMENTO = cancelar_agendamento(N_AGENDAMENTO)
                    PAGINA = 0        
               else:
                   print("\n\tTipo de infomação não aceitavel!") 
                   PAGINA = 0
        
        #SOBRE NÓS
        case "3":
            PAGINA = 3
            while PAGINA == 3: 
               header()
               print("\t\t\t SOBRE NÓS")
               print("\n\t|*LOGO*  ANDRÉ GERALDI MARCOLONGO      RM555285|")
               print("\n\t|*LOGO*  SAMIR HAGE NETO               RM555285|")
               print("\n\t|*LOGO*  FELIPE LEVY STEPHENS FIDELIX  RM556426|")
               confirm = input("\nVoltar para HOME?(Escreva sim para voltar): ")
               if confirm == "sim":
                    separador()
                    PAGINA = 0
               else:
                    input("Informação inválida ")
                    PAGINA = 3
        
        #FAZER PERGUNTA
        case "4":
            PAGINA = 4
            while PAGINA == 4: 
               header()
               print("\t\t\t DUVIDAS")
               print("\n\tOlá sou seu assistente virtual, como posso te ajudar?")
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               print("\n\t 1 - Como agendar um serviço?: ")
               print("\n\t 2 - Quais são as políticas de cancelamento e reembolso?: ")
               print("\n\t 3 - Como faço para alterar ou cancelar um agendamento existente?: ")
               print("\n\t 4 - Como posso visualizar ou gerenciar meus agendamentos futuros?: ")
               print("\n")
               PAGINA = duvidas()
               
        #ENCERRAR SESSÃO      
        case "5":
            print("Encerrando...")
            break
    
        #Caso opção errada    
        case _:

            print("\n")
            print("Opção invalida!")
            print("Escolha um das opções: 1, 2, 3, 4 ou 5.")
            continue