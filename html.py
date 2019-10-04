import urllib.request as rq
import lxml.etree as et
import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Estad%C3%ADsticas_de_la_Copa_Am%C3%A9rica'
dataframe = pd.io.html.read_html(url)
#print(dataframe)

#para organizar la tabla que se saca de l web
dataframe_futbol = dataframe[0]


#para ver las columnas
#print(dataframe_futbol.loc[0])


#con este metodo se crea un diccionario
dict(dataframe_futbol.loc[0])

#Para renonmbrar las columnas con el diccionario creado
dataframe_futbol = dataframe_futbol.rename(columns=dict(dataframe_futbol.loc[0]))




#para borrar una columnas
dataframe_futbol= dataframe_futbol.drop(0)
print(dataframe_futbol)
