def suma_numeros_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:  # Si el número es divisible por 2, es par
            suma += numero
    return suma

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_numeros_pares(numeros)
print(resultado)  # Debería imprimir 30