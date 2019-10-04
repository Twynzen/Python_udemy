#así se combinan series y dataframes

import pandas as pd
import  numpy as np

serie1 = pd.Series([1,2,np.nan])

serie2 = pd.Series([4,5,6])

serie3 = serie1.combine_first(serie2)

print("Asi se combinan 2 series",serie3)

lista_valores0 = [1,2,np.nan]
dataframe1 = pd.DataFrame(lista_valores0)

lista_valores1 = [4,5,6]
dataframe2 = pd.DataFrame(lista_valores1)

dataframe3 = dataframe1.combine_first(dataframe2)

print(dataframe3)
