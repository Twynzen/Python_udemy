fichero = open("ficherotexto.txt","at")#a : de appen (significa añadir más info ) t: de texto

cadena_para_incluir = "\nEsta es la tercera fila del fichero"

fichero.write(cadena_para_incluir)

fichero.close()
