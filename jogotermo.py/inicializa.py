from random import choice
from colorama import init, Fore, Back, Style
global palavras

def filtra(palavras, numeroletras):
    nlist = []
    palavras_normalizada = []
    for palavra in palavras:
        palavra_normalizada = palavra.lower()
        palavras_normalizada.append(palavra_normalizada)
    for palavra in palavras_normalizada:
        if len(palavra) == int(numeroletras) and palavra not in nlist:
            nlist.append(palavra.lower())
    return nlist

def inicializa(listapalavras):
    return {'n' : int(len(listapalavras[0])),
    'sorteada' : choice(listapalavras),
    'especuladas' : [],
    'tentativas' : len(listapalavras[0]) + 1
    }

