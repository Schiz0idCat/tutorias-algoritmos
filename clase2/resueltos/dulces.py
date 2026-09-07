# Hay `n` niños con dulces. Se te entrega un arreglo de enteros `dulces`, donde
# cada `dulces[i]` representa la cantidad de dulces que tiene el `i-ésimo` niño,
# y un entero `dulces_extra`, que indica la cantidad de dulces adicionales que tienes.
#
# Retorna un arreglo de booleanos `resultado` de longitud `n`, donde `resultado[i]`
# es `True` si, tras entregarle al `i-ésimo` niño todos los `dulces_extra`, este pasa
# a tener la mayor cantidad de dulces entre todos los niños, o `False` en caso contrario.
#
# Nota: Múltiples niños pueden tener la cantidad máxima de dulces simultáneamente.


def ninos_con_dulces_compresion(dulces: list[int], dulces_extra: int) -> list[bool]:
    max_dulces = max(dulces)
    
    return [(cantidad + dulces_extra) >= max_dulces for cantidad in dulces]


def ninos_con_dulces(dulces: list[int], dulces_extra: int) -> list[bool]:
    max_dulces = max(dulces)
    resultado = []

    for cantidad in dulces:
        resultado.append(cantidad + dulces_extra >= max_dulces)

    return resultado


if __name__ == "__main__":
    dulces_iniciales = [2, 3, 5, 1, 3]
    extra = 3
    
    print("--- Listas por Compresión ---")
    resultado = ninos_con_dulces_compresion(dulces_iniciales, extra)
    print(f"Dulces iniciales: {dulces_iniciales}")
    print(f"Dulces extra: {extra}")
    print(f"Resultado: {resultado}")

    print("--- SIN Listas por Compresión ---")
    resultado = ninos_con_dulces(dulces_iniciales, extra)
    print(f"Dulces iniciales: {dulces_iniciales}")
    print(f"Dulces extra: {extra}")
    print(f"Resultado: {resultado}")
