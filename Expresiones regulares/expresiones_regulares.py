# search 
texto = "Hola, mi nombre es Daniel"
import re

#Permite buscar una cadena de variables, devuelve un objeto tipo Match
resultado = re.search("nombre", texto)

re.search("Daniel$", texto) #con el signo dolar buscará la última palabra de la cadena
re.search("^Hola", texto)#Buscara por la primera palabra de la cadena de texto
re.search("mi.*es", texto)# El punto y el * sirven para buscar lo que este entre medias de las palabras
if (resultado):
    print: ("Cadena encontrada")
else:
    print:("Cadena NO encontrada")

#findall

texto1 = """
Por ahora estoy aprendiendo python y logro
notar como puedo utilizar expresiones regulares por medio
de la libreria re
"""

re.findall("libreria.*python",texto1)# devuelve una lista con todas las coincidencias de en la linea con esas palabras

#split
texto2 = "La silla es blanca y vale 80"
re.split("\s", texto2)#sirve para dividir las palabras de las cadenas

#sub
texto3 ="La silla blanca vale 80"
re.sub("blanca","roja",texto3)#sustitulle la palabra indicada por la que sigue
