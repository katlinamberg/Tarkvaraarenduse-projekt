import pygame
import sys

pygame.init()

# Ekraani seaded
ekraani_laius, ekraani_korgus = 300, 300
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])
pygame.display.set_caption("Lumemees - Kätlin Amberg")
ekraan.fill((0, 0, 0))  # Tausta värv on must

# Lumememme joonistamine kolme valge ringiga
pygame.draw.circle(ekraan, (255, 255, 255), (150, 250), 50)  # Alumine ring
pygame.draw.circle(ekraan, (255, 255, 255), (150, 170), 40)  # Keskmise ring
pygame.draw.circle(ekraan, (255, 255, 255), (150, 120), 30)  # Ülemine ring

# Mustade silmade joonistamine
pygame.draw.circle(ekraan, (0, 0, 0), (140, 110), 5)  # Vasak silm
pygame.draw.circle(ekraan, (0, 0, 0), (160, 110), 5)  # Parem silm

# Punase ninaga kolmnurga joonistamine, kus terav ots on ülespoole suunatud
nina_pikkus = 15
pygame.draw.polygon(ekraan, (255, 0, 0), [(150, 120 + nina_pikkus),
                                            (150 - nina_pikkus // 2, 120),
                                            (150 + nina_pikkus // 2, 120)])  # Nina

pygame.display.flip()

# Sündmuste tsükkel
jookseb = True
while jookseb:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            jookseb = False

# Lõpetamine
pygame.quit()
sys.exit()
