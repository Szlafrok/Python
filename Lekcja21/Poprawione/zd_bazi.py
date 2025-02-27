class Student():
    ocena_mat = 0.0
    ocena_inf = 0.0
    ocena_wf = 0.0


    def __init__(self, nazwisko, ocena_mat, ocena_inf, ocena_wf):
        self.nazwisko = nazwisko
        self.ocena_mat = ocena_mat
        self.ocena_inf = ocena_inf
        self.ocena_wf = ocena_wf
        self.srednia = (self.ocena_mat + self.ocena_inf + self.ocena_wf) / 3
    
    
   
    def zdane(self):
        if self.ocena_mat >= 3 and self.ocena_inf >= 3 and self.ocena_wf >= 3:
            print("gratulacje zdałeś każdy przedmiot")
        else:
            print("przykro mi czegoś nie zdałeś")

    def wypisz_oceny(self):
        print(f"ocena z matmy: {self.ocena_mat} ocena z infy: {self.ocena_inf} ocena z wf: {self.ocena_wf}. Średnia: {self.srednia}")


zak = Student("Patryk", 5, 5, 3.5)
zak.zdane()
zak.wypisz_oceny()

# (3/5)