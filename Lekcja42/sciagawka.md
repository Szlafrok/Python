# REST API, biblioteka requests

## Co to API?
(Application Programming Interface) to zestaw zasad i protokołów, które pozwalają różnym programom komunikować się ze sobą. Wyobraź sobie API jako kelnera w restauracji. Ty (klient) składasz zamówienie (żądanie), kelner (API) przekazuje to zamówienie do kuchni (serwera), a następnie kelner przynosi Ci jedzenie (odpowiedź).

## REST
REST (Representational State Transfer) to styl architektury, który umożliwia tworzenie API działających na zasadzie prostych zasad i protokołów. API, które jest zgodne z zasadami REST, nazywamy **REST API**. Takie API korzysta zazwyczaj z protokołu HTTP, aby umożliwić komunikację między aplikacjami. Oznacza to, że aplikacja może wysyłać żądania HTTP i oczekiwać odpowiedzi w formacie takim, jak JSON.
Protokół HTTP (HyperText Transfer Protocol) to protokół komunikacyjny, który określa sposób komunikacji między dwiema stronami w sieci, zwykle na linii klient - serwer. Taki protokół to zestaw kroków, których muszą przestrzegać obie strony, aby się sprawnie dogadywać. Przy postępowaniu zgodnie z tymi krokami obie strony wiedzą, jak zadawać komunikaty i co one oznaczają.

## Zasady REST
1. Architektura klient - serwer
Klient i serwer są oddzielone, dzięki czemu mogą rozwijać się kompletnie niezależnie. Jedyna komunikacja między nimi odbywa się poprzez API, na zasadzie wysyłania żądań i otrzymywania odpowiedzi.
2. Bezstanowość
Żądanie klienta wobec serwera musi zawierać wszystkie informacje niezależnie od dotychczasowej komunikacji - serwer nie przechowuje informacji na temat dotychczasowych żądań, które można wykorzystać jako kontekst do dalszej pracy.
**Uwaga:** przechowywanie danych np. jako forma dziennika (logu) dla administratora nie łamie tej reguły. Zasada bezstanowości jest złamana dopiero wtedy, kiedy użytkownik, wydając zapytanie, polega na swoich poprzednich zapytaniach, np. klient wysyła `GET /orders/next` i serwer zwraca kolejne zamówienie... ale tylko dlatego, że wcześniej klient wysłał `GET /orders/start`.
3. Jednolity interfejs
Wszystkie zasoby powinny być dostępne pod przewidywalnymi i intuicyjnymi adresami URL, a operacje na zasobach są realizowane za pomocą standardowych metod HTTP (np. GET, POST, PUT, DELETE). Klient może zmieniać zasoby nie bezpośrednio, tylko przez wysłanie jego reprezentacji, np. przy formacie JSON, podaje on nowe dane do określonego obszaru jako `{"name":"Jan Kowalski"}`, i dopiero serwer dokonuje stosownej zmiany.
4. Podział na zasoby
Adresy URL zasobów są unikalne. Zasoby to np. konkretne produkty, użytkownicy, zamówienia, etc. Przykładowo:
```
GET /users - pobierz listę wszystkich użytkowników
POST /users - utwórz nowego użytkownika
GET /users/1 - pobierz dane użytkownika o ID 1
```

### Podstawowe operacje REST API
- `GET` - Pobiera dane z serwera (np. listę użytkowników).
- `POST` - Tworzy nowe dane na serwerze (np. dodaje nowego użytkownika).
- `PUT` - Modyfikuje istniejące dane (np. aktualizuje dane użytkownika).
- `DELETE` - Usuwa dane z serwera (np. usuwa użytkownika).

### Kody rezultatów
To trzycyfrowe kody odpowiedzi serwera HTTP, które informują nas o wyniku przetwarzania żądania przez serwer. Każdy z kodów należy do 1 z 5 kategorii, a każda z tych kategorii ma swoje specyficzne znaczenie.
1. 1xx - Informational (Informacyjne)
Serwer otrzymał żądanie i jest w trakcie jego przetwarzania
> - 100 Continue: Serwer otrzymał początek zapytania i możemy kontynuować jego wysyłanie
> - 101 Switching Protocols: Żądaliśmy zmiany protokołu i serwer to zaakceptował
2. 2xx - Success (Sukces)
Żądanie zostało poprawnie odebrane, zrozumiane i przetworzone.
> - 200 OK: Żądanie zakończyło się sukcesem, a odpowiedź serwera zawiera dane (np. wyniki zapytania GET).
> - 201 Created: Zasób został utworzony pomyślnie (np. po zapytaniu POST).
> - 202 Accepted: Żądanie zostało przyjęte do przetworzenia, ale nie jest jeszcze zakończone.
> - 204 No Content: Żądanie zakończyło się sukcesem, ale odpowiedź nie zawiera żadnych danych (często przy DELETE).
3. 3xx - Redirection (Przekierowania)
Klient musi podjąć dodatkowe działania, żeby uzyskać dostęp do danego zasobu.
> - 301 Moved Permanently: Zasób został przeniesiony na stałe pod nowy URL.
> - 302 Found (lub 302 Moved Temporarily): Zasób jest tymczasowo dostępny pod innym URL.
> - 304 Not Modified: Zasób nie został zmieniony od ostatniego pobrania. To może się pojawić, kiedy korzystamy z cache'ingu (tymczasowego zapamiętywania plików przez przeglądarkę celem przyspieszenia działania). Jeśli otrzymamy ten kod, to klient ma już ten plik o który pytamy i nie musimy go pobierać ponownie. 
> - 307 Temporary Redirect: Podobny do 302, ale z gwarancją, że metoda, z której korzystamy nie powinna być zmieniona, np. nie używaj PUT zamiast POST, niech to dalej będzie PUT, aby wykonać tę operację.
4. 4xx - Client Error (błędy klienta)
Problem leży po stronie klienta, np. złe żądanie albo brak uprawnień.
> - 400 Bad Request: Żądanie jest niepoprawne lub niekompletne.
> - 401 Unauthorized: Brak autoryzacji – wymagane uwierzytelnienie.
> - 403 Forbidden: Klient ma uprawnienia, ale dostęp do zasobu jest zabroniony.
> - 404 Not Found: Serwer nie może znaleźć żądanego zasobu (np. niewłaściwy URL).
> - 405 Method Not Allowed: Metoda HTTP użyta w żądaniu nie jest dozwolona dla tego zasobu (np. POST na zasób dostępny tylko dla GET).
5. 5xx - Server Error (błędy serwera)
Problem wystąpił po stronie serwera mimo prawidłowego żądania.
> - 500 Internal Server Error: Wystąpił błąd na serwerze, nieokreślony.
> - 501 Not Implemented: Serwer nie obsługuje żądanej metody.
> - 502 Bad Gateway: Serwer pełni rolę bramki lub proxy i otrzymał nieprawidłową odpowiedź od serwera upstream.
> - 503 Service Unavailable: Serwer jest tymczasowo niedostępny (np. z powodu przeciążenia).
> - 504 Gateway Timeout: Serwer pełniący rolę bramki lub proxy nie otrzymał odpowiedzi w odpowiednim czasie od serwera upstream.