#Los diccionarios son una coleccion de elementos que estan indexados no estan ordenados y se pueden modificar.

diccionario_colores = {"red":"rojo", "blue":"azul", "green":"verde"}
print(diccionario_colores)

print(diccionario_colores["red"])

valor = diccionario_colores["green"]

print(valor)

diccionario_colores["black"]= "negro"

print(diccionario_colores)

#esto elimina un valor
diccionario_colores.pop("blue")
del(diccionario_colores["red"])

print("Elimie los colores azul y rojo")
print(diccionario_colores)

for clave,valor in diccionario_colores.items():
    print(clave, valor)
