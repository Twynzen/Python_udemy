class claseSilla:
    #creaciónd e atributos
    color = "blanco"
    precio = 100

objetoSilla1 = claseSilla()

print(objetoSilla1.color)

objetoSilla2 = claseSilla()

objetoSilla2.color = "verde"
objetoSilla2.precio = 120

print(objetoSilla2.precio)

class Persona:
    #creaciónd e atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
     #creación de metodos
    def saludar(self):
        print("Hola, me llamo {} y tengo {} años".format(self.nombre, self .edad))

persona1 = Persona("Daniel",25)

print(persona1.saludar())
