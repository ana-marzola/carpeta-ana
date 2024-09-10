# se solicita cuatro notas del estudiante
nota1 = float(input("ingrese la primera nota(de 1 a 5):"))
nota2 = float(input("ingrese la segunda nota(de 1 a 5):"))
nota3 = float(input("ingrese la tercera nota(de 1 a 5):"))
nota4 = float(input("ingrese la cuarta nota(de 1 a 5):"))
# Calcula el promedio de las notas
promedio = (nota1+nota2+nota3+nota4)/4
# Clasificar el rendimiento del estudiante
if 4<=promedio<=5:
    rendimiento = "Excente"
elif 3<=promedio<4:
    rendimiento = "Bien"
else:
    rendimiento = "Deficiente"
# se solicita  el costo de la matricula
costo_matricula = float(input("ingresa el costo de la matricula:"))
# calcula el costo final de la matricula
if rendimiento == "Excelente":
    costo_final = costo_matricula * 0.8 # Aplicar un descuento de 20%
else:
    costo_final = costo_matricula
# Mostrar los resultados
print("El promedio de estudiante es:",promedio)
print(" su rendimiento es:",rendimiento)
print("El monton final a pagar por la matricula es:,costo_final,"pesos")

