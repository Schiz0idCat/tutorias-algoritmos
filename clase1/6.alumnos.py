#####################################
####### ALUMNOS Y PORCENTAJES #######
#####################################

# Tienes una lista con las notas finales de un grupo de estudiantes.
# La nota mínima para aprobar es un 4.0.
# Debes contar cuántos alumnos aprobaron y cuántos reprobaron.
# Al final, debes mostrar la cantidad de aprobados/reprobados
# y el porcentaje que representa cada grupo respecto al total, con 2 decimales.

notas = [5.5, 3.2, 6.0, 2.8, 4.0, 4.5]

# Variables
cantrepro = 0
cantapro = 0
total = len(notas)

# Verificar
for nota in notas:
    if nota >= 4.0:
        cantapro += 1
    else:
        cantrepro += 1

# Mat
porcapro = (cantapro/total) * 100
porrepro = (cantrepro/total) * 100

print(f"De {total} alumnos, {cantapro} aprobaron y {cantrepro} reprobaron")
print(f"El porcentaje de aprobados es {porcapro} y de reprobados es {porrepro}")
