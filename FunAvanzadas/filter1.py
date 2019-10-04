#Función para filtrar resultados segun una condición

def positivo(numero):
    if numero >0:
        return True
    else:
        return False


print(positivo(4))
print(positivo(-7))

numeros = [2,4,-5,-3,7,-9]
filtro = filter (positivo, numeros)

resultado = list(filtro)
print(resultado)
