import pandas as pd
import numpy as np

listaValores = range (4)
listaIndices = list ('CABD')

serie1 = pd.Series(listaValores, index=listaIndices)

print(serie1)

#ordenar una serie1
print("ordenado por la serie",serie1.sort_index())
print("ordenado por los valores",serie1.sort_values())
print("ordenado por el ranking deposiciones",serie1.rank())
