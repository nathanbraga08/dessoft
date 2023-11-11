def inidica_posicao(input_dict):
    # Verifica se o tamanho das palavras diverge
    if len(input_dict['palavra_sorteada']) != len(input_dict['palavra_especulada']):
        return []
    
    resultado = []
    for i in range(len(input_dict['palavra_sorteada'])):
        if input_dict['palavra_especulada'][i] == input_dict['palavra_sorteada'][i]:
            # A letra está na posição correta
            resultado.append(0)
        elif input_dict['palavra_especulada'][i] in input_dict['palavra_sorteada']:
            # A letra existe na palavra sorteada, mas não está na posição correta
            resultado.append(1)
        else:
            # A letra não existe na palavra sorteada
            resultado.append(2)
    return resultado
