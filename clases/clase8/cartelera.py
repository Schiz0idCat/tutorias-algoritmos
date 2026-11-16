# Un cine te pide implementar la lógica de su cartelera y venta de entradas.
# Los clientes pueden consultar películas, comprar entradas, aprovechar cambios
# de precio y revisar segmentos de la cartelera (películas disponibles, orden
# invertido, recaudación por sala, etc).
#
# Datos:
# - cartelera: diccionario que asocia el título de una película con una tupla
#   con la forma (sala, precio, asientos_disponibles).
#   No pueden existir dos películas con el mismo título.
#
# Recordatorio de diccionarios:
#   cartelera[clave]        -> valor asociado a la clave
#   clave in cartelera      -> True si la clave existe, False si no
#   cartelera.get(clave)    -> valor asociado, o None si no existe
#   cartelera.keys()        -> todas las claves
#   cartelera.items()       -> pares (clave, valor)
#   del cartelera[clave]    -> elimina la clave y su valor
#   len(cartelera)          -> cantidad de claves
#
# Recordatorio de slicing (sobre una lista de títulos):
#   titulos[inicio:fin]   -> desde 'inicio' hasta 'fin' - 1
#   titulos[inicio:]      -> desde 'inicio' hasta el final
#   titulos[:fin]         -> desde el inicio hasta 'fin' - 1
#   titulos[::paso]       -> todos, tomando uno cada 'paso'
#   titulos[-n:]          -> los últimos n
#   titulos[::-1]         -> invertida

cartelera: dict[str, tuple[str, int, int]] = {
    "Dune: Parte Dos": ("Sala 1", 6500, 40),
    "Inside Out 2": ("Sala 2", 5500, 25),
    "Deadpool & Wolverine": ("Sala 3", 7000, 0),
    "Oppenheimer": ("Sala 1", 6000, 12),
    "Barbie": ("Sala 2", 5000, 8),
}


def buscar_pelicula(titulo: str) -> str | None:
    """
    Busca una película por su título (insensible a mayúsculas/minúsculas).
    Ignora los espacios sobrantes al inicio y al final del título.
    Retorna el título tal como está guardado en 'cartelera', o None si no existe.
    """
    upper = titulo.upper().strip()
    for key, _ in cartelera.items():
        if upper == key.upper():
            return key

    return None


def agregar_pelicula(titulo: str, sala: str, precio: int, asientos: int) -> bool:
    """
    Agrega una película a la cartelera con la forma (sala, precio, asientos).
    No agrega si el título ya existe (insensible a mayúsculas/minúsculas),
    si 'titulo' o 'sala' están vacíos, si 'precio' es menor o igual a 0 o si
    'asientos' es negativo.
    Retorna True si la película fue agregada, False en caso contrario.
    """
    if buscar_pelicula(titulo) == None or titulo.strip() == "" or sala.strip() == "" or precio <= 0 or asientos < 0:
        return False

    cartelera[titulo] = (sala, precio, asientos)

    return True



def comprar_entradas(titulo: str, cantidad: int) -> int:
    """
    Vende 'cantidad' entradas para la película indicada, descontando los
    asientos disponibles.
    Solo se puede vender si la película existe, 'cantidad' es mayor que 0 y
    hay asientos suficientes.
    Retorna el total pagado (precio * cantidad), o -1 si la venta no se pudo
    realizar.
    """
    
    if buscar_pelicula(titulo) != None or cantidad <= 0:
        return -1

    sala, precio, asientos = cartelera[titulo]

    if asientos < cantidad:
        return -1

    cartelera[titulo] = (sala, precio, asientos - cantidad)

    return precio * cantidad



def cambiar_precio(titulo: str, nuevo_precio: int) -> bool:
    """
    Cambia el precio de una película existente.
    Solo se puede cambiar si la película existe y 'nuevo_precio' es mayor que 0.
    Retorna True si el cambio fue exitoso, False en caso contrario.
    """
    if buscar_pelicula(titulo) == None or nuevo_precio <= 0:
        return False

    sala, _, asientos = cartelera[titulo]
    cartelera[titulo] = (sala, nuevo_precio, asientos)
    
    return True


def cancelar_funcion(titulo: str) -> bool:
    """
    Elimina una película de la cartelera.
    Retorna True si la película existía y fue eliminada, False en caso contrario.
    """
    if buscar_pelicula(titulo) == None:
        return False

    del cartelera[titulo]
    return True


def peliculas_disponibles() -> list[str]:
    """
    Retorna los títulos de las películas que tienen al menos 1 asiento disponible,
    en el orden en que aparecen en la cartelera.
    """
    disponibles = []

    for titulo, (_, _, asientos) in cartelera.items():
        if asientos > 0:
            disponibles.append(titulo)

    return disponibles


