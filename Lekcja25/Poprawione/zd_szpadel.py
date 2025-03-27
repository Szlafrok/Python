import pygame
import Element

file_path = Element.file_path

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load(file_path + "background.png")
obraz_postaci = pygame.image.load(file_path + "base.png")

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

pygame.font.init()
moja_czcionka = pygame.font.SysFont("Consolas", 35)

nakrycie_glowy = Element.NakrycieGlowy()
ubranie = Element.Ubranie()
oczy = Element.Oczy()
bron = Element.Bron()

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

gra_dziala = True
zapisywanie = False
# czas komunikatu określa kiedy zaczęliśmy wyświetlać komunikat
czas_komunikatu = 0

while gra_dziala:
    zdarzenia = pygame.event.get()

    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            elif zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_w:
                oczy.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_e:
                ubranie.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_r:
                bron.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_s:
                zapisywanie = True

    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(obraz_postaci, (270, 130))

    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(ubranie.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(bron.wybranyObraz(), (270, 130))

    wypisz_tekst(ekran, f"[Q] Głowa: {nakrycie_glowy.wybrany + 1}", (50, 100))
    wypisz_tekst(ekran, f"[W] Oczy: {oczy.wybrany + 1}", (50, 140))
    wypisz_tekst(ekran, f"[E] Ubranie: {ubranie.wybrany + 1}", (50, 180))
    wypisz_tekst(ekran, f"[R] Broń: {bron.wybrany + 1}", (50, 220))
    wypisz_tekst(ekran, f"[S] Zapisz", (50, 260))

    if zapisywanie:
        pygame.image.save(ekran, f"{file_path}postac.png")
        zapisywanie = False
        # sprawdzamy aktualny czas w milisekundach
        czas_komunikatu = pygame.time.get_ticks()

    # sprawdzamy czy nadal mamy wyświetlać komunkikat
    if czas_komunikatu > 0:
        wypisz_tekst(ekran, "Plik zapisano", (270, 470))

        # sprawdzamy aktualną różnicę miedzy aktualnym czasem a czasem komunikatu
        # aby określić czy nadal mamy go wyświetlać
        if pygame.time.get_ticks() - czas_komunikatu >= 3000:
            czas_komunikatu = 0

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
quit()


# Sprytnie! 4/4 :)

# Da się to zrobić bez pygame.time.get_ticks(), pokażę tę metodę jak skończy się czas zadania ;)