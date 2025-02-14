u1_1 = "Jan"
u1_2 = "Nowak"
u1_3 = 52
u2_1 = "Maciej"
u2_2 = "Laczek"
u2_3 = 13
u3_1 = "Adam"
u3_2 = "Kowalski"
u3_3 = 19

def pelnoletnosc(wiek):
    if wiek >= 18:
        return "Brawo jestes pelnoletni"
    else:
        return "Niestety poczekaj jeszcze pare lat"

print(u1_1 ,u1_2 ,u1_3)
print(pelnoletnosc(u1_3))

print(u2_1 ,u2_2 ,u2_3)
print(pelnoletnosc(u2_3))

print(u3_1 ,u3_2 ,u3_3)
print(pelnoletnosc(u3_3))

#print(u4_1 ,u1_2 ,u1_3)
