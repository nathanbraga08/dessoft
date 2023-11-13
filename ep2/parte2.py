import random

def inicializa(palavras):
    # Escolhe uma palavra aleatória da lista
    palavra_sorteada = random.choice(palavras)
    
    # Cria o dicionário com as informações do jogo
    jogo = {
        'n': len(palavra_sorteada),
        'tentativas': len(palavra_sorteada) + 1,
        'especuladas': [],
        'sorteada': palavra_sorteada
    }
    
    return jogo
