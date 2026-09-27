# Un profesor de lingüística quiere clasificar un listado de palabras agrupando 
# aquellas que contengan exactamente las mismas letras (anagramas).
#
# Escribe la función `agrupar_anagramas(lista_palabras)` que reciba una lista como 
# ["roma", "amor", "losa", "mora", "sola"] y retorne una lista de listas con los 
# grupos formados: [["roma", "amor", "mora"], ["losa", "sola"]].

def agrupar_anagramas(palabras: list[str]) -> list[list[str]]:
    claves = []   # guardará las firmas ordenadas (ej: "amor")
    anagramas = []   # guardará las listas de palabras agrupadas (ej: [["roma", "amor"]])

    for palabra in palabras:
        clave = "".join(sorted(palabra.lower())) # palabra ordenada, sirve como id

        if clave in claves: # ya hay un anagrama registrado
            idx = claves.index(clave)
            anagramas[idx].append(palabra) # agregamos la palabra a la sublista
        else: # no hay anagramas registrados
            claves.append(clave)
            anagramas.append([palabra]) # creamos una sublista con el elemento

    return anagramas


if __name__ == "__main__":
    palabras = ["roma", "amor", "perro", "mora", "prore", "ramo", "Ruta", "tUra"]
    
    resultado = agrupar_anagramas(palabras)
    print("Lista original:", palabras)
    print("Grupos de anagramas:", resultado)
