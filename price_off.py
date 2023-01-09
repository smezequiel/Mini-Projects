# Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento.
# El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10%
# y si la clave es 02 el descuento en del 20% (solo existen dos claves).

articulo = str(input("Ingrese nombre del articulo: "))
clave = str(
    input("Seleccione una de las dos claves: \n\ta. 01\n\tb. 02 \n\tIngrese: "))
precio_original = int(input("Precio original: "))

if clave == "01":
    final = int(precio_original * 0.9)
else:
    final = int(precio_original * 0.8)

print(f"El monto a final a pagar de un/a {articulo} es ${final}")
