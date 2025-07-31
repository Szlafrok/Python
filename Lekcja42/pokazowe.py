import requests
from pprint import pprint

API_KEY = "cd5b3262f4a1a6071dcf78eba8229b22"

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    print(response.status_code)
    pprint(response.json())
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    name = response.json()[0]["name"]
    country = response.json()[0]["country"]
    la_ver = response.json()[0]["local_names"]["la"]
    #print(la_ver)

    return lat, lon, name, country

# a, b, c, d = (..., ..., ..., ...)

"""
Proszę napisać skrypt, który na podstawie powyższej funkcji wczyta od użytkownika MIASTO DOCELOWE
oraz MIASTO, Z KTÓREGO ZACZYNA DROGĘ i zapisze do zmiennych dla obu miast: wysokość i szerokość geograficzną
(latitude, longitude), nazwę i państwo.
"""

city_1 = input("Proszę podać miasto startowe: ")
city_2 = input("Proszę podać miasto docelowe: ")
lat_1, lon_1, name_1, country_1 = check_coordinates(city_1, API_KEY)
lat_2, lon_2, name_2, country_2 = check_coordinates(city_2, API_KEY)

print(lat_1, lon_1, name_1, country_1)
print(lat_2, lon_2, name_2, country_2)

#print(check_coordinates("Rzeszów", API_KEY))