import requests
from googletrans import Translator
from Planeta import Planeta



class ApiPlanet:
    def __init__(self,planet):
            self.url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet}"
            print(self.url)

    def get_url(self):            
        response = requests.get(self.url)
        res = self.set_planet(response.json())
        return res

    def set_planet(self,planeta):
        data = planeta
        nombre = data["englishName"]
        numero_satelites = len(data["moons"])
        masa_kg = data["mass"]["massValue"] * 10 ** data["mass"]["massExponent"]
        volumen = data["vol"]["volValue"] * 10 ** data["vol"]["volExponent"]
        diametro = 2 * data["equaRadius"]
        distancia_media_sol = data["semimajorAxis"]
       
        res_planet = {"nombre":nombre,"numero_Satelites":numero_satelites,"masa_kg":masa_kg,"volumen":volumen,"diametro":diametro,"distancia":distancia_media_sol}
        return res_planet
        # Planeta(nombre,numero_satelites,masa_kg,volumen,diametro,distancia_media_sol)
    
text_trans = Translator()
texto_espanol = "saturno"

# Realizar la traducción de español a inglés
planet_en = text_trans.translate(texto_espanol, src='es', dest='en')

res = ApiPlanet(planet_en.text)

print(res.get_url())

