#Entrada y salida de arrays

import numpy as np



array1 = np.arange(6)

#Así se guarda un array, el primer parametro es el nombre con elque se va a guardar
np.save('array1s', array1)
#Así se carga un array llamandolo por el parametro, se le coloca extyención npy
np.load('array1s.npy')

array2 = np.arange(8)
array3 = np.arange(-4,10)

np.savez('arrays',x=array1, y = array3)

array_recuperado = np.load('arrays.npz')

print(array_recuperado['y'])
#para salvarlo en un fichero txt
np.savetxt('mificheroarray.txt', array2, delimiter= ',')
array2_recuperado = np.loadtxt('mificheroarray.txt',delimiter=',')
print(array2_recuperado)
