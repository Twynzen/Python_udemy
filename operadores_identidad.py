frutas1 = ["manzana","pera"]
frutas2 = ["manzana","pera"]
frutas3 = frutas1

if frutas1 is frutas3:
    print("si es igual")
else:
    print("No son iguales")

frutas3.append("naranja")

print(frutas3)

if frutas1 is not frutas3:
    print("si es igual")
else:
    print("No son iguales")
