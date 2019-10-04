def saludar():
    print("Que honda")
print("-----------------")

saludar()

def llamado(nombre):
  print("Hola que tal "+ nombre)

nombre = "Daniel"
llamado(nombre)

def sumar(numero1, numero2):
    suma = (numero1 + numero2)#no se syma correctamente debo arreglarlo
    return suma

print("Diga un numero")
numero1 = input()

print("Diga otro numero")
numero2 = input()
resultado = sumar(numero1,numero2)

print(resultado)

colores = ["rojo","blanco","verde"]

def incluir_color(colores,color):
    colores.append(color)

color = "negro"
incluir_color(colores,color)

print(colores)
