inversion = float(input("ingrese el valor a invertir: "))
tasa_interes = float(input("ingrese la tasa de interes: "))
años_inversion = float(input("ingrese los años de inversion: "))

interes_simple = inversion * tasa_interes/100 * años_inversion
monto_total = interes_simple + inversion

print(f"El interes simple es:{interes_simple}")
print(f"El monto total de la inversion es: {monto_total} ")

nombre = input("ingresa su nombre")
edad = input("ingresa eda")

if edad >= 18:
    print(f"la persona {nombre} tiene {edad} años y puede votar")
else edad <18
# print("es mayor")