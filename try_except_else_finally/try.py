# TRY permite verificar si un bloque de codigo contiene errores
#numero1 = 5
#numero2 = 0
#division = numero1 / numero2
#Esto genera un error que se llama ZeroDivisionError


try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError: #Podemos aclarar el error esperado con un mensaje predefinido
    print ("Error, division de cero")
except:
    print ("Ha habido un error")

try:
    numero1 = 5
    numero2 = 10
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print ("Error, division de cero")
else:
    print("La division funciona correctamente")

#Finally permite ejecutar un codigo independiente del resultado del try y del except

 try:
     numero1 = 5
     numero2 = 10
     division = numero1 / numero2
     print(division)
 except ZeroDivisionError:
     print ("Error, division de cero")
 else:
     print("La division funciona correctamente")
finally:
    print("Esta prueba de try ha acabado")
