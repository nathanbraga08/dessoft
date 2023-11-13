import palavrassolucao
from random import choice
from colorama import init, Fore, Back, Style
init(autoreset=True)

while True:

    qletras = 5 
    filtandopalavras = palavrassolucao.filtra2(qletras) 
    inicializa = palavrassolucao.inicializa(filtandopalavras)
    tentativas = inicializa['tentativas']
    especuladas = inicializa['especuladas']
    
    print('')
    print('Bem Vindo ao neurotermo')
    print('')
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