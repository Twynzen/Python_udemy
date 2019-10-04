import pandas as pd

#primero creamos un array
#este array es de 4 filas y 2 columnas
lista_valores0 = [[1,2],[1,2],[5,6],[5,8]]

lista_indices0 = list('mnop')

lista_columnas = ['valor1','valor2']

dataframe = pd.DataFrame(lista_valores0, index= lista_indices0, columns= lista_columnas)

print(dataframe)
#Este metodo elimina las filas repetidas
print(dataframe.drop_duplicates())


dataframe2= dataframe.drop_duplicates()
#para modificar columnas, el las para que elija mantener el último valor
print(dataframe2.drop_duplicates(['valor1'], keep='last'))
