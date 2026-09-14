# La escuela de infomática guarda los estudiantes y sus notas en tablas independientes pero relacionadas.
# Estas tablas son accedidas por medio de python usando listas.
#
# Se deben crear listas para los promedios y otra que diga si está aprobado (True) o reprobado (False).
# Se tiene que seguir la lógica de las listas sincronizadas.


# Versión paso a paso
def promedio(numeros):
    """Recibe una lista de números y retorna el promedio"""
    pass


def procesar_promedios(col_notas):
    """Recibe una matriz de notas y retorna una lista de promedios"""
    pass


def procesar_situacion(promedios, minimo = 4):
    """Recibe una lista de promedios y retorna una lista de booleanos
    indicando los índices aprobados/reprobados"""
    pass

def resumen(alumnos, notas, promedios, situaciones):
    """Muestra por consola toda la información relacionada al grupo de estudiantes.
    su índice, el nombre, sus notas, su promedio y si está aprobado o reprobado"""
    pass


if __name__ == "__main__":
    alumnos: list[str] = ["Felipe", "Agustín", "Juan", "Pedro"]
    notas: list[list[float]] = [
            [6.5, 7.0, 5.8], # Felipe
            [2.5, 3.0, 3.5], # Agustín
            [4.0, 4.0, 4.0], # Juan
            [3.0, 4.5, 3.5]  # Pedro
            ]

    promedios_res = procesar_promedios(notas)
    situaciones_res = procesar_situacion(promedios_res)

    resumen(alumnos, notas, promedios_res, situaciones_res)
