# Una app de música te pide implementar la lógica de su playlist colaborativa.
# Los usuarios pueden agregar canciones, ver segmentos de la lista,
# reproducir bloques y generar "versiones alternativas" de la playlist (mix, invertida, etc).
#
# Datos:
# - canciones: lista de tuplas con la forma (titulo, artista, duracion_segundos).
#   No pueden existir dos canciones con el mismo título.
#
# Recordatorio de slicing: 
#   canciones[inicio:fin]   -> desde 'inicio' hasta 'fin' - 1
#   canciones[inicio:]      -> desde 'inicio' hasta el final
#   canciones[:fin]         -> desde el inicio hasta 'fin' - 1
#   canciones[::paso]       -> todos, tomando uno cada 'paso'
#   canciones[-n:]          -> los últimos n
#   canciones[::-1]         -> invertida
#   del canciones[:n]       -> elimina los primeros n

canciones: list[tuple[str, str, int]] = [
    ("The Fox (What Does The Fox Say?)", "Ylvis", 214),
    ("Dumb Ways to Die", "The Gregory Brothers", 187),
    ("Loonboon", "Laura Shigihara", 107),
    ("All Star", "Smash Mouth", 200),
    ("Pizzatron 3000", "Club Penguin", 119),
    ("Renai Circulation", "Honeypia", 255),
    ("Angry Birds Theme", "Ari Pulkkinen", 68),
    ("Five Night at Freddy's", "The Living Tombstone", 226),
    ("Revenge", "captainsparklez", 220),
    ("Don't Mine at Night - Minecraft Parody", "Brad Knauber", 217)
]


def buscar_cancion(titulo: str) -> int:
    """
    Busca una canción por su título (insensible a mayúsculas/minúsculas).
    Retorna el índice de la canción en 'canciones', o -1 si no existe.
    """
    titulo_limpio = titulo.strip().lower()

    for i in range(len(canciones)):
        if canciones[i][0].lower() == titulo_limpio:
            return i

    return -1


def agregar_cancion(titulo: str, artista: str, duracion: int) -> bool:
    """
    Agrega una canción al final de la playlist con la forma
    (titulo, artista, duracion_segundos).
    No agrega si el título ya existe (insensible a mayúsculas/minúsculas)
    o si 'duracion' es menor o igual a 0.
    Retorna True si la canción fue agregada, False en caso contrario.
    """
    if duracion <= 0:
        return False

    if buscar_cancion(titulo) != -1:
        return False

    canciones.append((titulo.strip(), artista.strip(), duracion))

    return True


def obtener_segmento(inicio: int, fin: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de las canciones entre 'inicio' (incluido)
    y 'fin' (excluido).
    OJO: si un índice se sale de rango, slicing lo ajusta solo (no lanza error).
    """
    titulos: list[str] = []

    for titulo, _, _ in canciones[inicio:fin]:  # slicing: desde 'inicio' hasta 'fin' - 1
        titulos.append(titulo)

    return titulos


def ultimas_canciones(n: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de las últimas 'n' canciones de la playlist.
    Si 'n' es menor o igual a 0, retorna una lista vacía.
    Si 'n' es mayor que la cantidad de canciones, retorna todas.
    """
    if n <= 0:
        return []

    titulos: list[str] = []

    for titulo, _, _ in canciones[-n:]:  # slicing: los últimos n
        titulos.append(titulo)

    return titulos


def crear_mix(paso: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de una canción de cada 'paso', partiendo por
    la primera. Ejemplo: paso = 2 -> canción 0, 2, 4, ...
    Si 'paso' es menor a 1, retorna una lista vacía.
    """
    if paso < 1:
        return []

    titulos: list[str] = []

    for titulo, _, _ in canciones[::paso]:  # slicing: uno de cada 'paso'
        titulos.append(titulo)

    return titulos


def invertir_orden() -> list[str]:
    """
    [SLICING] Retorna los títulos de la playlist en orden inverso,
    sin modificar la lista original.
    """
    titulos: list[str] = []

    for titulo, _, _ in canciones[::-1]:  # slicing: secuencia invertida
        titulos.append(titulo)

    return titulos


def resumen() -> tuple[int, int, int]:
    """
    Retorna una tupla con el estado de la playlist:
    (cantidad de canciones, duración total en segundos, duración promedio entera).
    Si la playlist está vacía, retorna (0, 0, 0).
    """
    duracion_total = 0

    for _, _, duracion in canciones:
        duracion_total += duracion

    cantidad = len(canciones)

    if cantidad == 0:
        return 0, 0, 0

    return cantidad, duracion_total, duracion_total // cantidad


if __name__ == "__main__":
    print("\n#=====> BUSCAR Y AGREGAR CANCIONES <=====#")
    print(f"Playlist inicial: {canciones}")

    print(f"\nÍndice de 'Loonboon': {buscar_cancion('Loonboon')}")
    print(f"Índice de 'Nyan Cat Theme': {buscar_cancion('Nyan Cat Theme')}")

    print(f"\n¿Se agregó 'Nyan Cat Theme'?: {agregar_cancion('Nyan Cat Theme', 'Homme', 112)}")
    print(f"Playlist actual: {canciones}")

    print("\n#=====> SEGMENTOS DE LA PLAYLIST <=====#")
    print(f"Segmento [1:4]: {obtener_segmento(1, 4)}")
    print(f"Últimas 2 canciones: {ultimas_canciones(2)}")

    print("\n#=====> MIX E INVERSIÓN <=====#")
    print(f"Mix (una de cada 2): {crear_mix(2)}")
    print(f"Playlist invertida: {invertir_orden()}")
    print(f"La playlist original no cambió: {canciones}")

    print("\n#=====> RESUMEN <=====#")
    print(f"Resumen (cantidad, total, promedio): {resumen()}")

    print("\n[ Playlist final ]")
    for titulo, artista, duracion in canciones:
        print(f"  - {titulo} - {artista} ({duracion}s)")
