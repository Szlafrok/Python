(+3 pkt) (1.07.2025)

Proszę przygotować struktury przechowująceuprawnienia poszczególnych użytkowników - przykładowo użytkownicy: `root`, `admin`, `operator`, `user`, `guest`, itd. Przykładowo:
```py
guest = {"login", "logout", "view_file"}
user = {"login", "logout", "view_file", "create_file", "modify_file"}
```

Proszę przechować te zbiory uprawnień w odpowiedniej strukturze danych tak, aby w łatwy sposób dało się odczytać uprawnienia dla danej roli. Następnie proszę napisać program, który spyta użytkownika o dwie różne role w systemie, a następnie poinformuje go, jakie są różnice pomiędzy uprawnieniami poszczególnych ról - przykładowo, między rolami `user`, a `guest` różnice to: `{"create_file", "modify_file"}