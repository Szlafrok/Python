import pygame
import Element

file_path = Element.file_path

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600


obraz_tla = pygame.image.load(file_path + "background.png")
postac = pygame.image.load(file_path + "base.png" )

pygame.init()



ekran = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
zegar = pygame.time.Clock()

pygame.font.init()
czcionka = pygame.font.SysFont('Arial', 30)



nakrycie_glowy =  Element.NakrycieGlowy()
ubranie = Element.Ubranie()
oczy = Element.Oczy()
bron = Element.Bron()

def wypisz_tekst(ekran, tekst, pozycja):
    napis = czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)
kom_cz = 0
gra_dziala = True
zapisywanie = False
while gra_dziala:

    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
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
        #naciśnięcie przycisku X aby zamknąć okno
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
            
    ekran.blit(obraz_tla, (0, 0) )
    
    ekran.blit(postac, (270, 130))

    ekran.blit(ubranie.wybranyObraz(),(270, 130))
    ekran.blit(oczy.wybranyObraz(),(270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(),(270, 130))
    ekran.blit(bron.wybranyObraz(),(270, 130))
#____________________________________________zadamie domowe______________________________
    if zapisywanie:
        pygame.image.save(ekran, f'{file_path}postac.png')
        zapisywanie = False
        kom_cz = pygame.time.get_ticks() + 3000 # czas wyświetlania
#___________________________________________________________________________________-_____
    wypisz_tekst(ekran, f'[Q] Glowa: {nakrycie_glowy.wybrany + 1}', (100, 100))
    wypisz_tekst(ekran, f'[W] Oczy: {oczy.wybrany + 1}', (100, 140))
    wypisz_tekst(ekran, f'[E] tors: {ubranie.wybrany + 1}', (100, 180))
    wypisz_tekst(ekran, f'[R] Bron: {bron.wybrany + 1}', (100, 220))
    wypisz_tekst(ekran, f'[S] Zapisz (50PLN) ', (100,260))
#_____________________________reszta funkcji________________
    if pygame.time.get_ticks() < kom_cz:
        wypisz_tekst(ekran, "Plik zapisano", (SZEROKOSC_EKRANU // 2 - 100, 50))
#__________________________________________
    pygame.display.flip()


    zegar.tick(30)


pygame.quit()

# Elegancko! 4/4

# Da się to zrobić bez pygame.time.get_ticks(), pokażę tę metodę jak skończy się czas zadania ;)