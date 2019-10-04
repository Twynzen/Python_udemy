import numpy as np

array = np.arange (0, 11)

print(array)

print(array[5:8])

lista_copiada = array.copy()

print(lista_copiada)

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))

print("Así hacemos indexación de array  de 3 filas y 3 columnas",array2[2])
