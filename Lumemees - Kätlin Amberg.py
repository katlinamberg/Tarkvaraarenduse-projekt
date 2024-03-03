import pygame  # pygame import, mis võimaldab luua mänge ja graafikat
import sys  # sys import, mis annab meile ligipääsu süsteemi funktsioonidele

# Pygame init valmistab ette funktsioonid mänguakna loomiseks
pygame.init()

# Ekraani suuruse määramine
ekraani_laius, ekraani_korgus = 300, 300
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])  # Uue ekraani loomine määratud suurusega
pygame.display.set_caption("Lumemees - Kätlin Amberg")  # Määrame akna pealkirja
ekraan.fill((0, 0, 0))  # Täidame ekraani musta värviga

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

pygame.display.flip()  # Värskendame ekraani, et joonistused oleksid nähtavad

# Sündmuste tsükkel
jookseb = True
while jookseb:  # Tsükkel kestab seni, kuni jookseb muutuja on True
    for sündmus in pygame.event.get():  # Käime läbi kõik sündmused pygame sündmuste järjendist
        if sündmus.type == pygame.QUIT:  # Kui sündmuse tüüp on "QUIT", siis aken suletakse
            jookseb = False  # Muudame jookseb muutuja väärtuseks False, mis lõpetab tsükli

# Lõpetamine
pygame.quit()  # Lõpetame Pygame'i kasutamise
sys.exit()  # Lõpetame programmi täitmise
