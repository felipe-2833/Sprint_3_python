from functions import *
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
def verifica_marca_modelo() -> str | str | bool:
    marca = input("\tDigite a marca do seu carro: ").lower()
    if marca not in BD_MARCA_MODELOS.keys():
        print("\t\nMarca não encontrada.")
        return "","",False
    modelo = input(f"\tDigite o modelo do seu carro: ").lower()
    lista_modelos = BD_MARCA_MODELOS[marca]
    if modelo not in lista_modelos:
        print("\t\nModelo não encontrado.")
        return "","", False
    
    return marca, modelo, True

# Função para definir o tipo de problema e gerar um possivel agendamento com as informações do carro.
def tipo_problema_(marca:str, modelo:str,id:str) -> dict:
    while True:
        tipo = input("\nEscolha 0 - Nenhum dos problemas | 1 - Poblema Motor | 2 - Problema Transmissão | 3 - Falha Elétrica | 4 - Problemas freios: ")
        match tipo:
            case '0':
                print("\n\t Ok até a proxima!")
                return {"id":None}
            case '1':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é de superaquecimento do carro,\n\t pode ser um problema sério, pois pode danificar o motor e outros \n\tcomponentes importantes do veículo...")
                problema = "Poblema Motor"
                return agendamento(problema,marca,modelo, id)
            case '2':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é de dificuldade de troca de marcha,\n\t será necessário uma troca dos sincronizadores desgastados...")
                problema = "Problema Transmissão"
                return agendamento(problema,marca, modelo, id)
                
            case '3':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema é da bateria do carro\n\t será necesserio troca...")
                problema = "Falha Elétrica"
                return agendamento(problema,marca, modelo, id)

            case '4':
                foto(20)
                print("\n\t Certo!Segundo a foto tirada o problema está no desgaste das pastilhas,\n\t será necesserio troca...")
                problema = "Problemas freios"
                return agendamento(problema,marca, modelo, id)
            case _:
                print("Escolha entre 1, 2, 3 ou 4")

# Função para mudar data de agendamento
def mudar_data(carros:list[dict], carros_agendados:list[dict]) -> list[dict]:
    while True:
        confirm_data = input("\n\tGostaria de mudar a data? [S/n]:")
        if confirm_data.lower() != "s":
            return carros_agendados
        else:
            n_agendamento = input("\n\tInforme o numero do agendamento que deseja mudar a data:")
            carro_escolhido = carros[n_agendamento]
            index = carros_agendados.index(carro_escolhido)
            for data in DATAS:
                if data != carro_escolhido["data"]:
                    print(f"\n\tData disponivel para agendamento (n - {DATAS.index(data)}): ", data)
            data_nova = input("\n\tInforme o numero da nova data ou digite 3 para manter a data anterio: ")
            if data_nova == 3:
                return carros_agendados
            elif data_nova == 0 or 1 or 2:
                carro_escolhido["data"] = DATAS[int(data_nova)]
                carro_data_antiga = carros_agendados[index]
                carros_agendados.remove(carro_data_antiga)  
                carros_agendados.insert(index, carro_escolhido)
                return carros_agendados
            else:
                print("Opção invalida!informe(0, 1 ou 2)")
                
# Função para cancelar agendamento
def cancelar_agendamento(carros:list[dict], carros_agendados:list[dict]) -> list[dict]:
    while True:
        confirm = input("\tGostaria de cancelar seu agendamento?[S/n]:")
        if confirm.lower() == "n":
            print("OK, até!")
            return carros_agendados
        elif confirm.lower() == "s":
            try:
                n_agendamento = input("\n\tInforme o numero do agendamento que deseja cancelar:")
                carro_escolhido = carros[n_agendamento]
                for carro in carros_agendados:
                    if carro == carro_escolhido:
                        carros_agendados.remove(carro)
                        print("\tCancelamento realizado com sucesso!")
                return carros_agendados
            except KeyError:
                print("Você não digitou um numero de agendamento valido!")
                continue
        else:
            print("Opção invalida!informar: [S/n]")
    
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
            
#Função que verifica no bd o login e senha, retorna o numero da pagina, a validação para acessar a area de explorar e o usuario que foi logado.
def login() -> int| bool| str:
    print("Login de usuário:")
    while True:
        user_name = input("\nUser name: ")
        senha = input("Senha: ")

        login_valido = busca_login(user_name, senha)
        
        if login_valido:
            print("Login realizado com sucesso!")
            return 0, True, user_name, busca_matche_usuario("user_name", user_name)
        else:
            print("Usuario não encontrado")
            continuar = input("\nTentar novamente? [S/n]: ")
            print("\n")
            if continuar.lower() != "s":
                return 0, False, "", []
            else:
                return 5, False, "", []
            
