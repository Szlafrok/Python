import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

def get_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    return response.json()

def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default'] # Zapytanie wynika z analizy składni słownika zwróconego przez get_pokemon_info()
    return link
 
def get_pokemon_types(pokemon_info):
    types = []
    for item in pokemon_info['types']:  # Zapytanie wynika z analizy składni słownika zwróconego przez get_pokemon_info()
        type = item['type']['name']
        types.append(type)
    return types

def scrap_pokemon_list():
    url = 'https://pokelife.pl/pokedex/index.php?title=Lista_Pokemon%C3%B3w_Kanto'
    response = requests.get(url)
    #print (response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemons_list = []
    table = soup.find('table', class_ = 'Tabela1')
    rows = table.find_all('tr')
    for row in rows[1:]:
        columns = row.find_all('td')
        pokemon = (columns[2].text[:-1], f"No.{columns[0].text[:-1]}")
        pokemons_list.append(pokemon)
        #print(pokemon)
    pokemons_without_mega = [pokemon for pokemon in pokemons_list if ("Mega" not in pokemon[0] and "Gigantamax" not in pokemon[0])]
    for pokemon in pokemons_without_mega:
        pass #print(pokemon)
    return pokemons_without_mega
    
    # [wyrażenie for element in obiekt if warunek] [x**2 for x in range(10)]

info_list = []
pokemon_list = scrap_pokemon_list()
for pokemon in pokemon_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[1][3:]) # Pobranie informacji o pokemonie na podstawie ID
        image_url = get_pokemon_image(pokemon_info) # Pobranie linku do obrazu Pokemona
        img_data = requests.get(image_url).content # Zaczerpnięcie obrazu bezpośrednio ze strony (pokazywaliśmy to na lekcji, image_url prowadzi do strony z wyłącznie podanym obrazkiem)
        pokemon_types = get_pokemon_types(pokemon_info) # Pobiera typy Pokemona (żywioły).

        info_list.append({ # Najłatwiej i najczytelniej będzie zrobić zapis jako słownik
            "name": pokemon[0],
            "id": pokemon[1],
            "info": pokemon_info,
            "image" : img_data,
            "types": pokemon_types
        })
    except Exception as e:
        print(pokemon, e)

pdf = FPDF()

pdf.add_font("DejaVu", "", "Lekcja44/DejaVuSansCondensed.ttf")

for pokemon in info_list:
    pdf.add_page(format = 'A5')
    pdf.set_font("DejaVu", size=16)
    pdf.text(x=5, y = 10, text=f"#{pokemon["id"]} {pokemon["name"]}") # Nagłówek z danymi osobowymi Pokemona
    pdf.image(pokemon["image"], x=30, y=10, w=100, h = 100 ) # umieszczenie obrazu Pokemona
    pdf.set_font("DejaVu", size=12)
    type_tekst = ', '.join(pokemon["types"]) # Wypisanie typów pokemona po przecinku
    pdf.text(x = 50, y = 120, text=f"Typ: {type_tekst}")

pdf.output("Lekcja44/Pokedex.pdf")

print("Zakończone!")

"""
OPIS PROBLEMU:

W czasie lekcji wyskoczyły błędy związane z następującymi Pokemonami:
Nidoran, Nidoran, Mr Mime, Mewtwo X, Mewtwo Y

Ich nazwy były pobierane z Pokedexu poprawnie, natomiast serwer API nie
rozpoznał tych nazw. Powinny być to odpowiednio: nidoran-f, nidoran-m,
mr-mime, mewtwo-mega-x, mewtwo-mega-y. Podstawienie nazwy np. "Mr Mime" do
linku wykorzystywanego przez zapytanie API generowało błąd.

Zgodnie z dokumentacją PokeAPI (https://pokeapi.co/docs/v2#pokemon) zapytanie
o Pokemona można wykonać z wykorzystaniem jego ID lub NAZWY.

Wykorzystanie ID Pokemona zamiast jego nazwy jest lepszym pomysłem, ponieważ
indeks zawsze będzie liczbą całkowitą i przez to szansa problemu jest dużo
mniejsza. Strona regionu Kanto była prawdopodobnie niedawno aktualizowana i
dodano do niej Pokemony Mewtwo X i Mewtwo Y - nawet jeśli wykonamy zapytanie
za pomocą ID Pokemona, otrzymamy błąd, ponieważ nie istnieje taki zasób na serwerze.

Dla poprawnie wczytanych Pokemonów możemy rozpocząć analizę danych i tworzenie Pokedexu.

"""