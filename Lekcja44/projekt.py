import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    return response.json()

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
        print(pokemon)
    return pokemons_without_mega
    
    # [wyrażenie for element in obiekt if warunek] [x**2 for x in range(10)]

pokemon_list = scrap_pokemon_list()
for pokemon in pokemon_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[1][3:])
        print(pokemon)
    except Exception as e:
        print(pokemon[1], e)