#así se puede combinar dataframe de diferentes formas
import pandas as pd
import numpy as np
lista_valores = np.arange(25).reshape(5,5)

dataframe = pd.DataFrame(lista_valores)
print(dataframe)
#esto genera 5 numeros de forma aleatoria
combinacion_aleatoria = np.random.permutation(5)
#con esta combinacion organizamos el dataframe
print(dataframe.take(combinacion_aleatoria))
