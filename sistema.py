import os

def limpatela():
    os.system('clear' if os.name == 'posix' else 'cls')

def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg).strip()
        try:
            valor = int(n)
        except (TypeError, ValueError):
            print('ERRO! Digite uma opção válida.')
        else:
            break
    return valor 

def linha(tam=42):
    return '='*tam

def mensagem(msg, tam=42):
    print(f'{msg}'.center(42))

def menu(lista):
    print(linha())
    mensagem('JOGO DA FORCA')
    print(linha())
    c = 1
    for item in lista:
        print(f'{c:>15} - {item}')
        c += 1
    print(linha())
    
def arqexiste(arq):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(arq):
    try:
        arquivo = open(arq, 'wt+')
    except FileExistsError:
        print('Arquivo já existe!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')
        arquivo.close()
        
def jogo(secreto):
    digitadas = []
    chances = 5
    sececreto_temp = palavrasecreta(digitadas, secreto)
    limpatela()
    while True:
        print(f'Você tem {chances} chances.')
        print(linha())
        print(f'A palavra secreta: {sececreto_temp}')
        print(linha())
            
        letra = str(input('Digite uma letra: ')).strip().upper()
        
        if len(letra) > 1:
            print('ERRO, Não vale digitar mais de uma letra.')
        else:
            if letra in digitadas:
               print('Você já chutou essa letra!')
            else: 
                digitadas.append(letra)
                if letra not in secreto:
                    chances -= 1
                limpatela()
        
        sececreto_temp = palavrasecreta(digitadas, secreto)
            
        if verificajogo(sececreto_temp, secreto, chances):
            break

def palavrasecreta(digitadas, secreto):
    sececreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            sececreto_temp += letra_secreta
        else:
            sececreto_temp += '_'
    return sececreto_temp

def verificajogo(secreto_temp, secreto, chances):
    if secreto_temp == secreto:
        print('Você venceu e escapou da forca!')
        print(f'A palavra era: {secreto}')
        return True
    else:
         if chances <= 0:
            print('Você perdeu! FORCA!')
            return True      
    return False

def addpalavras(arquivo):
    while True:
        limpatela()
        print(linha())
        mensagem('ADICIONAR PALAVRAS AO JOGO')
        print(linha())
        
        palavra = input('Digite a palavra que deseja adicionar (ou digite "sair" para voltar): ').strip().upper()
        
        if palavra == 'SAIR':
            break
        
        if len(palavra) < 3:
            print('ERRO! A palavra deve ter pelo menos 3 letras.')
        else:
            with open(arquivo, 'at') as arquivo_palavras:
                arquivo_palavras.write(palavra + '\n')
            print(f'Palavra "{palavra}" adicionada com sucesso!')