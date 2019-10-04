
#Es como un array pero esta indexado por unos valores
import pandas as pd

serie1 = pd.Series([3,5,7])

print(serie1[1])

asignaturas = ['matematicas', 'historia', 'fisica', 'literatura']

notas = [8,6,9,7]

serie_notas_daniel = pd.Series(notas, index= asignaturas)

print(serie_notas_daniel)
print(serie_notas_daniel['fisica'])

print("Los valores que son mayores o iguales a la nota de 8",serie_notas_daniel[serie_notas_daniel>=8])

# Para mostrar en general lsod atos de una serie podemos usar estos metodos
serie_notas_daniel.index.name = 'Asignatura de Daniel'

print(serie_notas_daniel)

# este metodo to_dict crea un diccionario
diccionario = serie_notas_daniel.to_dict()
print(diccionario)


#También se puede hacer una suma entre 2 series
notas_ana = [7,8,5,9]

serie_notas_ana= pd.Series(notas_ana,index=asignaturas)

serie_notas_clase = (serie_notas_ana + serie_notas_daniel)/2

print("Las notas de Ana son: ", serie_notas_ana)
print("La media de la clase es: ",serie_notas_clase)
