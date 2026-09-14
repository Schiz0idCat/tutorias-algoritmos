# Dada una cadena de texto `s` y un número entero `k`.
# Invierte los primeros `k` caracteres de `s` y retorna la cadena resultante.
# Se asume que: len(s) > k

# Notación slicing:
#   s[:k] -> todos los caracteres hasta la posición k
#   s[k:] -> todos los caracteres desde la posición k
#   s[::-1] -> String invertido

def invertir_primeros_k_slicing(s: str, k: int) -> str:
    invertido = s[:k][::-1]
    resto = s[k:]

    return invertido + resto


def invertir_primeros_k_sin_slicing(s: str, k: int) -> str:
    invertido = ""
    resto = ""

    # s[:k][::-1]
    for i in range(k - 1, -1, -1): # range(inicio, final, pasos)
        invertido += s[i]

    # s[k:]
    for i in range(k, len(s)):
        resto += s[i]

    # s[:k][::-1] + s[k:]
    return invertido + resto

if __name__ == "__main__":
    s, k = "python", 3
    print("--- OPCIÓN CON SLICING ---")
    print(f"Original: '{s}', k={k} -> Resultado: '{invertir_primeros_k_slicing(s, k)}'")

    print("\n--- OPCIÓN SIN SLICING ---")
    print(f"Original: '{s}', k={k} -> Resultado: '{invertir_primeros_k_sin_slicing(s, k)}'")
