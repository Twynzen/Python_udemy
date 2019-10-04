#Operaciones que dan un valor, como la media
import pandas as pd
import numpy as np

#primero creamos un dataframe
lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan, np.nan, np.nan]]

print(lista_valores)

lista_columnas = list('abc')

dataframe = pd.DataFrame(lista_valores, columns = lista_columnas)

#esta es la agregación: agrupar para obtener un valor
#en este caso calculamos la suma y el minimo valor
print(dataframe.agg(['sum','min']))
#así elejimos el eje para que lo haga por filas en vez de por columnas
print(dataframe.agg('sum',axis=1))
