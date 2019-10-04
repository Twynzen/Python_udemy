rango = range(0,11)
for numer in rango:
    print(numer)


#Creación de función generadoras se llama pares
def pares(maximo):
    for numer in range(maximo):
        if (numer %2 == 0):
            #yield devuelve valores hasta un maximo
            yield numer




maximo = 11
for numero in pares(maximo):
    print (numero)
