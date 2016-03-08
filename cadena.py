import re

def extrae(texto):
    lista = []
    try:
        lista1 = re.findall('href=".+?"', texto)
        lista2 = re.findall('src=".+?"', texto)
        lista4 = re.findall('"https:.+?"', texto)
        lista3 = re.findall('"http:.+?"', texto)
        lista = lista1 + lista2 + lista3 + lista4 
        return lista
    except:
        print("Error al dar de alta el registro")

def contarCaracter(cadena, letra):
    contador = 0
    for l in cadena:
        if l == letra:
            contador = contador + 1
    return contador
