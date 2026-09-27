# Un profesor de lingüística quiere clasificar un listado de palabras agrupando 
# aquellas que contengan exactamente las mismas letras (anagramas).
#
# Escribe la función `agrupar_anagramas(lista_palabras)` que reciba una lista como
# ["roma", "amor", "losa", "mora", "sola"] y retorne una lista de listas con los
# grupos formados: [["roma", "amor", "mora"], ["losa", "sola"]].

# Listas
palabrasort = []
anagramas = []

# Funciones
def definir_palabras(lista_p):
    for palabra in lista_p:
        palabra_ord = "".join(sorted(palabra))
        if palabra_ord not in palabrasort:
            palabrasort.append(palabra_ord)


def agrupar_anagramas(lista_p, palabrasort):
    for palabra in lista_p:
        i = palabrasort.index("".join(sorted(palabra)))

        if i >= len(anagramas):
            anagramas.append([palabra])
        else:
            anagramas[i].append(palabra)
