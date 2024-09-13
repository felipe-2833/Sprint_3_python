from settings import *
from datetime import datetime 

#Função que imprime faz a verificação de ação do usuario pós tirar uma duvida 
def perguntar_saida_pag_duvidas() -> int:
    from functions_pagina import separador
    confirm = input("\n\tGostaria de tirar mais alguma duvida?[S/n]: ")
    if confirm.lower() != "s":
        return  0
    else:
        separador()
        return 4
    
#Função que busca um valor dentro de uma tupla no bd e retorna esta tupla caso encontre o valor desejado
def busca(chave: int, valor: str | int) -> dict:
    for user in BD_USUARIOS:
        if user[chave] == valor:
            return user
    return {}
    
def busca_login(nome_usuario: str, senha: str | int) -> bool:
    for user in BD_USUARIOS:
        for key,value in user.items():
            if user["user_name"] == nome_usuario and user["senha"] == senha:
                return True
    return False

#Função que verifica se a algum valor compativel com alguma tupla no bd usuarios, retorna uma lista com a tupla encontrada
def busca_matche_usuario(chave: int, valor: str | int) -> list[dict]:
    result = []
    for user in BD_USUARIOS:
        if user[chave] == valor:
            result.append(user)
    return result

#Função para validação de RG
def validar_rg(rg) -> bool:
    rg = ''.join(filter(str.isalnum, rg))
    return 7 <= len(rg) <= 9

def validar_cpf(cpf) -> bool:
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

def validar_telefone(telefone:str) -> bool:
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) not in [10, 11]:
        return False
    
    return True

#Função que retorna o numero de id do usuario
def id_usuario() -> str:
    return str(int(BD_USUARIOS[-1]["user_id"]) + 1)

#Função que verifica se o user name ja se encontra em uma tupla no bd 
def verifica_usuario(user_name:str) -> bool:
    result = busca("user_name", user_name)
    return len(result) > 0 and len(result["user_name"]) > 0

#Função que atualiza o bd usuarios, apagando a antiga tupla e add uma nova com novas informções    
def atualizar_BD_USUARIOS(key: str, nome_cadastrado: str, aux:str | int | datetime) -> None:
    for user in BD_USUARIOS:
        if user["user_name"] == nome_cadastrado:
            user[key] = aux
            print("\nModificação realizada com sucesso!")