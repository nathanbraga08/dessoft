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
    print('Bem-vindo ao Insper Termo!')
    print('Neste jogo, estou pensando em uma palavra de 5 letras.')
    print('Você tem 6 tentativas para adivinhar a palavra.')
    print('Após cada tentativa, vou te dar algumas dicas:')
    print('- Se a letra da palavra que você especulou está na posição correta da palavra que pensei, vou mostrar a letra em azul.')
    print('- Se a letra existe na palavra que pensei, mas não está na posição correta, vou mostrar a letra em amarelo.')
    print('- Se a letra não existe na palavra que pensei, vou mostrar a letra em cinza.')
    print('Vamos começar o jogo!')
    
    palavras = ['sabor', 'doce', 'risco', 'poder', 'salsa']  # Lista de palavras válidas
    jogo = gera_jogo(palavras)
    
    for tentativa in range(jogo['tentativas']):
        palavra_especulada = input('Digite sua palavra especulada: ')
        jogo['especuladas'].append(palavra_especulada)
        
        resultado = verifica_posicao(jogo, palavra_especulada)
        print('Resultado:', ''.join(resultado))
        
        if palavra_especulada == jogo['sorteada']:
            print('Parabéns, você adivinhou a palavra!')
            return
    
    print('Você não conseguiu adivinhar a palavra. A palavra era:', jogo['sorteada'])

joga_termo()
