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

def procesar_votos(votos: list[str]) -> tuple[str, int] | tuple[list[str], int]:
    """
    Retorna el nombre del ganador y su cantidad de votos.
    En caso de empate, retorna el nombre de todos quienes hayan empatado y sus votos
    """
    if not votos:
        return ("", 0)

    # los votos del candidato[i], se guardan en conteos[i]
    candidatos = [] # Candidatos normalizados
    conteos = []    # votos de candidatos

    # Conteo de votos
    for voto in votos:
        nombre = voto.strip().capitalize() # normalización
        
        if nombre in candidatos: # se suma un conteo
            idx = candidatos.index(nombre)
            conteos[idx] += 1
        else: # se agrega un candidato
            candidatos.append(nombre)
            conteos.append(1)

    max_votos = max(conteos) # máxima cantidad de votos

    # Quienes tienen la máxima cantidad de votos
    ganadores = []
    for i in range(len(conteos)):
        if conteos[i] == max_votos:
            ganadores.append(candidatos[i]) # Agregamos el NOMBRE del candidato

    # Determinar resultado
    if len(ganadores) > 1:
        return (ganadores, max_votos)

    return (ganadores[0], max_votos)


if __name__ == "__main__":
    # Ejemplo 1: Empate entre Ana y Bob (3 votos cada uno)
    votos_empate = ["Ana", "  bob ", "ANA", "Bob", "Carlos", "Ana", "bob"]
    empate, votos_max = procesar_votos(votos_empate)
    
    print("--- Ejemplo Empate ---")
    print(f"Votos procesados: {votos_empate}")
    print(f"Resultado: {empate} con {votos_max} votos")
    
    # Ejemplo 2: Ganador único (Ana con 4 votos)
    votos_ganador = ["Ana", "  bob ", "ANA", "Bob", "Carlos", "Ana", "ANA"]
    ganador, votos_max = procesar_votos(votos_ganador)
    
    print("\n--- Ejemplo Ganador Único ---")
    print(f"Votos procesados: {votos_ganador}")
    print(f"Resultado: {ganador} con {votos_max} votos")
