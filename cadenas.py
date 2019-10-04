nombre = "Daniel"
print("Buenos días "+nombre)

# . format

nombre2 = "Armando"
edad = 23
print("Buenos días {}, Feliz cumpleaños {}".format(nombre2,edad))

resultado = 10 / 3
print("El resultado acortando decimales es: {r:1.3f}".format(r=resultado))

# f-strings

nombre3 = "Alejandra"
edad = 20
print(f"Buenos días {nombre3}, feliz cumpleaños {edad}")

#entrada por teclado
#input
print("Introduzca un nombre")
entrada = input()
print("hola "+ entrada)
