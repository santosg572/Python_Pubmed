from translate import Translator


# Configura el traductor del inglés ('en') al español ('es')

traductor = Translator(from_lang="en", to_lang="es")

file = "parkinson_title.txt"

fil = open(file, 'r')

datos = fil.readlines()

n = len(datos)

i = 0

while i < 1000:
  ss = datos[i]
  ss = ss.replace('\n', '')
  print(ss)
  i = ss.find('"')
  i = ss.find('"',i+1)   
  i = ss.find('"',i+1)
  palabras = ss[i:]
  texto_espanol = traductor.translate(palabras)
  print(texto_espanol)  
  i = i+1

'''
# Texto de ejemplo en inglés
texto_ingles = "Hello, how are you? Welcome to Python programming."


# Realiza la traducción

texto_espanol = traductor.translate(texto_ingles)

# Muestra el resultado
print("Original:", texto_ingles)
print("Traducido:", texto_espanol)

'''
