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
    nombre_s = nombre.lower()

    for i_nombre, _, _ in menu:
        if i_nombre.lower() == nombre_s:
            return False
    
    menu.append((nombre_s, precio, categoria.lower()))
        
        


def buscar_precio_plato(nombre: str) -> int:
    """
    Busca un plato en el menú por su nombre (insensible a mayúsculas/minúsculas).
    Retorna su precio base. Retorna -1 en caso de no encontrarlo.
    """

    for plato, _, precio  in menu:
        if plato == nombre.lower():
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

    pedidos_validados = []
    precio_total = 0

    for pedido in items:
        for comida, _, precio in menu:
            if pedido.lower() == comida:
                pedidos_validados.append(comida)
                precio_total += precio
            
    if len(pedidos_validados) == 0:
        return -1 

    pedidos.append((contador[0], pedidos_validados, precio_total))

    contador[0] += 1

    return contador - 1
        
        


def cambiar_estado_pedido(id_pedido: int, nuevo_estado: str) -> bool:
    """
    Busca el pedido por su ID dentro de la lista 'pedidos'.
    Si existe y 'nuevo_estado' es válido ("pendiente", "en preparacion", "entregado", "cancelado"),
    reemplaza la tupla del pedido con el nuevo estado y retorna True.
    En caso contrario, retorna False.
    """

    for id_pedido, _, estado_pedido, _ in pedidos:
        estado_pedido = nuevo_estado


def aplicar_cupon_descuento(id_pedido: int, porcentaje: int) -> bool:
    """
    Aplica un porcentaje de descuento (ej: 10 para 10%) sobre el total del pedido.
    Solo se puede aplicar si el pedido existe y su estado es 'pendiente'.
    Reemplaza la tupla actualizando el total con la división entera del descuento y retorna True.
    Retorna False si el pedido no existe, si no está 'pendiente' o si el porcentaje no está entre 1 y 100.
    """

    pass


def resumen_ventas() -> tuple[int, int, int]:
    """
    Calcula y retorna una tupla con las métricas de los pedidos con estado 'entregado':
    (total_recaudado, cantidad_pedidos, total_platos_vendidos)
    """

    pass


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