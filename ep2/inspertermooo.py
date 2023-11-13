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
    print('Bem Vindo ao termo')
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
            
            
    while True:
        if tentativas == 0:
            print('Você infezlimente perdeu! \n A resposta era: ' + sorteada)
            print('Sua pontuação final foi 0 pontos')
            break
        print('Voce tem {0} tentativas.'.format(tentativas))
        chute = input('Qual o seu palpite? ').strip().lower()
        if chute.lower() == 'desisto':
            break
        if len(chute) != int(qletras):
            print('Somente palavras de 5 letras')
        elif chute not in palavrassolucao.palavras:
            print('Palavra desconhecida.')
        elif chute in especuladas:
            print('Palavra já escolhida.')
        else:
            especuladas.append(chute)
            for i in range(6):
                if i < len(especuladas):
                    termo(especuladas[i])
                else:
                    termo('')
            if chute == sorteada and tentativas == 5:
                print('Você ganhou!')
                print('Sua pontuação é de 10 pontos')
                break
            if chute == sorteada and tentativas == 4:
                print('Você ganhou!')
                print('Sua pontuação é de 8 pontos')
                break
            if chute == sorteada and tentativas == 3:
                print('Você ganhou!')
                print('Sua pontuação é de 6 pontos')
                break
            if chute == sorteada and tentativas == 2:
                print('Você ganhou!')
                print('Sua pontuação é de 4 pontos')
                break
            if chute == sorteada and tentativas == 1:
                print('Você ganhou!')
                print('Sua pontuação é de 2 pontos')
                break
            tentativas -= 1
            
            

    rejogar = input('Deseja jogar novamente? (sim/nao): ').strip().lower()

    if rejogar == 'sim':
        continue
    else:
        print('Ate mais!')
        break