# La escuela de infomática guarda los estudiantes y sus notas en tablas independientes pero relacionadas.
# Estas tablas son accedidas por medio de python usando listas.
#
# Se deben crear listas para los promedios y otra que diga si está aprobado (True) o reprobado (False).
# Se tiene que seguir la lógica de las listas sincronizadas.


alumnos: list[str] = ["Felipe", "Agustín", "Juan", "Pedro"]
notas: list[list[float]] = [
        [6.5, 7.0, 5.8], # Felipe
        [2.5, 3.0, 3.5], # Agustín
        [4.0, 4.0, 4.0], # Juan
        [3.0, 4.5, 3.5]  # Pedro
        ]


# Versión difícl
def procesar_promedios(notas: list[list[float]]) -> list[float]:
    return [sum(notas_estudiante) / len(notas_estudiante) for notas_estudiante in notas]


def procesar_situacion(promedios: list[float], minimo: float = 4.0) -> list[bool]:
    return [promedio >= minimo for promedio in promedios]


# Versión rápida
def procesar_notas(col_notas: list[list[float]], promedios: list[float], situacion: list[bool], minimo: float = 4.0) -> None:
    for notas in col_notas:
        promedio = sum(notas) / len(notas)

        promedios.append(promedio)
        situacion.append(promedio >= minimo)


# Versión paso a paso
def promedio(numeros):
    return sum(numeros) / len(numeros)


def procesar_promedios_2(col_notas):
    promedios = []

    for notas in col_notas:
        prom = promedio(notas)

        promedios.append(prom)

    return promedios


def procesar_situacion_2(promedios, minimo = 4):
    situaciones = []

    for promedio in promedios:
        situacion = promedio >= minimo

        situaciones.append(situacion)

    return situaciones

def resumen(alumnos, notas, promedios, situaciones):
    for i in range(len(alumnos)):
        estado = "aprobado" if situaciones[i] else "reprobado"

        print(f"alumno {i + 1}")
        print(f"alumno: {alumnos[i]}")
        print(f"notas: {notas[i]}")
        print(f"promedio: {promedios[i]}")
        print(f"situación: {estado}")


if __name__ == "__main__":
    promedios_res = procesar_promedios_2(notas)
    situaciones_res = procesar_situacion_2(promedios_res)

    resumen(alumnos, notas, promedios_res, situaciones_res)
