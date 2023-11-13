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