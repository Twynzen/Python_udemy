import pandas as pd
import numpy as np

lista_valores = np.arange(3)

lista_indices = ['il','i2','i3']

serie = pd.Series(lista_valores, index=lista_indices)

print(serie)

#se puede acceder así:
serie['i2']

#puede devolver el conjunto de valores
serie[0:2]

# con una condiciónote
serie[serie > 1]
