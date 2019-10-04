import pandas as pd

lista_valores0 = [1,2,3]
lista_indices0 = ['a','b','c']
serie = pd.Series(lista_valores0, index=lista_indices0)


print(serie)

#las series no pueden cambiar sus indices
print(serie.index[0])

lista_valores1 = [[8,7,6],[3,5,8],[4,8,7]]
lsita_indices1 = ['matematicas','historia','fisica']
lista_nombres = ['Antonio','daniel','ale']

dataframe = pd.DataFrame(lista_valores1, index= lsita_indices1, columns= lista_nombres)

#podemos utilizar dataframe para traer datos del array o matriz
print(dataframe.index)
print(dataframe.index[2])
