import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)

print(lista_valores)

lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['c1','c2','c3','c4','c5']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)

print(dataframe)

#para traer una columna o fila especifica

#
print("para traer una columna o fila especifica:",dataframe[['c2','c4']])
#conocer valores del data frame que son mayores o menores de algo
print(dataframe >20)
#con el metodo loc conocesmos en especifico un dato o conjunto de datos
print(dataframe.loc['i3'])
