import re

def filtra(lista, num_letras):
    # Normaliza as palavras para minúsculas e remove caracteres especiais no início e fim
    lista = [re.sub('^[^a-z]*|[^a-z]*$', '', palavra.lower()) for palavra in lista]
    
    # Filtra as palavras pelo número de letras
    lista = [palavra for palavra in lista if len(palavra) == num_letras]
    
    # Remove as repetições
    lista = list(set(lista))
    
    return lista

print(filtra)
