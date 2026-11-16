# Una tienda de videojuegos te pide implementar la lógica de su inventario.
# Los clientes pueden consultar juegos, comprar copias, aprovechar descuentos
# y revisar segmentos del catálogo (ofertas, orden invertido, etc).
#
# Datos:
# - inventario: lista de tuplas con la forma (titulo, plataforma, precio, stock).
#   No pueden existir dos juegos con el mismo título.
#
# Recordatorio de slicing (visto en clase 6):
#   inventario[inicio:fin]   -> desde 'inicio' hasta 'fin' - 1
#   inventario[inicio:]      -> desde 'inicio' hasta el final
#   inventario[:fin]         -> desde el inicio hasta 'fin' - 1
#   inventario[::paso]       -> todos, tomando uno cada 'paso'
#   inventario[-n:]          -> los últimos n
#   inventario[::-1]         -> invertida

inventario: list[tuple[str, str, int, int]] = [
    ("Hollow Knight", "PC", 15000, 8),
    ("Celeste", "Switch", 12000, 0),
    ("Hades", "PC", 18000, 5),
    ("Stardew Valley", "Switch", 14000, 3),
    ("Cuphead", "Xbox", 10000, 6),
    ("Undertale", "PC", 8000, 2),
]


def buscar_juego(titulo: str) -> int:
    """
    Busca un juego por su título (insensible a mayúsculas/minúsculas).
    Ignora los espacios sobrantes al inicio y al final del título.
    Retorna el índice del juego en 'inventario', o -1 si no existe.
    """

    for idx in range(len(inventario)):
        if inventario[idx][0].lower() == titulo.lower():
            return idx

    return -1


def agregar_juego(titulo: str, plataforma: str, precio: int, stock: int) -> bool:
    """
    Agrega un juego al final del inventario con la forma
    (titulo, plataforma, precio, stock).
    No agrega si el título ya existe (insensible a mayúsculas/minúsculas),
    si 'titulo' o 'plataforma' están vacíos, si 'precio' es menor o igual a 0 o si 'stock' es negativo.
    Retorna True si el juego fue agregado, False en caso contrario.
    """
    
    if not titulo.strip() or not plataforma.strip() or precio <= 0 or stock < 0:
        return False
    
    for nombre, _, _, _ in inventario:
        if nombre.lower() == titulo.lower():
            return False

    inventario.append((titulo, plataforma, precio, stock))
    return True

def vender_copias(titulo: str, cantidad: int) -> bool:
    """
    Vende 'cantidad' copias del juego indicado, descontándolas del stock.
    Solo se puede vender si el juego existe, 'cantidad' es mayor que 0 y hay stock suficiente.
    Reemplaza la tupla del juego actualizando su stock y retorna True.
    Retorna False en caso contrario.
    """
    
    idx = buscar_juego(titulo)

    if idx == -1 or cantidad <= 0:
        return False
    
    nombre, plat, precio, stock = inventario[idx]

    if stock < cantidad:
        return False

    inventario[idx] = (nombre, plat, precio, stock - cantidad)
    return True

def aplicar_descuento(titulo: str, porcentaje: int) -> bool:
    """
    Aplica un porcentaje de descuento (ej: 10 para 10%) sobre el precio del juego.
    Solo se puede aplicar si el juego existe, tiene stock disponible y 'porcentaje' está entre 1 y 100.
    Reemplaza la tupla actualizando el precio con división entera y retorna True.
    Retorna False en caso contrario.
    """
    
    idx = buscar_juego(titulo)

    if idx == -1 and porcentaje < 1 and porcentaje > 100:
        return False

    nombre, plat, precio, stock = inventario[idx]
    
    if stock <= 0:
        return False

    precio_nuevo = (precio * porcentaje) // 100
    inventario[idx] = (nombre, plat, precio_nuevo, stock)
    return True


