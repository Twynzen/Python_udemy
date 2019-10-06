#Es una represantación grafica de una varibale o datos en forma de barras,
#donde la superficie de cada barra es proporcional a la frecuencia de los valores representados
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

datos1 = np.random.randn(100)
print(datos1)

mpl.pyplot.hist(datos1)
