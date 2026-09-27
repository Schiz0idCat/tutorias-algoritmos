###################################
######## DESCUENTO DE CINE ########
###################################

# Un cine sus entradas a $4.000 pesos.
# Pero tiene descuento según edad y si eres miembro del 'Club de Cinéfilos'
# Si el cliente es menor de 12 años o mayor de 60, recibe un descuento del 20%.
# Y si es miembro del 'Club de Cinéfilos' recibe un descuento del 15%.
# Los descuentos son acumulables,
# pero solo los mayores de 18 años pueden ser miembros del club

entrada = 4000
descuento = 0

edad = int(input())

if edad <= 12 or edad >= 60:
    descuento = 0.2

if edad >= 18:
    club = input("Es miembro del club? ")

    if club.upper() == "SI":
        descuento += 0.15

descuento_total = entrada * (descuento)
precio_final = entrada - descuento_total
print(precio_final)
