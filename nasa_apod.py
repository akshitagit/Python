import urllib.request
import json
import webbrowser
import wget
from datetime import date
import os

# Definir index
api_key = 'api_key=DEMO_KEY'
url = 'https://api.nasa.gov/planetary/apod?'

# Chamar o webservice
urlobj = urllib.request.urlopen(url + api_key)


# Lendo o objeto
urlread = urlobj.read()

#Abrindo arquivo
data_atual = date.today()
name_image = "Img_of_day_{}.png".format(data_atual)

# Decodificar JSON para a estrutura do python
decodeurl = json.loads(urlread.decode('utf-8'))
url_final = decodeurl['hdurl']

# Mostrar o arquivo pythônico
print("\n\nArquivo Python Convertido")
local_name_img = wget.download(url_final)
comando = "mv {} {}".format(local_name_img, name_image)

os.system(comando)

# Usando o firefox para abrir o HTTPS URL
webbrowser.open(url_final)
