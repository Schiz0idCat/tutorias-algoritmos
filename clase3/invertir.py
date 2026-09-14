# Dada una cadena de texto `s` y un número entero `k`.
# Invierte los primeros `k` caracteres de `s` y retorna la cadena resultante.
# Se asume que: len(s) > k

# Notación slicing:
#   s[:k] -> todos los caracteres hasta la posición k
#   s[k:] -> todos los caracteres desde la posición k
#   s[::-1] -> String invertido

s: str = "python"
k: int = 3

def invertir(s: str, k: int):
    pass

if __name__ == "__main__":
    print(f"str: {s}")
    print(f"invertido: {invertir(s, k)}")
