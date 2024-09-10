# tarifa por minuto segun el destino
tarifa = {"Estados unidos":900,"Canada":800,"Europa":950,"Resto del mundo":120}
#se solicita al usuario el destino de la llamada
destino = input("ingrese el destino de la llamada(Estados Unidos,Canada,Europa,resto del mundo):")
# solicita la  usuario la duracion de la llamada en minutos
duracion =int(input("ingresa la duracion de la llamada en minutos"))
#calcula el costo total de la llamada
if destino in tarifa:
    costo_total = tarifa[destino] * duracion
# Aplicar descuento si la duracion es mayor a 15 minutos
if duracion>15:
    costo_total = costo_total*0.8
# Aplicar un descuento del 20%
# mostrar el costo total de la llamada
print("El costo_total de la llamada es:",costo_total,"peso")
else:
print("Destino no valido.")
