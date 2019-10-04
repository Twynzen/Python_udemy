import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente "popup" es una ventanda de informacion

def avisar():
    tkinter.messagebox.showinfo("Titulo","mensaje con la informacion")

boton = tkinter.Button(raiz, text="Pulsar para aviso", command = avisar)
boton.pack()






raiz.mainloop()
