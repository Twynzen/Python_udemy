import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Estad%C3%ADsticas_de_la_Copa_Am%C3%A9rica'
webbrowser.open(website)


dataframe_copa= pd.read_clipboard()

print(dataframe_copa)
