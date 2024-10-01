def invertir_lista(lista):
    nueva_lista = []
    for i in range(len(lista)-1, -1, -1):  # Recorre la lista desde el último al primero
        nueva_lista.append(lista[i])
    return nueva_lista

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print(resultado)  # Debería imprimir [5, 4, 3, 2, 1]