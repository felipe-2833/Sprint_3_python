from settings import *
from datetime import datetime 
import random

# Função para desenhar um quadrado com o tamanho especificado, para utilizar como foto
def foto(SIZE:int):
    print("\n\tTire uma foto do problema do carro")
    for i in range(10):
        print("\t\t\t\t\t\t\t\t",'*' * SIZE)
    print("\n\tObrigado!")
    
# Função para agendar e recolher as informações do agendamento
def agendamento(tipo_problema:str, marca:str, modelo:str,id:str) -> dict:
    while True:
        inf = input("\n\t Gostaria de agendar com nossos mecanicos?[S/n]:").lower()
        if inf == "s":
            print("\n\tOK foi agendado!")
            print("\tAgora vá/ou retorne a pagina de agendamento para mais informações.")
            return {"data": str(escolhe_data_aleatoria()), "marca": marca, "modelo": modelo, "problema": tipo_problema,"mecanica": escolhe_oficina_aleatoria(), "id":id}
        elif inf == "n":
            print("\tOK, até a proxima!")
            return{}
        else:
            print("\tDigite S/n.")
            
# Função gera oficina aleatoria
def escolhe_oficina_aleatoria() -> str:
    return random.choice(OFICINAS_MECANICAS)

# Função gera oficina aleatoria
def escolhe_data_aleatoria() -> date:
    return random.choice(DATAS)

#Função que imprime/faz a verificação de ação do usuario pós tirar uma duvida 
def perguntar_saida_pag_duvidas() -> int:
    from functions_pagina import separador
    confirm = input("\n\tGostaria de tirar mais alguma duvida?[S/n]: ")
    if confirm.lower() != "s":
        return  0
    else:
        separador()
        return 4
    
#Função que busca um valor dentro de um dicionario no bd e retorna este dicionario caso encontre o valor desejado
def busca(chave: int, valor: str | int) -> dict:
    for user in BD_USUARIOS:
        if user[chave] == valor:
            return user
    return {}
    
#Função que faz verificação caso o usuario tenha feito cadastro
def busca_login(nome_usuario: str, senha: str | int) -> bool:
    for user in BD_USUARIOS:
        if user["user_name"] == nome_usuario and user["senha"] == senha:
            return True
    return False

#Função que verifica se a algum valor compativel com algum dicionario no bd usuarios, retorna uma lista com o dicionario encontrada
def busca_matche_usuario(chave: int, valor: str | int) -> list | list[dict]:
    result = []
    for user in BD_USUARIOS:
        if user[chave] == valor:
            result.append(user)
    return result

#Função que faz validação de nome e user_name, possibilitando qualquer nome maior de 3 char
def validar_nome(user_name:str) -> str:
    if len(user_name) > 3:
        return user_name
    else:
        print("O nome de usuário é inválido. Deve ter mais de 3 caracteres.")

#Função para validação de RG
def validar_rg(rg:str) -> bool:
    rg = ''.join(filter(str.isalnum, rg))
    return 7 <= len(rg) <= 9

#Função para validar o CPF
def validar_cpf(cpf:str) -> bool:
    rg = ''.join(filter(str.isalnum, cpf))
    return 7 <= len(cpf) <= 11

#Função para validação de data
def validar_data(data: datetime) -> bool:
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
#Função para validação do e-mail 
def validar_email(email:str) -> bool:
    if "@" not in email:
        return False
    
    usuario, dominio = email.split("@", 1)
    
    if not usuario or not dominio:
        return False
    
    if "." not in dominio:
        return False
    
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    
    return True

#Função para validação do telefone
def validar_telefone(telefone:str) -> bool:
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) not in [10, 11]:
        return False
    
    return True

#Função que retorna o numero de id do usuario
def id_usuario() -> str:
    return str(int(BD_USUARIOS[-1]["user_id"]) + 1)

#Função que verifica se o user name ja se encontra em um dicionario no bd 
def verifica_usuario(user_name:str) -> bool:
    result = busca("user_name", user_name)
    return len(result) > 0 and len(result["user_name"]) > 0

#Função que atualiza o bd usuarios, apagando a antigo dicionario e add um novo com novas informções    
def atualizar_BD_USUARIOS(key: str, aux:str | int | datetime) -> None:
    for user in BD_USUARIOS:
        user[key] = aux
        print("\nModificação realizada com sucesso!")