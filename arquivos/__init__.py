from interface import linha


# Es i pa djubih si arquivo existe ou nao
def arquivo_existe(meuArquivo):
    try:
        arquivo = open(meuArquivo, 'rt')
        arquivo.close()
    except (FileExistsError, FileNotFoundError):
        # Si arquivo ca foi encontrado i na da erro, logo no na retorna falso
        return False
    else:
        # Si arquivo existe i foi encontrado, i na retorna verdadeiro
        return True


# Es i pa cria arquivo
def criar_arquivo(meuArquivo):
    try:
        arquivo = open(meuArquivo, 'wt+')
        arquivo.close()
    except:
        print('\033[31mHouve um erro na hora di cria arquivo\033[m')
    else:
        print(f'Arquivo {meuArquivo} foi criado com sucesso')


# Li gos no na bai mostra algo ku sta dentro di arquivo
def mostrar_dados_arquivo(meuArquivo):
    try:
        arquivo = open(meuArquivo, 'rt')
    except (FileExistsError, FileNotFoundError):
        print(f'\033[31mHouve um erro, no ca sta na consegui mostra nada!\033[m')
    else:
        # Si arquivo existe i foi encontrado, logo i na mostra algo ku sta dentro di arquivo
        print(arquivo.read())
    finally:
        arquivo.close()


# Li no na bai inseri dados dentro di arquivo, i na recebi nome, idade, pais de origem
def inserir_dados_arquivo(meuArquivo, nome='<desconhecido>', idade=0, pais='<Sem pais>'):
    try:
        arquivo = open(meuArquivo, 'at')
    except (FileExistsError, FileNotFoundError):
        print(f'\033[31mErro! Ica foi possivel adiciona dado na lista!\033[m')
    else:
        # Li no na bai adiciona que ku passado pa usuario dentro di arquivo, dps no quebra linha
        arquivo.write(f'\n{nome:<15} {idade:<10} {pais:>25}')
        print()
        print(f'{nome} foi adicionado com sucesso 😊')
    finally:
        arquivo.close()


# Es i pa adiciona cabecalho dentro di ficheiro:
def cabecalho_arquivo(meuArquivo):
    try:
        arquivo = open(meuArquivo, 'at')
    except (FileExistsError, FileNotFoundError):
        print(f'\033[31mErro! Ica foi possivel adiciona dado na lista!\033[m')
    else:
        arquivo.write(f'{"Nome":<15} {"Idade":<10} {"Pais de Origem":>25}\n')
        arquivo.write('~' * 55)
        print()
        
    finally:
        arquivo.close()
