import random

def gera_jogo(palavras):
    palavra_sorteada = random.choice(palavras)
    jogo = {
        'n': len(palavra_sorteada),
        'tentativas': len(palavra_sorteada) + 1,
        'especuladas': [],
        'sorteada': palavra_sorteada
    }
    return jogo

def verifica_posicao(jogo, palavra_especulada):
    if len(jogo['sorteada']) != len(palavra_especulada):
        return []
    
    resultado = []
    for i in range(len(jogo['sorteada'])):
        if palavra_especulada[i] == jogo['sorteada'][i]:
            resultado.append('\033[34m' + palavra_especulada[i] + '\033[0m')  # A letra está na posição correta (azul)
        elif palavra_especulada[i] in jogo['sorteada']:
            resultado.append('\033[33m' + palavra_especulada[i] + '\033[0m')  # A letra existe na palavra sorteada, mas não está na posição correta (amarelo)
        else:
            resultado.append('\033[30m' + palavra_especulada[i] + '\033[0m')  # A letra não existe na palavra sorteada (cinza)
    return resultado

def joga_termo():
    palavras = ['sabor', 'doce', 'risco', 'poder', 'salsa']  # Lista de palavras válidas
    jogo = gera_jogo(palavras)
    
    print('Bem-vindo ao Insper Termo!')
    print('Estou pensando em uma palavra de', jogo['n'], 'letras.')
    print('Você tem', jogo['tentativas'], 'tentativas para adivinhar a palavra.')
    
    for tentativa in range(jogo['tentativas']):
        palavra_especulada = input('Digite sua palavra especulada: ')
        jogo['especuladas'].append(palavra_especulada)
        
        resultado = verifica_posicao(jogo, palavra_especulada)
        print('Resultado:', ''.join(resultado))
        
        # Imprime a tabela com o número de letras e o número de tentativas restantes
        print('Número de letras:', jogo['n'])
        print('Tentativas restantes:', jogo['tentativas'] - tentativa - 1)
        
        if palavra_especulada == jogo['sorteada']:
            print('Parabéns, você adivinhou a palavra!')
            return
    
    print('Você não conseguiu adivinhar a palavra. A palavra era:', jogo['sorteada'])

joga_termo()
