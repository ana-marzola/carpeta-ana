# Algoritmo para calcular el nuevo salario mínimo
salario_minimo_actual = float(input("Ingresa el salario mínimo actual: "))
incremento = 0.042
nuevo_salario_minimo = salario_minimo_actual * (1 + incremento)
print("El nuevo salario mínimo para el próximo año es:", nuevo_salario_minimo)