import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#creamos el componente label (etiqueta)

texto = "Hola pué"
etiquetaLabel = tkinter.Label(raiz,text=texto)
#esto configura el label
etiquetaLabel.config(fg="green",bg="lightgrey",font=("Cortana",30))
# lo muestra
etiquetaLabel.pack()

raiz.mainloop()
