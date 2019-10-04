def saludar(nombre):
    """
    Esto será un comentario de la funcion saludar.
    Esta funcion recibira como parametro una cadena con el nombre e
    imprimirá por pantalla un saludo con el nombre concatenado
    """
    print("Buenos días "+ nombre)

saludar("Daniel")

#Muestra la documentación del metodo saludar
help(saludar)

class Saludos:
    """
    Esta clase tendrá dos funciones buenos_dias y adios
    ambas funciones recibiran como parametro un nombre
    """
    def buenos_dias(self, nombre):
        """ Esta funcion sirve para decir buenos dias a una persona """
        print("Buenos dias {}".format(nombre))

    def adios(self, nombre):
        """Esta funcion dice adios a una persona"""
        print("Adios {}".format(nombre))

saludo = Saludos()
saludo.adios("Daniel")

help(Saludos)

help(print)       
