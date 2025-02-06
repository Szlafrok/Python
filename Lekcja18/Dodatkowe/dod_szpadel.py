from dod_dawid import najdluzszy_ciag_rosnacy

def oblicz_ciag_rosnacy (ciag: list) -> None:
    lista_serii = []
    lista_ciagow = []
    seria = 0
    ciag_rosnacy = []
    for num in ciag:
        if ciag.index(num) + 1 == len(ciag): # Tu jest pierwszy błąd - ten sposób wysypie się, jeżeli liczby w ciągu powtarzają się
            if (ciag[-1]) - ciag[-2] > 0:
                seria += 1
                ciag_rosnacy.append(num)
                lista_serii.append(seria)
                lista_ciagow.append(ciag_rosnacy)
                continue
            else:
                lista_serii.append(seria)
                lista_ciagow.append(ciag_rosnacy)
                seria = 1
                ciag_rosnacy = [num]
        else: # jeżeli to nie ostatni element ciągu
            if (ciag[ciag.index(num) + 1]) - num > 0: # Jeżeli sprawdzasz, czy ten ciąg jest rosnący, to w ten sposób chcesz weryfikować różnicę :P
                seria += 1
                ciag_rosnacy.append(num) # ? Robisz to po to, aby potem posortować te ciągi?
                continue # nie potrzebujesz dawać continue, po wyjściu z tego ifa przejdziesz do następnej iteracji
            else:
                lista_serii.append(seria)
                lista_ciagow.append(ciag_rosnacy)
                seria = 1
                ciag_rosnacy = [num]
    
    najdłuższa_seria = lista_serii.index(max(lista_serii)) # Sortowanie list (i wyznaczanie maxa) odbywa się na bazie porównywania pierwszych elementów, nie długości list.
    najdłuższy_ciag = lista_ciagow[najdłuższa_seria]
    print(f"Najdłuższy jest ciąg: {najdłuższy_ciag}, miał on {lista_serii[najdłuższa_seria]} znaków długości")
    print(lista_serii)
    print(lista_ciagow)
    print(seria)
    print(ciag_rosnacy)

L = [2, 8, 3, 4, 5, 6, 1]
oblicz_ciag_rosnacy(L)

# Coś Ci dzwoniło, ale masz błędy w implementacji i zdecydowanie za bardzo ją przekomplikowałeś :/

# (+1 / 3)