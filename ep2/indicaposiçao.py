def inidica_posicao(psorteada, pespeculada):
    if len(psorteada) != len(pespeculada):
        return []
    
    solucao = []
    for i in range(len(psorteada)):
        if psorteada[i] == pespeculada[i]:
            solucao.append(0)  
        elif pespeculada[i] in psorteada:
            solucao.append(1)  
        else:
            solucao.append(2)  

    return solucao