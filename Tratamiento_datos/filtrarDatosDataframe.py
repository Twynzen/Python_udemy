import pandas as pd
import numpy as np

lista_valores = np.random.rand(10,3)
dataframe = pd.DataFrame(lista_valores)

#así identificamos una columna
columna0 = dataframe[0]
 print(columna0)

#esto sirve para filtrar los valores de una columna
print(columna[columna > 0.40])
#se puede filtrar un dataframe también
print(dataframe[dataframe > 0.40])
