import re

tekst = "Witaj Silksongo Americano"
result = re.match(r"""
                  
[A-Za-z]{3} # tu mam jakieś ciekawe coś
                  
""", tekst, re.VERBOSE) # sprawdza czy podany tekst od początku spełnia wymagania
# print(result)
# print(f"Początek: {result.start()}")
# print(f"Koniec: {result.end()}")
# print(f"Przedział: {result.span()}")
# print(f"Grupa: {result.group()}")


tekst = "01234-Paaaaa.aaaaP[]-85421"#"Jestem Gerald Piotruś von Minecraft 123 Gerald"

result = re.search(r"P[a-z.]{10}P\[\]", tekst) # 01234-sfhudfhdufdhfdfu-85421

print(result)
print(f"Początek: {result.start()}")
print(f"Koniec: {result.end()}")
print(f"Przedział: {result.span()}")
print(f"Grupa: {result.group()}")

# Proszę zapisać wywołanie funkcji re.search(), które zbada czy podany string jest
# adresem e-mail:

"""
[podkreślenia, cyfry, litery, kropki] @ [litery, kropki]
"""
email = "goku.drip_12@yahoo.com"

result = re.search(r"^[0-9a-z_.]+@[a-z.]+$", email)
print(result.group())



tekst = "Siema mały Polonezie!"                 
result = re.findall(r"[A-Za-z\w]{3}", tekst, re.ASCII)
print(result)


result = re.sub(r"[A-Za-z]{3}", "DRYDRY" , tekst)
print(result)

# Potrzebne symbole: \b \d * []

# Proszę napisać wywołanie funkcji, które znajdzie wszystkie liczby nieparzyste w ciągu,
# gdzie sa one podzielone spacjami.

ciag = "5 12 442 321 45 20 21 37"