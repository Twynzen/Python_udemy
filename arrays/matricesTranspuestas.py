#Conciste ne cambiar ordenadamente las filas por las columnas

import numpy as np

# creaciónd e una matriz de 0 a 14 con 5 columnas y 3 filas
array = np.arange(15).reshape((3,5))

#Con el metodo T se transpone la matriz
array_tras = array.T

#matriz normal
print("Matrz normal",array)
#matriz transpuesta
print("Matriz transpuesta",array_tras)
