# Un palíndromo es una palabra que se lee igual de izquierda a derecha y de derecha a izquierda.
# hacer función 'es_palindromo(s: str): -> bool' que retorna si un string es palíndromo o no.
#
# RESTRICCIÓN:
#   - Se tiene que usar slicing

def es_palindromo(s: str) -> bool:
    s_clean = s.lower()
    return s_clean == s_clean[::-1]


def es_palindromo_2(s: str) -> bool:
    s_clean = s.lower()
    izquierda = 0
    derecha = len(s_clean) - 1

    while izquierda < derecha:
        if s_clean[izquierda] != s_clean[derecha]:
            return False

        izquierda += 1
        derecha -= 1

    return True


if __name__ == "__main__":
    s = "Anilina"

    print(f"{s} es palíndromo?: {es_palindromo(s)}")
