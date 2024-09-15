from interface import *
from arquivos import *
from time import sleep
from validacaoErro import *


meuArquivo = 'pessoas.txt'

# li no na verfica si contra arquivo existe ou nao.
# Si arquivo ca existe, no na crial automaticamente
if not arquivo_existe(meuArquivo=meuArquivo):
    print('Arquivo ca existe. No na crial automaticamente')
    print(f'Criando o arquivo....')
    sleep(1.5)
    criar_arquivo(meuArquivo)
    cabecalho_arquivo(meuArquivo)
else:
    print(f'Arquivo di nome {meuArquivo} existe dja')


while True:
    cabecalho('Sistema de registro v1.0')
    resposta_usuario = menu_principal(
        ['Ver Pessoas Registradas', 'Registrar Nova Pessoa', 'Sair do Programa'])

    if resposta_usuario == 1:
        cabecalho('Ver Pessoas Registradas')
        mostrar_dados_arquivo(meuArquivo=meuArquivo)
        print()
    elif resposta_usuario == 2:
        cabecalho('Registrar Nova Pessoa')
        while True:
            nomePessoa = ler_nome('Nome: ')
            idade = ler_numero_inteiro('Idade: ')
            pais = ler_pais('Pais de Origem: ')
            inserir_dados_arquivo(meuArquivo, nome=nomePessoa, idade=idade, pais=pais)
            print()
            linha()
            resposta = ' '
            while resposta not in 'sn':
                resposta = str(input('Bu misti adiciona mais? [S/N]: ')).strip().lower()[0]
            if resposta == 'n':
                break
    elif resposta_usuario == 3:
        print('Finalizando programa... Volte sempre 🫠')
        sleep(1)
        break
    else:
        print(f'\033[31mErro: Digita um dos opcoes acima. Tenta di nobo 😉 \033[m')
