#Permite generar documentacion automatica desde la consola o terminal de comandos

class Saludos:
    """
    Esta sería la documentación de la clase silla
    tendrá 2 funciones buenos días y adios, ambas
    tendrán necesario pasarle un parametro con el nombre de la persona
    """
    def buenos_dias(self, nombre):
        """ sirve para dar los buenos días a un nombre introduccido con parametro"""
        print("Buenos días {}".format(nombre))
    def adios(self, nombre):
        """ Sirve para decir adios junto con el nombre puesto en parametro"""
        print("Adios {}".format(nombre))
#Utilizo el pydoc + la ruta donde esta el recurso, utilizar pydoc tiene muchas funciones con -w para crear un formato html de la documentacion
