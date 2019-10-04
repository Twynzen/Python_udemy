colores = ["verde","azul","rojo"]
for color in colores:
    print(color)


cadena = "hola mundo"
for caracter in cadena:
    print(caracter)


#para mpas info documentacion de range
range(8)

for numero in range(3,8):
    print(numero)

#break

for numero in in range(10):
    if (numero == 5):
        break
    print(numero)


#continue

for numero in range(10):
    if(numero ==6):
        continue
    print(numero)

#doble for

for numero1 in range(4):
    for numero2 in range(3):
        print(numero1,numero2)
