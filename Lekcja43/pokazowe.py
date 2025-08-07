import requests
from pprint import pprint

API_KEY = "cd5b3262f4a1a6071dcf78eba8229b22"

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    # print(response.status_code)
    # pprint(response.json())
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    name = response.json()[0]["name"]
    country = response.json()[0]["country"]
    la_ver = response.json()[0]["local_names"]

    return lat, lon, name, country

# a, b, c, d = (..., ..., ..., ...)

"""
Proszę napisać skrypt, który na podstawie powyższej funkcji wczyta od użytkownika MIASTO DOCELOWE
oraz MIASTO, Z KTÓREGO ZACZYNA DROGĘ i zapisze do zmiennych dla obu miast: wysokość i szerokość geograficzną
(latitude, longitude), nazwę i państwo.
"""

# city_1 = input("Proszę podać miasto startowe: ")
# city_2 = input("Proszę podać miasto docelowe: ")
# lat_1, lon_1, name_1, country_1 = check_coordinates(city_1, API_KEY)
# lat_2, lon_2, name_2, country_2 = check_coordinates(city_2, API_KEY)

# print(lat_1, lon_1, name_1, country_1)
# print(lat_2, lon_2, name_2, country_2)

#print(check_coordinates("Rzeszów", API_KEY))

def get_weather_info(lat, lon, API_KEY):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=PL&units=metric")
    # print(response.status_code)
    # pprint(response.json())
    response_json = response.json()
    weather = response_json['weather'][0]['description']   # pogoda
    temperature = response_json['main']['feels_like']     # temperatura odczuwalna
    pressure = response_json['main']['pressure'] # ciśnienie
    humidity = response_json['main']['humidity'] # wilgotność
    return weather, temperature, pressure, humidity

# weather, temperature, preesure, humidity = get_weather_info(lat_2, lon_2, API_KEY)

# print(f"Pogoda: {weather}")
# print(f"Temperatura: {temperature} st. C")
# print(f"Ciśnienie: {preesure} hPa")
# print(f"Wilgotność: {humidity}%")

def get_country_data(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    # pprint(response.json())
    full_name = response.json()[0]['name']['common']
    currency = list(response.json()[0]['currencies'].keys())[0]
    return full_name, currency

# country_name_orig, country_currency_orig = get_country_data(country_1)
# country_name_dest, country_currency_dest = get_country_data(country_2)

# print(f"Państwo: {country_name_dest}")
# print(f"Waluta: {country_currency_dest}")

def get_currency_ratio(origin_curr, dest_curr):
    if origin_curr != "PLN":
        url = f"https://api.nbp.pl/api/exchangerates/rates/B/{origin_curr}/"
        response = requests.get(url)
        origin_rate = response.json()['rates'][0]['mid']
    else:
        origin_rate = 1

    if dest_curr != "PLN":
        url = f"https://api.nbp.pl/api/exchangerates/rates/B/{dest_curr}/"
        response = requests.get(url)
        dest_rate = response.json()['rates'][0]['mid']
    else:
        dest_rate = 1
    # print(origin_rate, dest_rate)
    return origin_rate / dest_rate

# ratio = get_currency_ratio(country_currency_orig, country_currency_dest)
# print(f"Kurs wymiany waluty: {ratio}")

origin_loc = None
destin_loc = None
comm = ""

while True:
    print("Jaką akcję chcesz wykonać?")
    print("    1. Podaj/zamień miejsce startowe")
    print("    2. Podaj/zamień miejsce docelowe")
    print("    3. Sprawdź lokalizację miejsca startowego")
    print("    4. Sprawdź lokalizację miejsca docelowego")
    print("    5. Sprawdź pogodę miejsca startowego")
    print("    6. Sprawdź pogodę miejsca docelowego")
    print("    7. Poznaj kursy wymiany walut")
    print("    8. Koniec")
    print(comm)
    comm = ""
    chosen_option = int(input())

    if chosen_option == 1:
        pass
    elif chosen_option == 2:
        pass
    elif chosen_option == 3:
        pass
    elif chosen_option == 4:
        pass
    elif chosen_option == 5:
        pass
    elif chosen_option == 6:
        pass
    elif chosen_option == 7:
        pass
    elif chosen_option == 8:
        quit()