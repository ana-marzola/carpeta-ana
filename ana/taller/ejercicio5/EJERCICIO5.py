# a) Verificar si 'x' está entre 'y' y 'z', y si 'w' es par:

x, y, z, w = 15, 10, 20, 8

# Verificar si 'x' está entre 'y' y 'z'
x_entre_y_z = y < x < z

# Verificar si 'w' es par
w_es_par = w % 2 == 0

print("¿x está entre y y z?", x_entre_y_z)
print("¿w es par?", w_es_par)