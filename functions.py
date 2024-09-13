from settings import *
from  functions_pagina import *

#Função que imprime faz a verificação de ação do usuario pós tirar uma duvida 
def perguntar_saida_pag_duvidas():
    confirm = input("\n\tGostaria de tirar mais alguma duvida?[S/n]: ")
    if confirm.lower() != "s":
        PAGINA = 0
    else:
        separador()
        PAGINA = 4