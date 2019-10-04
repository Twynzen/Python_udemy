import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Creamos el componente entry, es decir un campo de entrada de datos

entrada = tkinter.Entry(raiz)
entrada.config(justify="center",show="*") #el show permite cambiar los caracteres intrucidos por asteriscos
entrada.pack()

raiz.mainloop()
