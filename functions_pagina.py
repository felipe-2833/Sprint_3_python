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
def duvidas() -> int:
     while True:
        duv = input("Escolha 1, 2, 3, 4 ou 0 caso não queira tirar nenhuma duvida:")
        match duv:
            case '0':
                print("OK, até!")
                separador()
                return 0
            case '1':
                print("\n\tCerto!Entre na pagina Mecânico Virtual, faça um diagnostico de seu \n\tproblema. Marque uma consulta e \n\tveja suas informações em AGENDAMENTO.")
                return perguntar_saida_pag_duvidas()
            case '2':
                print("\n\tCerto!É possivel cancelar seu agendamento na pagina AGENDAMENTO.")
                return perguntar_saida_pag_duvidas()
            case '3':
                print("\n\tCerto!Entre na pagina de AGENDAMENTO, \n\te escolha a opção CANCELAR AGENDAMENTO escrevendo cancelar no indicado;")
                return perguntar_saida_pag_duvidas()
            case '4':
                print("\n\tCerto!Vizualizalo na pagina de AGENDAMENTO.")
                return perguntar_saida_pag_duvidas()
            case _:
                continue
            
#Função que verifica no bd o login e senha, retorna o numero da pagina, a validação para acessar a area de explorar e o user_name que está sendo usado no momento.
def login() -> int| bool| str:
    print("Login de usuário:")
    while True:
        user_name = input("\nUser name: ")
        senha = input("Senha: ")

        login_valido = busca_login(user_name, senha)
        
        if login_valido:
            print("Login realizado com sucesso!")
            return 0, True, user_name
        else:
            print("Usuario não encontrado")
            continuar = input("\nTentar novamente? [S/n]: ")
            print("\n")
            if continuar.lower() != "s":
                return 0, False, ""
            else:
                return 2, False, ""
            
#Função que permite o usuario se cadastrar e adicionar suas informações na bd
def cadastro() -> int:
    print("Cadastre seu usuário:")
    while True:
        nome = input("\nNome Completo: ")
        user_name = input("User Name: ")
        rg1 = input("RG: ")
        rg_valido = validar_rg(rg1)
        if rg_valido:
            rg = rg1
        else:
            print("RG invalido!, (somente numeros)")
            continue
        
        cpf1 = input("CPF: ")
        cpf_valido = validar_cpf(cpf1)
        if cpf_valido:
            cpf = cpf1
        else:
            print("CPF invalido!, (somente numeros)")
            continue
        
        data_nascimento1 = input("Data de Nascimento: ")
        data_valida = validar_data(data_nascimento1)
        if data_valida:
            data_nascimento = data_nascimento1
        else:
            print("Data invalida!")
            continue
        
        email1 = input("E-mail: ")
        email_valido = validar_email(email1)
        if email_valido:
            email = email1
        else:
            print("Email invalido!")
            continue
        
        telefone1 = input("Telefone: ")
        telefone_valido = validar_telefone(telefone1)
        if telefone_valido:
            telefone = telefone1
        else:
            print("Telefone invalido!, (somente numeros)")
            continue
        
        endereco = input("Endereço: ")
        senha = input("Senha: ")

        user_id = id_usuario()

        if not verifica_usuario(user_name):
            BD_USUARIOS.append({"user_id":user_id, "nome":nome, "user_name":user_name, "RG":rg, "CPF":cpf, "Data_Nasc":data_nascimento, "email":email, "telefone":telefone, "adress":endereco, "senha":senha})
            print("Usuário cadastrado com sucesso!!!")
            return 6
        else:
            print("Não foi possivel o cadastro. User name ja existe.")
            continuar = input("\nContinuar cadastrando? [S/n]: ")
            print("\n")
            if continuar.lower() != "s":
                return 6
            else:
                continue
            
