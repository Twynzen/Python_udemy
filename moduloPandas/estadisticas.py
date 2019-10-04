import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])
dataframe = pd.DataFrame(array, index= ['a','b'], columns = list('123'))

print(dataframe)

#suma de columnas
dataframe.sum()
#para sumar por filas
dataframe.sum(axis=1)

#El minimo valor es
dataframe.min()
#el valor maximo
dataframe.max()

#conocer el valor minimo o maximo con el listaIndices
dataframe.idxmin()

#Da un conjunto de datos estadisticos de la matris
print(dataframe.describe())
