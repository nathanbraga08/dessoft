'''a = 0
b = 1
print(a+b)'''

def troca_nome(texto,dicionario):
    for texto, metonimia in dicionario.items():
        if metonimia in dicionario:
            substitui = len(metonimia)
            novo_text = texto(f'(metonimia:_*substitui)')
    return novo_text

print(troca_nome(texto = "Adicione uma colher de sopa de Maizena a dois copos de leite e leve ao fogo baixo, mexendo sempre. Ao final, acrescente o leite Moça.", dicionario = {'Leite Moça': 'leite condensado','Leite Ninho': 'leite em pó','Maizena': 'amido de milho',}))