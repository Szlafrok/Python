## Inżynieria wsteczna (5 pkt)

Dany jest program w Pythonie:
```py
from bs4 import BeautifulSoup
import requests
import regex as re
import time

def pobierz_dane(argumencik):
    wyniczek_jakis_zabawny = []
    i = 1
    while True:
        print(f"Analysing page: {i}")
        data = requests.get(f"https://scratch.mit.edu/users/{argumencik}/followers/?page={i}")
        if not data.status_code == 200:
            break
        mniam = BeautifulSoup(data.content, 'html.parser')
        elementy = mniam.find_all('span', class_ = 'title')
        for elem in elementy:
            text = re.search(r'/users/[A-Za-z0-9_\-]+/', str(elem), flags = re.MULTILINE).group()
            wyniczek_jakis_zabawny.append(text[7:-1])
        i += 1

    return wyniczek_jakis_zabawny

start = time.time()
result = pobierz_dane("KamiennyGigant")
clock = time.time() - start

print(result)
print(len(result))
print(f"Time: {round(clock, 2)}s")
```
### a) Analiza skryptu (3 pkt)
Proszę przeanalizować podany kod, i określić jego działanie, wraz z uzasadnieniem i podaniem kroków prowadzących do wyciągnięcia przez Ciebie wniosków.

### b) Tester płakał jak czytał (2 pkt)
Proszę odpowiednio zmodyfikować powyższy kod tak, aby dało się z niego sprawnie wyciągnąć informację, co on robi. Co należy poprawić i dlaczego?

---
## Konto na GitHub (5 pkt)
Proszę założyć konto na GitHub i przesłać nazwę użytkownika na czacie  podczas zajęć trenerowi prowadzącemu lub mnie drogą mailową. Proszę to zrobić PRZED KOŃCEM KURSU, ponieważ później będę zamykał repozytorium na GitHubie i pozostawiał dostęp tylko dla Was!

*Nazwy użytkownika przesłali: Wiktor, Bazi, Alan, Patryk* ✅