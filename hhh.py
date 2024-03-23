from googletrans import Translator

# Crear un objeto Translator
translator = Translator()

# Texto en español que deseas traducir
texto_espanol = "Hola, ¿cómo estás?"

# Realizar la traducción de español a inglés
traduccion_ingles = translator.translate(texto_espanol, src='es', dest='en')

# Imprimir el texto traducido a inglés
print(traduccion_ingles.text)