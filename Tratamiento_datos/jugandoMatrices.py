# concatenación de arrays, series y dataframes
import pandas as pd
import numpy as np
array1 = np.arange(9).reshape(3,3)

print(array1)

#asi se unen 2 arrays, el axis es para cambiar las columnas algo así
print(np.concatenate([array1,array1], axis=1))

serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([4,5,6], index=['d','e','f'])

#así se concatenan 2 series las keys es para añadir una clave extra
print(pd.concat([serie1,serie2], keys=['serie1','serie2']))

#creamos dataframes
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns = ['a','b','c'])
dataframe2 = pd.DataFrame(np.random.rand(2,3), columns = ['a','b','c'])

#asi se concatenan el ignore_index es para que salgan ordenados
dataframe3 = pd.concat([dataframe1,dataframe2], ignore_index=True)
print(dataframe3)
