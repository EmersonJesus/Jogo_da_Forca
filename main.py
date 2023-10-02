################################################
##### PROGRAMADO POR: EMERSON C. JESUS     #####
################################################

from sistema import *
from random import randint

arq = 'palavras.txt'
if not arqexiste(arq):
    criararquivo(arq)
    
while True:
    arquivo = open(arq, 'r')
    palavras = arquivo.readlines()
    arquivo.close()
    sorteio = randint(0, len(palavras)-1)
    secreto = palavras[sorteio].replace('\n', '').strip().upper()
    opc = ['JOGAR', 'ADICIONAR PALAVRAS', 'SAIR']
    menu(opc)
    escolha = leiaInt('Sua opção: ') 
    match escolha:
        case 1:
            jogo(secreto)
            while True:
                i = str(input('Você quer continuar jogando? [S/N]: ')).strip().upper()
                if i == 'S' or i == 'N':
                    break
                else:
                    print('DIGITE UMA OPÇÃO VÁLIDA!')
            if i == 'S':
                limpatela()
            else:
                print(linha())
                mensagem('SAINDO DO PROGRAMA...')
                break
        case 2:
            arquivo = open(arq, 'a+')
            addpalavras(arquivo)
            arquivo.close()
            mensagem('Palavra Adicionada com sucesso!')
        case 3:
            mensagem('SAINDO DO PROGRAMA...')
            break
        case _:
            print('ERRO, OPÇÃO INVALIDA!')