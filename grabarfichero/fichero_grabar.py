
#Esto crea el fichero
fichero = open("fichero_para_grabar.txt","wt")# la W es de : write. Y la T es de: text

texto_del_fichero = "Hola, esta es la linea que vamos a grabar en el fichero de texto"

#con el metodo write guardamos  el texto dentro del fichero
fichero.write(texto_del_fichero)

fichero.close()
