#Convertir datos de un diccionario python a una estructura JSON
producto1 = {"nombre":"silla", "color":"blanco", "precio":80}
import json
estructura_json = json.dumps(producto1)

print(producto1["nombre"])

#convertir estructura JSON (estructura_json) en un diccionario en python

producto2 = json.loads(estructura_json)
print(producto2["color"])