#Função que permite o usuario se cadastrar e adicionar suas informações na bd
def cadastro() -> int:
    print("Cadastre seu usuário:")
    while True:
        nome1 = input("\nNome Completo: ")
        nome_valido = validar_nome(nome1)
        if nome_valido:
            nome = nome1
        else:
            continue
        user_name1 = input("User Name: ")
        use_valido = validar_nome(user_name1)
        if use_valido:
            user_name = user_name1
        else:
            continue
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
def info_cadastro(usuario:list[dict]) -> int:
    while True:
        if usuario == []:
            print("\nUsuario não encontrado!")
            return 6
        
        else:
            print(f" # Informações: \n -Nome: {usuario[0]["nome"]}\n -User Name: {usuario[0]["user_name"]} \n -RG: {usuario[0]["RG"]} \n -CPF: {usuario[0]["CPF"]} \n -Data de nascimento: {usuario[0]["Data_Nasc"]} \n -Email: {usuario[0]["email"]} \n -Telefone: {usuario[0]["telefone"]} \n -Endereço: {usuario[0]["adress"]} \n -Senha: {usuario[0]["senha"]}")
            
        continuar = input("\nVocê gostaria de sair?  [S/n]:")
        print("\n")
        if continuar.lower() != "s":
            continue
        else:
            return 6
        
#Função que imprime na tela as informações completas de cadastro e possibilita modificação, retorna o numero da pagina e o status do usuario(logado ou não)
def atualizar_dados(usuario:list[dict]) -> int |bool:
    status = True
    while True:
        if usuario == []:
            print("\nUsuario não encontrado!")
            return 6, status
        
        else:
            print(f" # Informações: \n -Nome: {usuario[0]["nome"]}\n -User Name: {usuario[0]["user_name"]} \n -RG: {usuario[0]["RG"]} \n -CPF: {usuario[0]["CPF"]} \n -Data de nascimento: {usuario[0]["Data_Nasc"]} \n -Email: {usuario[0]["email"]} \n -Telefone: {usuario[0]["telefone"]} \n -Endereço: {usuario[0]["adress"]} \n -Senha: {usuario[0]["senha"]} \n -Voltar")
            opcao = input("Qual informação gostaria de mudar?:").lower()
            
            match opcao:
                case "nome":
                    nome = input("Digite um novo nome:")
                    nome_valido = validar_nome(nome)
                    if nome_valido:
                        aux = nome
                    else:
                        continue
                    atualizar_BD_USUARIOS("nome", aux)
                    
                case "user name":
                    user_name = input("Digite um novo user name:")
                    nome_valido = validar_nome(user_name)
                    if nome_valido:
                        aux = user_name
                    else:
                        continue
                    atualizar_BD_USUARIOS("user_name", aux)
                    
                case "rg":
                    rg1 = input("Digite um novo rg:")
                    rg_valido = validar_rg(rg1)
                    if rg_valido:
                        aux = rg1
                    else:
                        print("RG invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("RG", aux)
                    
                case "cpf":
                    cpf1 = input("Digite um novo cpf:")
                    cpf_valido = validar_cpf(cpf1)
                    if cpf_valido:
                        aux = cpf1
                    else:
                        print("CPF invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("CPF", aux)
                
                case "data de nascimento":
                    data_nascimento1 = input("Digite uma nova data de nascimento:")
                    data_valida = validar_data(data_nascimento1)
                    if data_valida:
                        aux = data_nascimento1
                    else:
                        print("Data invalida!")
                        continue
                    atualizar_BD_USUARIOS("Data_Nasc", aux)
                    
                case "email":
                    email = input("Digite um novo E-mail:")
                    email_valido = validar_email(email)
                    if email_valido:
                        aux = email
                    else:
                        print("Email invalido!")
                        continue
                    atualizar_BD_USUARIOS("email", aux)
                    
                case "telefone":
                    telefone1 = input("Digite um novo telefone:")
                    telefone_valido = validar_telefone(telefone1)
                    if telefone_valido:
                        aux = telefone1 
                    else:
                        print("Telefone invalido!, (somente numeros)")
                        continue
                    atualizar_BD_USUARIOS("telefone", aux)
                    
                case "endereço":
                    aux = input("Digite um novo endereço:")
                    atualizar_BD_USUARIOS("adress", aux)
                    
                case "senha":
                    aux = input("Digite uma nova senha (AVISO!:será necessario realizar login novamente):")
                    atualizar_BD_USUARIOS("senha", aux)
                    status = False
                    
                case "voltar":
                    return 6,status
                    
                case _:
                    print("\n")
                    print("Opção invalida!")
                    print("Escolha uma das opções de cadastro.")
                    continue   
        
        continuar = input("\nVocê gostaria de sair? [S/n]:")
        print("\n")
        if continuar.lower() == "s":
            return 6, status
                