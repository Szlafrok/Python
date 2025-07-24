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


tekst = "01234-PaaaaaaaaaaP[]-85421"#"Jestem Gerald Piotruś von Minecraft 123 Gerald"

result = re.search(r"P[a-z]{10}P\[\]", tekst) # 01234-sfhudfhdufdhfdfu-85421

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