from time import sleep
from validacaoErro import *


# Linhas, pa tenta faci cussa fica bonito
def linha(tamanho=55):
    print('~' * tamanho)


# Cabecalho di programa
def cabecalho(texto):
    linha()
    print(texto.upper().center(55))
    linha()


# Pa mostra menu princpal, i pa retorna opcao di acordo ku usuario na cudji
def menu_principal(lista_menu):
    for posicao, menu in enumerate(lista_menu):
        print(f'\033[33m{posicao + 1}\033[m - \033[34m{menu}\033[m')

    linha()

    opcao = ler_numero_inteiro('Cal opcao ku misti?: ')
    print()
    return opcao
