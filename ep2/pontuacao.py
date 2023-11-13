'''def pontuacao(tentativa):
    if tentativa <= 2:
        pontuacao = 5
    if tentativa == 0:
        pontuacao = 0
    if tentativa > 2:
        pontuacao == 10'''

import palavrassolucao
from random import choice
from colorama import init, Fore, Back, Style
init(autoreset=True)

print('')
print('Bem Vindo ao termo')
print('')

while True:

    qletras = 5 
    filtandopalavras = palavrassolucao.filtra(qletras) 
    inicializa = palavrassolucao.inicializa(filtandopalavras)
    tentativas = inicializa['tentativas']
    especuladas = inicializa['especuladas']
    
    print('Os comandos são: desisto' + '\n')
    print(' ' + 'Regras:'+'\n')
    print('  - Você tem '+ Fore.RED + f'{tentativas}' + Fore.RESET + ' tentativas para acertar uma palavra aleatória de '+f'{qletras}' + ' letras.')
    print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
    print('    ♦ ' + Fore.BLUE+'Azul' + Fore.RESET + ': a letra está na posição correta;')
    print('    ♦ ' + Fore.YELLOW+'Amarelo' + Fore.RESET + ': a palavra tem a letra, mas está na posição errada;')
    print('    ♦ ' + Fore.BLACK+'Cinza' + Fore.RESET + ': a palavra não tem a letra.')
    print('  - Os acentos são ignorados;')
    print('  - As palavras podem possuir letras repetidas.' + '\n')
    print('Sorteando uma palavra...\n')
    print('Já tenho uma palavra! Tente adivinhá-la!')
    sorteada = inicializa['sorteada']
    
    def termo(chute):
            
        retorno = '| '

        if len(chute) > 0:
            cor = palavrassolucao.inidica_posicao(sorteada, chute)
            for i in range(len(chute)):
                if cor[i] == 0:
                    retorno += Fore.BLUE + chute[i] + Fore.RESET
                elif cor[i] == 1:
                    retorno += Fore.YELLOW +  chute[i] + Fore.RESET
                else:
                    retorno += Fore.BLACK + chute[i] + Fore.RESET
                retorno += " | "
        else:
            retorno += '  | ' * 5
        
        print(' ---'*5+'\n'+ retorno)
        print(' ---'*5)
            
            
    while True:
        if tentativas == 0:
            print('Você perdeu! \nA resposta era: ' + sorteada)
            break
        print('Voce tem {0} tentativas!'.format(tentativas))
        chute = input('Qual o seu palpite? ').strip().lower()
        if chute.lower() == 'desisto':
            break
        if len(chute) != int(qletras):
            print('Somente palavras de {0} letras'.format(qletras))
        elif chute not in palavrassolucao.palavras:
            print('Palavra desconhecida.')
        elif chute in especuladas:
            print('Palavra já escolhida!')
        else:
            especuladas.append(chute)
            for i in range(6):
                if i < len(especuladas):
                    termo(especuladas[i])
                else:
                    termo('')
            if chute == sorteada:
                print('Você ganhou!')
                break
            tentativas -= 1
            
            

    rejogar = input('Deseja jogar novamente? (s/n): ').strip().lower()

    if rejogar in ['s','sim','claro']:
        continue
    else:
        print('Ate mais!')
        break
    

