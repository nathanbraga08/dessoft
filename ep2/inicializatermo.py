import random

def inicializa(palavras):
    palavra_sorteada = random.choice(palavras)
    jogo = {
        'n': len(palavra_sorteada),
        'tentativas': len(palavra_sorteada) + 1,
        'especuladas': [],
        'sorteada': palavra_sorteada
    }
    
    return jogo