import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])
print(serie1)


serie2 = pd.Series([3,4,5,6], index=['a','b','c','d'])

print(serie1+serie2)

lista_valores = np.arange(4).reshape(2,2)

lista_indices = list('ab')
lista_columnas = list('12')
print("Esto construlle una lista con los elementos que hay dentro el metodo list",lista_indices)

dataframe= pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)

print(dataframe)

lista_indices2 = list('abc')
lista_columnas2 = list('123')
lista_valores2 = np.arange(9).reshape(3,3)

dataframe2 = pd.DataFrame(lista_valores2, index = lista_indices2, columns=lista_columnas2)

print("ahora una matriz de 3x3",dataframe2)
fusiondataframe = dataframe+dataframe2
print("Ahora una suma de  las anteriores matrices",fusiondataframe)

#se puede rellenar un dataframe conocer

print("Ahora una suma de  las anteriores matrices rellenando lo faltante",dataframe.add(dataframe2,fill_value=0))
