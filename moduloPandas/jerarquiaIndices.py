import pandas as pd
import numpy as np

listaValores = np.random.rand(6)
#lA SERIE TIENE 2 INDICES
listaIndices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]

serie = pd.Series(listaValores, index= listaIndices)

print(serie)
#este metodo pone los indices como columnas y filas del dataframe
dataframe = serie.unstack()

#reshape para el número de dimenciones de matriz
lista_valores = np.arange(16).reshape(4,4)

lista_indices = list('1234')
lista_columnas = list('abcd')

dataframe2 = pd.DataFrame(lista_valores, index= lista_indices, columns= lista_columnas)
print(dataframe2)

#este hace las listas de doble indices
serie2 = dataframe2.stack()

print(serie2)
