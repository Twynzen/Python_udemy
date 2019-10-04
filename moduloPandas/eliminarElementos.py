import pandas as pd
import numpy as np

np.arange(3)

serie = pd.Series(np.arange(4), index=['a','b','c','d'])

#print(serie)



#así se elimina un elmento de una serie
#print(serie.drop('c'))

#reshape dice las columnas y filas que tendrá
lista_valores0 = np.arange(9).reshape(3,3)
print(lista_valores0)

lista_filas= ['a','b','c']
lista_columnas = ['c1','c2','c3']

dataframe = pd.DataFrame(lista_valores0, index=lista_filas, columns=lista_columnas)

print(dataframe)
print("Eliminamos la columna c3")
#debo agregar el comnado axis=1 para indicar el eje en elq ue considera en que esta las
print(dataframe.drop('c3', axis=1))
