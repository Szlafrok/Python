def najdluzszy_ciag_rosnacy(L):
    if not L:
        return[]
    
    max_ciag = []
    akt_ciag = [L[0]]
    for i in range(1, len(L)):
        if L[i] > L[i-1]:
            akt_ciag.append(L[i])
            # robiąc weryfikację, czy len(akt_ciag) > len(max_ciag) tutaj, nie musiałbyś sprawdzać przyp. szczeg.
        else:
            if len(akt_ciag) > len(max_ciag):
                max_ciag = akt_ciag
            akt_ciag = [L[i]]

    if len(akt_ciag) > len(max_ciag): # Przypadek szczególny - OK
        max_ciag = akt_ciag
    return max_ciag

L = [2, 4, 3, 4, 5, 1]
najdluzszy_ciag = najdluzszy_ciag_rosnacy(L)

print(najdluzszy_ciag)

# Rozwiązanie prawie poprawne, nie przeczytałeś uważnie zadania!
# Trzeba było zwrócić długość maksymalnego podciągu, nie sam maksymalny
# podciąg - mógłbyś zrobić po prostu return len(max_ciag), ale program
# byłby nieoptymalny - trzebaby od początku przechowywać same długości,
# nie podciągi :P

# (+2.5 / 3)