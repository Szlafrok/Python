from pprint import pprint

lista = [1, 2, 3, 4, 5]
student = {
    "imie":"Piotrek",
    "nazwisko":"Polański",
    "miasto":"Kraków",
    "srednia":4.30,
    "wzrost":"krasnoludkiem nie jest",
    "stopien_spiwniczenia":"jaskiniowiec (wersja premium)",
    15: "Story"
}

print(student["imie"])
print(student["srednia"])
#print(student["pesel"])
print(student.get("pesel"))


for value in student.values():
    print(value)

for key in student.keys():
    print(key)

for key, value in student.items():
    print(key, value)

pprint(student)

student.setdefault("wiek", 20)
pprint(student)

#last_item = student.popitem()
#print(last_item)

del student["wiek"]
pprint(student)


print(student[15])

student.clear()
print(student)

# JSON - JavaScript Object Notification