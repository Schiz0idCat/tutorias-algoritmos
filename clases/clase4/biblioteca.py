# Una biblioteca te pide ayuda para que ayudes a crear registros de nuevos libros que quieren incluir.
# Además, quieren que les ayudes a manejar el sistema de préstamos, pues hasta ahora, lo llevan haciendo a mano

# Datos del sistema de biblioteca:
# - titulos: Contiene los libros de la biblioteca.
# - autores: Contiene los autores de los libros de la biblioteca.
# - stock: Cantidad de unidades que tienen del n-ésimo libro.
# - préstamos: En cuánto tiempo (en días) una unidad del enésimo libro deber ser devuelto.

# Todas son listas sincronizadas. esto significa que:
# El libro 'titulos[i]' fue escrito por 'autores[i]'.
# La biblioteca tiene en stock 'stock[i]' unidades del libro 'titulos[i]'.
# La biblioteca ha prestado 'len(prestamos[i])' unidades del libro 'titulos[i]'.
# La unidad 'j' del libro 'titulos[i]' debe ser devuelto en 'prestamos[i][j]' días.

titulos: list[str] = ["Cien Años de Soledad", "El Principito", "Rayuela"]
autores: list[str] = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "Julio Cortázar"]
stock: list[int] = [3, 0, 2]
prestamos: list[list[int]] = [
    [7, 14, 5],  # Préstamos de Cien Años de Soledad
    [3, 10],     # Préstamos de El Principito
    [12]         # Préstamos de Rayuela
]


def agregar_libro(titulo: str, autor: str, cantidad: int) -> None:
    """
    Recibe libro (nombre y autor) y la cantidad.
    Agrega el título, autor y cantidad a las listas correspondientes.
    Además, inicializa los préstamos de dicho libro.
    """
    titulos.append(titulo)
    autores.append(autor)
    stock.append(cantidad)
    prestamos.append([])
    


def buscar_libro(titulo: str) -> int:
    """
    Retorna el índice de un libro haciendo una búsqueda insensible a mayúsculas/minúsculas.
    Retorna -1 en caso de no encontrarlo.
    """
    for indice in range(len(titulos)):
        if titulo == titulos[indice]:
            return indice

    return -1


def prestar_libro(titulo: str, dias: int) -> bool:
    """
    Presta un libro durante una cierta cantidad de días.
    Resta en 1 el stock del libro y añade la cantidad de días al registro de préstamos.
    Retorna True si el préstamo fue exitoso, o False si no se encontró o no hay stock.
    """

    i = buscar_libro(titulo)
    if i == -1 or stock[i] <= 0:
        return False

    stock[i] -= 1
    prestamos[i].append(dias)

    return True


def pasar_dia() -> list[tuple[int, int, int]]:
    """
    Resta 1 día a la cantidad de días restantes de todos los préstamos activos.
    Retorna una lista de tuplas con la forma (índice libro, índice unidad, días pendientes)
    para las unidades cuyos días restantes sean menor o igual a 0.
    """
    vencidos = []
    for i in range(len(prestamos)):
        for j in range(len(prestamos[i])):
            prestamos[i][j] -= 1
            if prestamos[i][j] <= 0:
                vencidos.append((i, j, prestamos[i][j]))
        
    return vencidos


def devolver_libro(titulo: str, indice_unidad: int) -> bool:
    """
    Acepta la devolución de una unidad prestada.
    Remueve el préstamo en 'indice_unidad' y aumenta en 1 el stock.
    Retorna True si la operación fue exitosa, o False si el libro o la unidad no existen.
    """

    libro = buscar_libro(titulo)
    if libro == -1:
        return False
    
    if len(prestamos[libro]) >= indice_unidad >= 0:
        return False
    
    prestamos[libro].pop(indice_unidad)
    stock[libro] += 1
    return True


def generar_reporte() -> list[tuple[str, str, int, int]]:
    """
    Retorna una lista de tuplas con la estructura:
    (titulo, autor, stock_disponible, unidades_prestadas)
    """
    reporte = []
    for i in range(len(titulos)):
        info = (titulos[i], autores[i], stock[i], len(prestamos[i]))
        reporte.append(info)
    
    return reporte

    


if __name__ == "__main__":
    agregar_libro("Fahrenheit 451", "Ray Bradbury", 4)

    print(generar_reporte())
    
    prestar_exito = prestar_libro("rayuela", 7)

    print(generar_reporte())

    vencidos = pasar_dia()

    print(generar_reporte())

    devolucion_exito = devolver_libro("El Principito", 0)

    print(generar_reporte())
