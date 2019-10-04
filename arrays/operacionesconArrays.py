import numpy as np

array1 = np.array([1,2,3,4])

array1 += 4

print("sumandole 4 al array",array1)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
arraydoble = np.array(lista_doble)

sumarrdo = arraydoble + 5
print("Un array doble sumado con 5",sumarrdo)

mulvarrdo = arraydoble *5
print("Multiplicacion de array doble * 5",mulvarrdo)

elevaarrdo = arraydoble ** 5
print("Un array doble elevado a 5",elevaarrdo)
