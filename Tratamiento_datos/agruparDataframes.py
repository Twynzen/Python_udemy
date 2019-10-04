import pandas as pd
import numpy as np

lista_valores = {'clave1':['x','x','y','y','z'],
                 'clave2':['a','b','a','b','a'],
                 'datos1':np.random.rand(5),
                 'datos2':np.random.rand(5)}
print(lista_valores)

dataframe = pd.DataFrame(lista_valores)

print(dataframe)

#queremos clasificar datos de los datos 1 en funcion que tengan de la clave 1
grupo =dataframe['datos1'].groupby(dataframe['clave1'])

print(grupo.mean())
