#realizar un mapeo de una función para los valores de una lista
def multiplicar(numero):
    return numero * 2

print(multiplicar(2))

numeros = [2,4,6]

mapeo = map(multiplicar, numeros)

print(mapeo)

resultado = list(mapeo)

print(resultado)


#también se puede hacer con lambda
lista_resultado = list(map(lambda numero: numero *2, numeros))
