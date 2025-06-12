Proszę przygotować struktury przechowująceuprawnienia poszczególnych użytkowników - przykładowo użytkownicy: `root`, `admin`, `operator`, `user`, `guest`, itd. Przykładowo:
```py
guest = {"login", "logout", "view_file"}
user = {"login", "logout", "view_file", "create_file", "modify_file"}
```
Następnie proszę opracować program, który będzie wyświetlał 