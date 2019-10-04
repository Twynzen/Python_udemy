import pandas as pd
import numpy as np

lista_valores = np.arange(9).reshape(3,3)

lista_indices = list('abc')

dataframe = pd.DataFrame(lista_valores, index=lista_indices)
print(dataframe)
#así cambiamos los indices en este caso los volvemos mayusculas con str.upper
nuevos_indices = dataframe.index.map(str.upper)
dataframe.index = nuevos_indices
print(dataframe)

#así renonmbramos un dataframe en este casoa  minusculas
dataframe = dataframe.rename(index=str.lower)

#así se reemplazan lista_indices
#se crea un diccionario nuevo
nuevos_indices = {'a':'f', 'b':'g', 'c':'h'}
print(dataframe.rename(index=nuevos_indices))
