import pandas as pd
import numpy as np

#así se crea un valor nulo
listaValores = ['1', '2', np.nan, '4']

serie = pd.Series(listaValores, index= list('abcd'))

print("Una serie con un valor nulo",serie)

#un metodo para saber si un valor es nulo o no
print(serie.isnull())

#para saltarse un calor nulo
print(serie.dropna())

#para borrar permanemtemente
serie = serie.dropna()

lista_valores = [ [1,2,3], [4,np.nan,5],[6,7,np.nan]]

print("Introducidos unos valores nulos",lista_valores)

lista_indices = list('123')

lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores, index= lista_indices, columns=lista_columnas)
#se puede agregar y modificar borrar un nulo en un data DataFrame
print(dataframe.isnull())
print(dataframe.dropna())
#rellenar un nulo
print(dataframe.fillna(0))
