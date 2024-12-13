# Ten skrypt pozwala sprawdzić bieżącą ścieżkę, w której działa interpreter Pythona.
# (Interpreter to program, który przechodzi przez napisany kod i wykonuje go)
# Dzięki temu możemy wyznaczyć ścieżkę względną do pliku, np. z grafiką.

# PRZYKŁAD: 
# Pełna ścieżka do pliku graficznego:
#    C:\Users\Giganci\Desktop\Python\Lekcja12\grafiki\player.png

# Jeśli interpreter działa w folderze:
#    C:\Users\Giganci\Desktop\Python
# To ścieżka względna do pliku to:
file_path = "Lekcja12/grafiki/player.png"

# Kod wyświetla bieżący folder, w którym pracuje interpreter:
import os
print(f"\nŚcieżka do katalogu roboczego: {os.getcwd()}\n")