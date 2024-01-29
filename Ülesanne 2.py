import pygame
import sys

pygame.init()

# Ekraani seaded
ekraani_laius, ekraani_korgus = 640, 480
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])
pygame.display.set_caption("Ülesanne 2")

# Piltide laadimine
taust = pygame.image.load("bg_shop.jpeg")
poemyyja = pygame.image.load("seller.jpeg")
poemyyja = pygame.transform.scale(poemyyja, (255, 310))
jutumull = pygame.image.load("chat.jpeg")
jutumull = pygame.transform.scale(jutumull, (255, 200))

# Jutumulli tekst
font = pygame.font.SysFont("tahoma", 16)  # Font on Tahoma
tekst = "Tere, olen Kätlin Amberg"
tekst_pildina = font.render(tekst, True, (255, 255, 255))

# Mängutsükkel
jookseb = True
while jookseb:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            jookseb = False

    # Tausta joonistamine
    ekraan.blit(taust, (0, 0))

    # Poemüüja ja jutumulli joonistamine
    poemyyja_koord = (100, 150)
    ekraan.blit(poemyyja, poemyyja_koord)

    # Määran jutumulli asukoha pikslites
    x_koord_jutumull = 250  # Muuta vastavalt soovile
    y_koord_jutumull = 60  # Muuta vastavalt soovile
    ekraan.blit(jutumull, (x_koord_jutumull, y_koord_jutumull))

    # Määran tekstile asukoha jutumulli suhtes
    tekst_laius, tekst_korgus = font.size(tekst)
    x_koord_tekst = x_koord_jutumull + (jutumull.get_width() - tekst_laius) // 2
    y_koord_tekst = y_koord_jutumull + (jutumull.get_height() - tekst_korgus) // 2
    ekraan.blit(tekst_pildina, (x_koord_tekst, y_koord_tekst))

    pygame.display.flip()

# Lõpetamine
pygame.quit()
sys.exit()
