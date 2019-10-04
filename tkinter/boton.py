import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componenete button

#Definimos la funcion accion
def accion():
    print("Soy la funcion accion escribiendo")
boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
#configuracion del boton
boton.config(fg="green")
boton.pack()

raiz.mainloop()
