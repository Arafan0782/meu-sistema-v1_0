
# Es i pa seta lei so numero inteiro, td cusssa ki ca numero inteiro i cana passa.
def ler_numero_inteiro(expressao):
    while True:
        try:
            numero = int(input(expressao))
        except (TypeError, ValueError):
            print(
                f'\033[31mErro: Digita um numero valido sff. Tenta novamnete \033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuario preferi ca digita nada.\033[m')
            return 0
        else:
            return numero


# li es i pa i seta recebi so strings, td cussa ku ca string i na da erro
def ler_pais(texto):
    # staTudoBem = False
    while True:
        try: 
            expressao = str(input(texto)).strip()
            # Li no na djubih si cussa ku digitado si tene so letras
            if expressao.isalpha():
                return expressao
            
            # Li no na djubih si cussa ku digitado si i sta vazio, si i sta no na retorna algo ()
            elif expressao == '':
                return '<Pais sem nome>'
            
            # Li no na djubih si cussa ku digitado si tene numero, si i tene i no na mostra erro
            elif expressao.isalnum():
                for letra in expressao:
                    if letra[0].isnumeric():
                        print(
                            f'\033[31mErro: Nim um nome di pais ca ta escrevido ku numero! Tenta novamnete. \033[m')
                        break
                    
            # Si nada di riba ca sedo, i pb i sta td bem, no na retorna so expressao ku passado
            else:
                return expressao
        except KeyboardInterrupt:
            print(f'\033[31mUsuario preferi ca digita nada.\033[m')
            return '<Sem pais>'
        
            



def ler_nome(texto):
    while True:
        try:
            expressao = str(input(texto))
        except (TypeError, ValueError):
            print(
                f'\033[31mErro: Digita string valido sff. Tenta novamnete \033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuario preferi ca digita nada.\033[m')
            return '<desconhecido>'
        else:
            return expressao

    

# Pa testa funcao si na tarbadja drito ku mangas di hipoteses...
# nomePais = ler_string('Digite nome di bu pais: ')
# print(f'Bu digita {nomePais}. Fim!')

# nome = ler_string('Nome: ')