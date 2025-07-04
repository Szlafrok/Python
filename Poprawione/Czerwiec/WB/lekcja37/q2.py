import re

def ocen_haslo(haslo):
    punkty = 0
    komunikaty = []

    try:
        if len(haslo) >= 12:
            punkty += 1
        else:
            raise ValueError("Hasło ma mniej niż 12 znaków.")

        if re.search(r'[A-Z]', haslo):
            punkty += 1
        else:
            raise ValueError("Brak wielkiej litery.")

        if re.search(r'[a-z]', haslo):
            punkty += 1
        else:
            raise ValueError("Brak małej litery.")

        if re.search(r'\d', haslo):
            punkty += 1
        else:
            raise ValueError("Brak cyfry.")

        if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=/\\[\]~`]', haslo):
            punkty += 1
        else:
            raise ValueError("Brak znaku specjalnego.")
            print("Hello World") # Zauważ, że print jest wyblakłe w środowisku!
            # wykonywanie tego bloku się zakończy po zgłoszeniu pierwszego błędu, przez co lista komunikaty
            # będzie zawierała tylko i wyłącznie 1 komunikat. Musiałbyś zrobić każde badanie w osobnym bloku try,
            # aby osiągnąć zamierzony przez Ciebie efekt.

        print("Hasło spełnia wszystkie wymagania. Mocne hasło! ✅")

    except ValueError as e:
        komunikaty.append(str(e))

    finally:
        if komunikaty:
            print("Wykryto problemy z hasłem:")
            for komunikat in komunikaty:
                print("⛔", komunikat)
        print(f"Ocena hasła: {punkty}/5")

if __name__ == "__main__":
    haslo = input("Wprowadź hasło: ")
    ocen_haslo(haslo)

# Naprawdę robi wrażenie! Wybiegłeś mocno do przodu, o Regexie będziemy się uczyli w drugiej połowie lipca.
# Podobnie jak w zadaniu z lekcji 36, poprosiłbym Cię o krótkie omówienie wykorzystanej przez Ciebie funkcji re.search(), oki?

# (4p / 4p) (+1 bonus za zaawansowanie!) (+1p za zwracanie powodu) (+1p za odpowiedź)

# Aktualizacja: nie dopatrzyłem 1 rzeczy w rozpatrywaniu zadania, w zwiazku z poprawką dodałem 1pkt