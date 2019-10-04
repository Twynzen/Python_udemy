#permiten verificar si un objeto esta dentro de  una lista de valores u otro objeto

frutas1 = ["manzana", "pera", "naranja"]
frutas2 = "pera"

if frutas2 in frutas1:
    print("Sí esta dentro ")
    frutas2="papa"
else:
    print("No esta dentro ")

if frutas2 not in frutas1:
    print("NO esta dentro ")

else:
    print("si esta dentro ")
