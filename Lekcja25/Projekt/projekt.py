import pygame # Wczytanie modułu Pygame
import Element

file_path = Element.file_path

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load(file_path + 'background.png') # Tworzymy obiekt, którzy przechowuje obraz
obraz_postaci = pygame.image.load(file_path + 'base.png')

pygame.init() # Inicjujemy moduł

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU]) # Tworzymy obiekt ekranu ORAZ OKNO

zegar = pygame.time.Clock() # Tworzymy obiekt zegara

pygame.font.init()
moja_czcionka = pygame.font.SysFont('Arial', 30)

nakrycie_glowy = Element.NakrycieGlowy()
ubranie = Element.Ubranie()
oczy = Element.Oczy()
bron = Element.Bron()

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)
    return


gra_dziala = True
zapisywanie = False
while gra_dziala:

    zdarzenia = pygame.event.get() # Lista zdarzeń w Pygame
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT: # typ zdarzenia - zamknięcie okna znakiem X
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN: # typ zdarzenia - wciśnięty klawisz
            if zdarzenie.key == pygame.K_ESCAPE: # okreslenie wciśniętego klawisza jako ESCAPE
                gra_dziala = False
            elif zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            elif zdarzenie.key == pygame.K_w:
                oczy.wybierzNastepny()
            elif zdarzenie.key == pygame.K_e:
                ubranie.wybierzNastepny()
            elif zdarzenie.key == pygame.K_r:
                bron.wybierzNastepny()
            elif zdarzenie.key == pygame.K_s:
                zapisywanie = True


    ekran.blit(obraz_tla, (0, 0)) # dodanie do generowanego ekranu obrazu tła
    ekran.blit(obraz_postaci, (270, 130)) # dodanie do generowanego ekranu obrazu postaci

    ekran.blit(ubranie.wybranyObraz(), (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(bron.wybranyObraz(), (270, 130))

    wypisz_tekst(ekran, f"[Q] Głowa: {nakrycie_glowy.wybrany + 1}", (100, 100))
    wypisz_tekst(ekran, f"[W] Oczy: {oczy.wybrany + 1}", (100, 140))
    wypisz_tekst(ekran, f"[E] Tors: {ubranie.wybrany + 1}", (100, 180))
    wypisz_tekst(ekran, f"[R] Broń: {bron.wybrany + 1}", (100, 220))
    wypisz_tekst(ekran, f"[S] Zapisz (50zł)", (100, 260))

    if zapisywanie:
        pygame.image.save(ekran, f"{file_path}postac.png")
        zapisywanie = False

    pygame.display.flip() # aktualizacja ekranu

    zegar.tick(30) # ograniczenie klatek na sekundę do 30


pygame.quit() # zakończenie używania pygame