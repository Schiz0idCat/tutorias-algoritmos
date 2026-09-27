notas = [4.0, 3.7, 5.0, 4.3]
promedio = 4.2                  # sum(notas) / len(notas)
situacion = ""

hay_rojo = False

# for nota in notas:
#     if nota < 4:
#         hay_rojo = True

hay_rojo = any(nota < 4 for nota in notas)

if promedio >= 5.0 or (promedio >= 4.5 and not hay_rojo):
    situacion = "aprueba"
elif promedio >= 4.0 or (promedio >= 3.5 and not hay_rojo):
    situacion = "examen"
else:
    situacion = "reprueba"

print(situacion)
