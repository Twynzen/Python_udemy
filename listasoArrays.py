#lISTAS
colores = ["rojo", "verde", "azul"]

#rojo
colores[0]
#verde
colores[1]

print(colores)

#cambiamos el valores
colores[2]= "amarillo"

print(colores)

#contar cuantas variables tiene el array
print(len(colores))

#agregar un elemento al array
colores.append("cafe")

print(colores)

#para borrar un elemento del array
colores.remove("rojo")

#bucle for para que imprima cada elemento del array
for color in colores:
    print(color)
#borrar los elementos del array fila
colores.clear()
print(colores)
    
