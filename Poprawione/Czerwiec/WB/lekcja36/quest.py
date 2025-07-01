uprawnienia = {
    "guest": {"login", "logout", "view_file"},
    "user": {"login", "logout", "view_file", "create_file", "modify_file"},
    "operator": {"login", "logout", "view_file", "create_file", "modify_file", "delete_file"},
    "admin": {"login", "logout", "view_file", "create_file", "modify_file", "delete_file", "manage_users"},
    "root": {"login", "logout", "view_file", "create_file", "modify_file", "delete_file", "manage_users", "system_config"}
}


def porownaj_role(rola1, rola2):
    if rola1 not in uprawnienia or rola2 not in uprawnienia:
        print("Nie ma takiej roli w systemie.")
        return

    tylko_rola1 = uprawnienia[rola1] - uprawnienia[rola2]
    tylko_rola2 = uprawnienia[rola2] - uprawnienia[rola1]

    print(f"\nRóżnice między rolą '{rola1}' a '{rola2}':")
    print(f"- Tylko {rola1}: {tylko_rola1 or 'brak'}")
    print(f"- Tylko {rola2}: {tylko_rola2 or 'brak'}")


def main():
    print("Dostępne role:", ", ".join(uprawnienia))
    r1 = input("Podaj pierwszą rolę: ")
    r2 = input("Podaj drugą rolę: ")

    if r1 == r2:
        print("Muszą być dwie RÓŻNE role!")
    else:
        porownaj_role(r1, r2)

main()

# Rozwiązanie jest poprawne i bardzo eleganckie, wykorzystujesz płynnie wszystkie mechaniki, także
# pewną, której nie poruszaliśmy na zajęciach. Prosiłbym Cię o zgłoszenie się początkiem przerwy lub
# końcem następnej lekcji i krótkie omówienie struktury z linijek 19-20, tej wykorzystującej OR-y, oraz
# operacji w linijkach 15 - 16: co pozwala Ci na wykonanie takiego odejmowania?

# (+3 / 3), zadanie zrobione bardzo ładnie, ale proszę o to krótkie omówienie :)