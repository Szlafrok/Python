# oceny = []

# while True:
#     ocena = input("Podaj ocenę: ")
#     if ocena== "q":
#         break

#     ocena = int(ocena)
#     oceny.append(ocena)
#     print(oceny)
#     pass

# suma_ocen = sum(oceny)
# srednia = suma_ocen/len(oceny)
# print(srednia)

lista = [10,20,30,40,50,60,80,90]
                       
# for i in range(len(lista)):
#     print(lista[len(lista) - 1 - i])

nowa_lista = lista[-5:-1]
print(nowa_lista)

liczby = [2,5,6,8,2,4]
wynik = 1
for a in liczby:
    wynik *= a
    pass
print(wynik)

slowo="mama"
for i in slowo:
    print(i)
