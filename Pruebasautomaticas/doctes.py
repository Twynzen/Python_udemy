#Generar pruebas dentro de la documentacion

def sumar(numero1, numero2):
    """
    La documentación de esta función
    Recibe 2 numeros como parametros y devuelve su sumar

    >>> sumar(4,3)
    7

    >>> sumar(5,3)
    7

    >>> sumar(2,1)
    3

    """
    return numero1 + numero2

resultado = sumar(2,3)
print(resultado)

import doctest
doctest.testmod()
