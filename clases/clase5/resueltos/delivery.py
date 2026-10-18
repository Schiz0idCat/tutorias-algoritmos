# Datos del sistema de delivery y restaurante:
#
# - menu: Lista de tuplas con la forma (nombre_plato, precio, categoria).
# - pedidos: Lista de tuplas con la forma (id, lista_items, estado, total).
#   Estados válidos: "pendiente", "en preparacion", "entregado", "cancelado".

menu: list[tuple[str, int, str]] = [
    ("hamburguesa", 5000, "comida"),
    ("papas fritas", 2500, "comida"),
    ("bebida", 1500, "bebestible"),
    ("pizza", 8000, "comida")
]

estados_validos = ["pendiente", "en preparacion", "entregado", "cancelado"]

pedidos: list[tuple[int, list[str], str, int]] = [
    (1, ["hamburguesa", "papas fritas"], "entregado", 7500),
    (2, ["pizza", "bebida"], "en preparacion", 9500)
]

contador: list[int] = [3]


def agregar_plato(nombre: str, precio: int, categoria: str) -> bool:
    """
    Agrega un nuevo plato al menú como una tupla (nombre, precio, categoria).
    Si el plato ya existe en el menú (insensible a mayúsculas/minúsculas),
    no hace nada y retorna False.
    Retorna True si la inclusión fue exitosa.
    """

    nombre_limpio = nombre.strip().lower()

    for item_nombre, _, _ in menu:
        if item_nombre.lower() == nombre_limpio:
            return False

    menu.append((nombre_limpio, precio, categoria.strip().lower()))

    return True


def buscar_precio_plato(nombre: str) -> int:
    """
    Busca un plato en el menú por su nombre (insensible a mayúsculas/minúsculas).
    Retorna su precio base. Retorna -1 en caso de no encontrarlo.
    """
    nombre_limpio = nombre.strip().lower()

    for item_nombre, precio, _ in menu:
        if item_nombre.lower() == nombre_limpio:
            return precio

    return -1


def crear_pedido(items: list[str]) -> int:
    """
    Crea un nuevo pedido con estado 'pendiente'.
    Filtra los items para conservar solo los que existen en el menú y calcula el total sumando sus precios.
    Si ningún item es válido, no genera el pedido y retorna -1.
    Si hay al menos un item válido, añade la tupla (contador_id, items_validos, "pendiente", total)
    a la lista 'pedidos', incrementa 'contador_id' y retorna el ID del pedido creado.
    """
    items_validos: list[str] = []
    total = 0

    for item in items:
        precio = buscar_precio_plato(item)

        if precio != -1:
            items_validos.append(item.strip().lower())
            total += precio

    if not items_validos:
        return -1

    id = contador[0]
    contador[0] += 1

    nuevo_pedido = (id, items_validos, "pendiente", total)
    pedidos.append(nuevo_pedido)

    return id


def cambiar_estado_pedido(id_pedido: int, nuevo_estado: str) -> bool:
    """
    Busca el pedido por su ID dentro de la lista 'pedidos'.
    Si existe y 'nuevo_estado' es válido ("pendiente", "en preparacion", "entregado", "cancelado"),
    reemplaza la tupla del pedido con el nuevo estado y retorna True.
    En caso contrario, retorna False.
    """
    estado_limpio = nuevo_estado.strip().lower()

    if estado_limpio not in estados_validos:
        return False

    for i in range(len(pedidos)):
        ped_id, ped_items, _, ped_total = pedidos[i]

        if ped_id != id_pedido: continue

        pedidos[i] = (ped_id, ped_items, estado_limpio, ped_total)
        return True

    return False


def aplicar_cupon_descuento(id_pedido: int, porcentaje: int) -> bool:
    """
    Aplica un porcentaje de descuento (ej: 10 para 10%) sobre el total del pedido.
    Solo se puede aplicar si el pedido existe y su estado es 'pendiente'.
    Reemplaza la tupla actualizando el total con la división entera del descuento y retorna True.
    Retorna False si el pedido no existe, si no está 'pendiente' o si el porcentaje no está entre 1 y 100.
    """
    if not (1 <= porcentaje <= 100):
        return False

    # No se puede recorrer la lista 'pedidos' de forma directa,
    # Porque dentro del for se va a modificar.
    for i in range(len(pedidos)):
        id, items, estado, total = pedidos[i]

        if id != id_pedido:
            continue

        if estado != "pendiente":
            return False

        descuento = (total * porcentaje) // 100
        nuevo_total = total - descuento
        pedidos[i] = (id, items, estado, nuevo_total)
        return True

    return False


def resumen_ventas() -> tuple[int, int, int]:
    """
    Calcula y retorna una tupla con las métricas de los pedidos con estado 'entregado':
    (total_recaudado, cantidad_pedidos, total_platos_vendidos)
    """

    total_recaudado = 0
    cantidad_pedidos = 0
    total_platos_vendidos = 0

    for _, items, estado, total in pedidos:
        if estado == "entregado":
            total_recaudado += total
            cantidad_pedidos += 1
            total_platos_vendidos += len(items)

    return total_recaudado, cantidad_pedidos, total_platos_vendidos


if __name__ == "__main__":
    print("#=====> AGREGANDO UN PLATO AL MENU <=====#")
    print("menú inicial")
    print(menu)
    agregar_plato("empanada", 2000, "comida")
    print("\nmenú actual")
    print(menu)

    print("\n#=====> AGREGAR UN PEDIDO <=====#")
    print("pedidos inicial")
    print(pedidos)
    id_nuevo = crear_pedido(["hamburguesa", "bebida", "item_inexistente"])
    print("\npedidos actual")
    print(pedidos)


    print("\n#=====> APLICAR CUPÓN <=====#")
    print("pedido inicial")
    print(pedidos[id_nuevo-1])
    aplicar_cupon_descuento(id_nuevo, 10)

    print("\npedido actual")
    print(pedidos[id_nuevo-1])

    print("\n#=====> CAMBIAR ESTADO <=====#")
    print("pedido inicial")
    print(pedidos[id_nuevo-1])

    cambiar_estado_pedido(id_nuevo, "en preparacion")
    print("\npedido actual")
    print(pedidos[id_nuevo-1])

    cambiar_estado_pedido(id_nuevo, "entregado")
    print("\npedido actual")
    print(pedidos[id_nuevo-1])

    print("\n#=====> RESUMEN DE VENTAS <=====#")
    
    print("\n[ Menú actual ]")
    for plato, precio, cat in menu:
        print(f"  - {plato.title()} (${precio}) - Categoría: {cat}")

    print("\n[ Estado de todos los pedidos ]")
    for id_p, items, estado, total in pedidos:
        items_str = ", ".join(items)
        print(f"  - Pedido #{id_p}: [{estado.upper()}] | Items: {items_str} | Total: ${total}")

    recaudado, cant_pedidos, cant_platos = resumen_ventas()
    print(f"\nTotal recaudado: ${recaudado}")
    print(f"Pedidos entregados: {cant_pedidos}")
    print(f"Platos vendidos: {cant_platos}")
