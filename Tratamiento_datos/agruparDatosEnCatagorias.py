import pandas as pd
import numpy as np

precios  = [42,55,48,23,5,21,88,34,26]
rango = [0,10,20,30,40,50,60,70,80,90,100]

#con este metodo podemos agrupar los precios en un rango
precio_rango = pd.cut(precios, rango)
print(precio_rango)

#Este metodo nos dice  la cantidad de valores en un rango especifico
print(pd.value_counts(precio_rango))