def obtener_segmento(inicio: int, fin: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de los juegos entre 'inicio' (incluido) y 'fin' (excluido).
    OJO: si un índice se sale de rango, slicing lo ajusta solo (no lanza error).
    """
    juegos_entre = []

    for nombre, _, _, _ in inventario[inicio:fin]:
        juegos_entre.append(nombre)

    return juegos_entre


def crear_oferta(paso: int) -> list[str]:
    """
    [SLICING] Retorna los títulos de un juego de cada 'paso', partiendo por el primero.
    Ejemplo: paso = 2 -> juego 0, 2, 4, ...
    Si 'paso' es menor a 1, retorna una lista vacía.
    """

    juegos_paso = []
    
    if paso < 1:
        return juegos_paso

    for nombre, _, _, _ in inventario[::paso]:
        juegos_paso.append(nombre)

    return juegos_paso

def invertir_catalogo() -> list[str]:
    """
    [SLICING] Retorna los títulos del inventario en orden inverso,
    sin modificar la lista original.
    """
    titulos: list[str] = []

    for titulo, _, _, _ in inventario[::-1]:  # ejemplo de slicing invertido
        titulos.append(titulo)

    return titulos


def resumen() -> tuple[int, int, int]:
    """
    Retorna una tupla con el estado del inventario:
    (cantidad de juegos, valor total en dinero, precio promedio entero).

    - valor total: suma de precio * stock de cada juego.
    - precio promedio: suma de los precios del catálogo dividida por la
      cantidad de juegos (división entera).

    Si el inventario está vacío, retorna (0, 0, 0).
    """
    
    total_juegos = len(inventario)
    if total_juegos <= 0:
        return (0, 0, 0)

    suma_por_juego = 0
    stock_total = 0

    for _, _, precio, stock in inventario:
        stock_total += stock
        suma_por_juego += precio

    valor_total = suma_por_juego * stock_total
    precio_promedio = (suma_por_juego // total_juegos) * 100

    return (total_juegos, valor_total, precio_promedio)

    


if __name__ == "__main__":
    print("\n#=====> BUSCAR Y AGREGAR JUEGOS <=====#")
    print(f"Inventario inicial: {inventario}")

    print(f"\nÍndice de 'Hades': {buscar_juego('hades')}")
    print(f"Índice de 'Minecraft': {buscar_juego('Minecraft')}")

    print(f"\n¿Se agregó 'Minecraft'?: {agregar_juego('Minecraft', 'PC', 20000, 4)}")
    print(f"¿Se agregó 'Hades' de nuevo?: {agregar_juego('Hades', 'PC', 18000, 5)}")
    print(f"Inventario actual: {inventario}")

    print("\n#=====> VENTAS Y DESCUENTOS <=====#")
    print(f"Juego antes de vender: {inventario[buscar_juego('Hollow Knight')]}")
    print(f"¿Se vendieron 2 copias de Hollow Knight?: {vender_copias('Hollow Knight', 2)}")
    print(f"Juego después de vender: {inventario[buscar_juego('Hollow Knight')]}")
    print(f"¿Se vendieron 99 copias de Celeste?: {vender_copias('Celeste', 99)}")

    print(f"\nJuego antes del descuento: {inventario[buscar_juego('Cuphead')]}")
    print(f"¿Se aplicó 25% de descuento a Cuphead?: {aplicar_descuento('Cuphead', 25)}")
    print(f"Juego después del descuento: {inventario[buscar_juego('Cuphead')]}")
    print(f"¿Se aplicó descuento a Celeste (sin stock)?: {aplicar_descuento('Celeste', 10)}")

    print("\n#=====> SEGMENTOS Y OFERTAS <=====#")
    print(f"Segmento [1:4]: {obtener_segmento(1, 4)}")
    print(f"Oferta (uno de cada 2): {crear_oferta(2)}")
    print(f"Catálogo invertido: {invertir_catalogo()}")
    print(f"El inventario original no cambió: {inventario}")

    print("\n#=====> RESUMEN <=====#")
    print(f"Resumen (cantidad, valor total, precio promedio): {resumen()}")

    print("\n[ Inventario final ]")
    for titulo, plataforma, precio, stock in inventario:
        print(f"  - {titulo} ({plataforma}) | ${precio} | Stock: {stock}")
