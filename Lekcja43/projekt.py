import requests
from pprint import pprint

API_KEY = "cd5b3262f4a1a6071dcf78eba8229b22" # Skorzystajcie tu ze swojego klucza!

def check_coordinates(city: str, API_KEY: str) -> tuple:
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    lat = response.json()[0]["lat"] # szerokość geograficzna
    lon = response.json()[0]["lon"] # długość geograficzna
    name = response.json()[0]["name"] # nazwa miasta
    country = response.json()[0]["country"] # państwo

    return lat, lon, name, country

def get_weather_info(lat: float, lon: float, API_KEY: str) -> tuple:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=PL&units=metric")
    response_json = response.json()
    weather = response_json['weather'][0]['description']   # pogoda
    temperature = response_json['main']['feels_like']     # temperatura odczuwalna
    pressure = response_json['main']['pressure'] # ciśnienie
    humidity = response_json['main']['humidity'] # wilgotność
    return weather, temperature, pressure, humidity

def get_country_data(country_code: str) -> tuple:
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    full_name = response.json()[0]['name']['common']
    currency = list(response.json()[0]['currencies'].keys())[0]
    return full_name, currency

def get_currency_ratio(origin_curr: str, dest_curr: str) -> float:
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
    return origin_rate / dest_rate

origin_loc = None # Miasto startowe
destin_loc = None # Miasto końcowe
comm = "" # Komunikat podawany po wykonaniu polecenia. Domyślnie pusty.

while True:
    print("Jaką akcję chcesz wykonać?")
    print(f"    1. Podaj/zamień miejsce startowe / Aktualnie: {origin_loc if origin_loc else "Brak"}")
    print(f"    2. Podaj/zamień miejsce docelowe / Aktualnie: {destin_loc if destin_loc else "Brak"}")
    print("    3. Sprawdź lokalizację miejsca startowego")
    print("    4. Sprawdź lokalizację miejsca docelowego")
    print("    5. Sprawdź pogodę miejsca startowego")
    print("    6. Sprawdź pogodę miejsca docelowego")
    print("    7. Poznaj kursy wymiany walut")
    print("    8. Koniec")
    print(comm)
    comm = "" # czyszczenie komunikatu
    chosen_option = int(input())

    if chosen_option == 1:
        origin_loc = input("Podaj miasto startowe: ")

    elif chosen_option == 2:
        destin_loc = input("Podaj miasto docelowe: ")

    elif chosen_option == 3: # Sprawdź zadanie domowe!
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