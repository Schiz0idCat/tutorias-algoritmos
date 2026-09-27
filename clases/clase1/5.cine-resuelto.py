###################################
######## DESCUENTO DE CINE ########
###################################

# Un cine sus entradas a $4.000 pesos.
# Pero tiene descuento según edad y si eres miembro del 'Club de Cinéfilos'
# Si el cliente es menor de 12 años o mayor de 60, recibe un descuento del 20%.
# Y si es miembro del 'Club de Cinéfilos' recibe un descuento del 15%.
# Los descuentos son acumulables,
# pero solo los mayores de 18 años pueden ser miembros del club

# Input
edad = int(input("¿Cuántos años tienes?: "))
miembro = input("¿Eres miembro del 'Club de Cinéfilos? (s/n): " )

if miembro == "s" and edad >= 18:
    miembro = True
else:
    miembro = False

# Lógica
PRECIO_BASE = 4_000
descuento = 0

if edad <= 12 or edad >= 60:
    descuento += 0.20

if miembro:
    descuento += 0.15

precio = PRECIO_BASE * (1 - descuento)

print(f"Precio entrada: {PRECIO_BASE}")
print(f"Descuento aplicado: {int(descuento * 100)}%")
print(f"Total a pagar: ${int(precio)}")
