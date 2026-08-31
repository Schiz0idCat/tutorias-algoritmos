#####################################
####### ALUMNOS Y PORCENTAJES #######
#####################################

# Tienes una lista con las notas finales de un grupo de estudiantes.
# La nota mínima para aprobar es un 4.0.
# Debes contar cuántos alumnos aprobaron y cuántos reprobaron.
# Al final, debes mostrar la cantidad de aprobados/reprobados
# y el porcentaje que representa cada grupo respecto al total, con 2 decimales.

notas = [5.5, 3.2, 6.0, 2.8, 4.0, 4.5]

aprobados = 0
reprobados = 0

# Contador
for nota in notas:
    if nota >= 4.0:
        aprobados += 1
    else:
        reprobados += 1

# Cálculo
total_alumnos = len(notas)
per_aprobados = (aprobados / total_alumnos) * 100
per_reprobados = (reprobados / total_alumnos) * 100

# Print
print(f"Total de alumnos: {total_alumnos}")
print(f"Aprobados: {aprobados} ({round(per_aprobados, 2)}%)")
print(f"Reprobados: {reprobados} ({per_reprobados:.2f}%)")
