#así se reemplazan datos en Series
import pandas as pd

serie = pd.Series([1,2,3,4,5], index=list('abcde'))

#así se cambia un valor
serie = serie.replace(1,6)

print(serie)
#así se cambia otro ejemplo

serie = serie.replace({2:8,3:9})
print(serie)
