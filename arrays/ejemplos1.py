import numpy as np

np.zeros(4)
#crea elementos con un cero

cero = np.zeros(4)
print("ceros",cero)

unos = np.ones(4)
print("unos",unos)


creciendo = np.arange(4)
print("Arrays que contienen numeros en incremento",creciendo)
#Un arange es un recorrido de numeros de un valor definido
#En este caso va a ser desde -2 hasta 20 y de 2 en 2
dosendos = np.arange(-2,30,2)
print("Arrays ordenados de 2 en 2",dosendos)

#formas de lalmar un arrya en 2 diferentes maneras de mostrarlo como lo que tiene o como el conjunto qué es mazomenos eso entendi
lista1 = [1,2,3,4]
array1 = np.array(lista1)

print("Formas de mostrar un array",lista1, array1)

lista1=[1,2,3,4]
lista2=[5,6,7,8]

lista_doble = (lista1, lista2)

print("Un array doble",lista_doble)

array_doble = np.array(lista_doble)

print("Un array de 2 elemntos cada elemento una lista",array_doble)

#mostrar la forma de los Arrays
print("mostrar la forma de los Arrays",array_doble.shape)
#mostrar el tipo de array
print("El tipo de arrays es: ",array_doble.dtype )
