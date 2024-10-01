# Pedimos todos los datos al usuario
precio_base_moto = float(input("Ingrese el precio base de la motocicleta: "))
marca_moto = input("Ingrese la marca de la motocicleta: ")
dia = input("¿Qué día es la compra? ")
es_feriado = input("¿El día de la compra es feriado? Ingrese Sí o No. ")

# Definimos variables
descuento_acumulado = 0
ahorro = 0

# Procesamos descuentos por marca
if(marca_moto.lower() =="honda"):
    print("Se ha aplicado el descuento de Honda del 5%.")
    descuento_acumulado = 0.05
elif(marca_moto.lower() =="yamaha"):
    print("Se ha aplicado el descuento de Yamaha del 8%.")
    descuento_acumulado = 0.08
elif(marca_moto.lower() =="suzuki"):
    print("Se ha aplicado el descuento de Suziki del 10%.")
    descuento_acumulado = 0.1
else:
    print("Se ha aplicado el descuento de otras marcas del 2%.")
    descuento_acumulado = 0.02

# Procesamos descuentos por día o feriado
if(es_feriado.lower() =="sí" or es_feriado.lower() =="si"):
    print("Se ha aplicado el descuento de día de feriado del 25%.")
    descuento_acumulado = descuento_acumulado + 0.25
elif(dia.lower() =="martes"):
    print("Se ha aplicado el descuento del día Martes del 12%.")
    descuento_acumulado = descuento_acumulado + 0.12
elif(dia.lower() =="sábado" or dia.lower() =="sabado"):
    print("Se ha aplicado el descuento del día Sábado 18%.")
    descuento_acumulado = descuento_acumulado + 0.18

# Limitamos el descuento acumulado a 30 %
if(descuento_acumulado > 0.3):
    print("Se ha superado el límite de descuento... su descuento será del 30%.")
    descuento_acumulado = 0.3

# Calculamos el total ahorrado y despues el precio final de la moto
ahorro = precio_base_moto * descuento_acumulado
precio_final_moto = precio_base_moto - ahorro

# Mostramos el usuario los resultados
print("El precio final de la motocicleta es: ", precio_final_moto)
print("El total de descuento es: ", descuento_acumulado*100,"%")
print("El cliente ahorró: ", ahorro)