def obtener_segmento(inicio: int, fin: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de las películas entre 'inicio' (incluido)
    y 'fin' (excluido).
    OJO: si un índice se sale de rango, slicing lo ajusta solo (no lanza error).
    """
    titulos = []

    for titulo, _ in cartelera.items():
        titulos.append(titulo)

    return titulos[inicio:fin]


def invertir_cartelera() -> list[str]:
    """
    [SLICING] Retorna los títulos de la cartelera en orden inverso,
    sin modificar el diccionario original.
    """
    titulos = []

    for titulo, _ in cartelera.items():
        titulos.append(titulo)

    return titulos[::-1]


def recaudacion_por_sala() -> dict[str, int]:
    """
    Retorna un diccionario que asocia cada sala con la recaudación potencial
    de sus películas, calculada como precio * asientos_disponibles.
    Las salas sin películas no aparecen; las salas con películas agotadas
    aparecen con recaudación 0.
    """
    
    recaudacion = {}
    
    for titulo, (_, precio, asientos) in cartelera.items():
        recaudacion[titulo] = precio * asientos

    return recaudacion



def resumen() -> tuple[int, int, int]:
    """
    Retorna una tupla con el estado de la cartelera:
    (cantidad de películas, asientos disponibles totales, recaudación potencial total).

    - recaudación potencial: suma de precio * asientos_disponibles de cada película.

    Si la cartelera está vacía, retorna (0, 0, 0).
    """
    total_pelis = len(cartelera)
    if total_pelis == 0:
        return (0, 0, 0)

    precios_total = 0
    asientos_totales = 0

    for _, (_, precio, asientos) in cartelera.items():
        precios_total += precio * asientos
        asientos_totales += asientos 
    
    return (total_pelis, precios_total, asientos_totales)


if __name__ == "__main__":
    print("\n#=====> BUSCAR Y AGREGAR PELÍCULAS <=====#")
    print(f"Cartelera inicial: {cartelera}")

    print(f"\nTítulo encontrado para '  inside out 2 ': {buscar_pelicula('  inside out 2 ')}")
    print(f"Título encontrado para 'Minecraft': {buscar_pelicula('Minecraft')}")

    print(f"\n¿Se agregó 'Minecraft'?: {agregar_pelicula('Minecraft', 'Sala 4', 5000, 30)}")
    print(f"¿Se agregó 'Dune: Parte Dos' de nuevo?: {agregar_pelicula('dune: parte dos', 'Sala 1', 6500, 40)}")
    print(f"¿Se agregó una película con precio inválido?: {agregar_pelicula('Megamind', 'Sala 4', 0, 20)}")
    print(f"Cartelera actual: {cartelera}")

    print("\n#=====> VENTA DE ENTRADAS <=====#")
    print(f"¿Se vendieron 3 entradas para Dune?: {comprar_entradas('Dune: Parte Dos', 3)}")
    print(f"Asientos restantes de Dune: {cartelera['Dune: Parte Dos'][2]}")
    print(f"¿Se vendió 1 entrada para Deadpool (agotada)?: {comprar_entradas('Deadpool & Wolverine', 1)}")
    print(f"¿Se vendieron 100 entradas para Inside Out 2?: {comprar_entradas('Inside Out 2', 100)}")

    print("\n#=====> CAMBIOS EN LA CARTELERA <=====#")
    print(f"¿Se cambió el precio de Oppenheimer?: {cambiar_precio('Oppenheimer', 6500)}")
    print(f"¿Se cambió el precio de Barbie a -1?: {cambiar_precio('Barbie', -1)}")
    print(f"¿Se canceló Deadpool & Wolverine?: {cancelar_funcion('Deadpool & Wolverine')}")
    print(f"¿Se canceló Deadpool & Wolverine otra vez?: {cancelar_funcion('Deadpool & Wolverine')}")

    print("\n#=====> SEGMENTOS Y DISPONIBILIDAD <=====#")
    print(f"Películas disponibles: {peliculas_disponibles()}")
    print(f"Segmento [1:4]: {obtener_segmento(1, 4)}")
    print(f"Cartelera invertida: {invertir_cartelera()}")
    print(f"La cartelera original no cambió: {cartelera}")

    print("\n#=====> RECAUDACIÓN Y RESUMEN <=====#")
    print(f"Recaudación por sala: {recaudacion_por_sala()}")
    print(f"Resumen (películas, asientos, recaudación): {resumen()}")

    print("\n[ Cartelera final ]")
    for titulo, (sala, precio, asientos) in cartelera.items():
        print(f"  - {titulo} | {sala} | ${precio} | Asientos: {asientos}")
