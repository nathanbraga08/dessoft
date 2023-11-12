import re

def filtra(lista, num_letras):
    lista = [re.sub('^[^a-z]*|[^a-z]*$', '', palavra.lower()) for palavra in lista]
    lista = [palavra for palavra in lista if len(palavra) == num_letras]
    lista = list(set(lista))
    
    return lista

print(filtra)