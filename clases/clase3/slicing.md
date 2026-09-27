# Slicing
El slicing permite extraer secuencias de una lista en python siguiendo esta estructura:

```
lista[inicio:fin:paso]
```

Donde:
- inicio: índice donde empieza la extracción (se incluye y por defecto es 0).
- fin: índice donde termina la extracción (se excluye y por defecto es -1, o sea el fin de la lista).
- paso: salto entre elementos (por defecto es 1).

## Ejemplos
| Sintaxis | Descripción | "Ejemplo (x = \[0, 1, 2, 3, 4, 5\])" | Resultado |
| :--- | :--- | ---: | ---: |
| x\[a:b\] | Desde el índice a hasta b-1 | x\[1:4\] | "\[1, 2,  3\]" |
| x\[a:\] | Desde a hasta el final | x\[2:\] | "\[2, 3, 4, 5\]" |
| x\[:b\] | Desde el inicio hasta b-1 | x\[:3\] | "\[0, 1, 2\]" |
| x\[:\] | Copia superficial (shallow copy) de toda la lista | x\[:\] | "\[0, 1, 2, 3, 4, 5\]" |
| x\[::n\] | Todo el objeto tomando cada n elementos | x\[::2\] | "\[0, 2, 4\]" |
| x\[-n:\] | Los últimos n elementos | x\[-2:\] | "\[4, 5\]" |
| x\[::-1\] | Invertir la secuencia completa | x\[::-1\] | "\[5, 4, 3, 2, 1, 0\]" |
