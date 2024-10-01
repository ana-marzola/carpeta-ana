def eliminar_duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:  # Solo agrega si no está en la nueva lista
            nueva_lista.append(elemento)
    return nueva_lista

# Ejemplo de uso:
numeros_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 6]
resultado = eliminar_duplicados(numeros_con_duplicados)
print(resultado)  # Debería imprimir [1, 2, 3, 4, 5, 6]