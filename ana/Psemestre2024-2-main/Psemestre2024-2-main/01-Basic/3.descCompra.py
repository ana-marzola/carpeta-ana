precio_original = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
impuesto =1.19

descuento_cantidad = precio_original * (descuento / 100)
precio_final = precio_original - descuento_cantidad
precio_impuesto = precio_final* impuesto

print("El descuento es de:" , descuento_cantidad)
print("El precio final es:" , precio_final)
print("El precio con impuesto es:", precio_impuesto)