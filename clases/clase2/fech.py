# Estás creando el sistema para procesar los votos de una elección estudiantil. 
# Recibes una lista de strings con los nombres de los candidatos votados 
# (ej: ["Ana", "Bob", "ANA", "  bob ", "Nulo", "Ana"]).
#
# Debes escribir una función `procesar_votos(votos: list[str])` que cuente los votos de cada 
# candidato e identifique al ganador o si hubo empate.
#
# RESTRICCIÓN:
#   - NO puedes usar diccionarios (`{}`) ni conjuntos (`set()`). 
#   - Debes resolverlo únicamente con listas, tuplas y manipulación de strings/métodos de listas.

# Contadores
candi = []
conte = []

# Funciones
def procesar_candi(votos):
    for cand in votos:
        if cand.upper() not in candi:
            candi.append(cand.upper())

def procesar_votos(votos):
    for voto in votos:
        i = candi.index(voto.upper())
        conte[i] += 1
