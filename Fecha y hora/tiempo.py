from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

ano = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

# hora

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

#las llaves sustitullen los calores
print(" La hora es {}:{}:{}".format(hora,minutos,segundos))