#Função que imprime na tela as informações completas de cadastro, retorna o numero da pagina
def info_cadastro() -> int:
    while True:
        name_cadastro = input("Informe seu User name: ")
        cadastro = busca_matche_usuario("user_name", name_cadastro)
        
        if cadastro == []:
            print("\nUsuario não encontrado!")
            return 6
        
        else:
            print(f" # Informações: \n -Nome: {cadastro[0]["nome"]}\n -User Name: {cadastro[0]["user_name"]} \n -RG: {cadastro[0]["RG"]} \n -CPF: {cadastro[0]["CPF"]} \n -Data de nascimento: {cadastro[0]["Data_Nasc"]} \n -Email: {cadastro[0]["email"]} \n -Telefone: {cadastro[0]["telefone"]} \n -Endereço: {cadastro[0]["adress"]} \n -Senha: {cadastro[0]["senha"]}")
            
        continuar = input("\nVocê gostaria de sair?  [S/n]:")
        print("\n")
        if continuar.lower() != "s":
            continue
        else:
            return 6
        
#Função que imprime na tela as informações completas de cadastro e possibilita modificação, retorna o numero da pagina
def atualizar_dados() -> int:
    while True:
        name_cadastro = input("Informe seu User name: ")
        cadastro = busca_matche_usuario("user_name", name_cadastro)
        
        if cadastro == []:
            print("\nUsuario não encontrado!")
            return 6
        
        else:
            print(f" # Informações: \n -Nome: {cadastro[0]["nome"]}\n -User Name: {cadastro[0]["user_name"]} \n -RG: {cadastro[0]["RG"]} \n -CPF: {cadastro[0]["CPF"]} \n -Data de nascimento: {cadastro[0]["Data_Nasc"]} \n -Email: {cadastro[0]["email"]} \n -Telefone: {cadastro[0]["telefone"]} \n -Endereço: {cadastro[0]["adress"]} \n -Senha: {cadastro[0]["senha"]}")
            opcao = input("Qual informação gostaria de mudar?:").lower()
            
            match opcao:
                case "nome":
                    aux = input("Digite um novo nome:")
                    atualizar_BD_USUARIOS("nome", name_cadastro, aux)
                    
                case "user name":
                    aux = input("Digite um novo nome:")
                    atualizar_BD_USUARIOS("user_name", name_cadastro, aux)
                    
                case "rg":
                    rg1 = input("Digite um novo rg:")
                    rg_valido = validar_rg(rg1)
                    if rg_valido:
                        aux = rg1
                    else:
                        print("RG invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("RG", name_cadastro, aux)
                    
                case "cpf":
                    cpf1 = input("Digite um novo cpf:")
                    cpf_valido = validar_cpf(cpf1)
                    if cpf_valido:
                        aux = cpf1
                    else:
                        print("CPF invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("CPF", name_cadastro, aux)
                
                case "data de nascimento":
                    data_nascimento1 = input("Digite uma nova data de nascimento:")
                    data_valida = validar_data(data_nascimento1)
                    if data_valida:
                        aux = data_nascimento1
                    else:
                        print("Data invalida!")
                        continue
                    atualizar_BD_USUARIOS("Data_Nasc", name_cadastro, aux)
                    
                case "email":
                    email = input("Digite um novo E-mail:")
                    email_valido = validar_email(email)
                    if email_valido:
                        aux = email
                    else:
                        print("Email invalido!")
                        continue
                    atualizar_BD_USUARIOS("email", name_cadastro, aux)
                    
                case "telefone":
                    telefone1 = input("Digite um novo telefone:")
                    telefone_valido = validar_telefone(telefone1)
                    if telefone_valido:
                        aux = telefone1 
                    else:
                        print("Telefone invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("telefone", name_cadastro, aux)
                    
                case "endereço":
                    aux = input("Digite um novo endereço:")
                    atualizar_BD_USUARIOS("adress", name_cadastro, aux)
                    
                case "senha":
                    aux = input("Digite uma nova senha (será necessario realizar login novamente):")
                    atualizar_BD_USUARIOS("senha", name_cadastro, aux)
                    LOGIN_OK = False
                    
                case _:
                    print("\n")
                    print("Opção invalida!")
                    print("Escolha uma das opções de cadastro.")
                    continue   
        
        continuar = input("\nVocê gostaria de sair?  [S/n]:")
        print("\n")
        if continuar.lower() != "s":
            continue
        else:
            return 6