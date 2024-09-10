 # Leer las cinco notas del estudiante
notas = []
pesos = [0.2, 0.15, 0.22, 0.10, 0.33]

for i in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i + 1} (de 1.0 a 5.0): "))
            if 1.0 <= nota <= 5.0:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 1.0 y 5.0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Calcular la nota definitiva
nota_final = sum(nota * peso for nota, peso in zip(notas, pesos))

# Imprimir la nota final redondeada a dos decimales
print("La nota final del curso es:", round(nota_final, 2))

# Evaluación cualitativa (opcional)
if nota_final >= 4.5:
    print("Evaluación: Excelente")
elif nota_final >= 3.5:
    print("Evaluación: Bueno")
elif nota_final >= 2.5:
    print("Evaluación: Regular")
else:
    print("Evaluación: Insuficiente")
