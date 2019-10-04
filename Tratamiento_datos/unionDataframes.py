import pandas as pd
#Asi se crea un dataframe
dataframe1 = pd.DataFrame({'c1':['1','2','3'], 'clave':['a','b','c']})

print(dataframe1)

dataframe2 = pd.DataFrame({'c2': ['4','5','6'], 'clave':['c','b','e']})

#Para unir un DataFrame

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2)
print(dataframe3)

#para que mantanga las filas del dataframe 1
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2,on ='clave', how='left')
#para que mantanga las filas del dataframe 2
dataframe5 = pd.DataFrame.merge(dataframe1, dataframe2,on ='clave', how='right')

print(dataframe4)
print(dataframe5)

#pone todos los valores de ambos dataframes
dataframe6 = pd.DataFrame.merge(dataframe1, dataframe2,on ='clave', how='outer')
print(dataframe6)
